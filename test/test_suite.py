# test/test_suite.py
import importlib
import os
import sys
import inspect
from typing import get_origin, get_args, Optional, List, Any, get_type_hints
from collections import deque
from libs.linked_list import ListNode, LinkedList
from libs.tree import TreeNode

_tests_executed = False


def convert_result(test_case, actual):
    if "pos" in test_case and not isinstance(test_case["expected"], bool):
        if actual is None:
            return None
        orig = test_case.get("_original_list")
        if orig is None:
            return actual.to_safe_list()[0]
        index = 0
        curr = test_case["head"]
        found = -1
        limit = len(orig)
        while curr and index < limit:
            if curr == actual:
                found = index
                break
            curr = curr.next
            index += 1
        return found
    else:
        if actual is None:
            if "head" in test_case and hasattr(test_case["head"], "to_safe_list"):
                return test_case["head"].to_safe_list()[0]
            return None
        if isinstance(actual, ListNode):
            return actual.to_safe_list()[0]
        elif hasattr(actual, "to_list") and callable(actual.to_list):
            return actual.to_list()
        else:
            return actual


def is_scalar(obj):
    """判断对象是否是标量类型（int, float, bool, str 等）"""
    return isinstance(obj, (int, float, bool, str))


def is_tree_node(obj):
    """采用鸭子类型判断是否是树节点：只要有 val、left、right 属性即可"""
    return hasattr(obj, "val") and hasattr(obj, "left") and hasattr(obj, "right")


def adjust_tree_output(raw_list: List[Optional[Any]], expected: List[Optional[Any]]) -> List[Optional[Any]]:
    """根据 expected 的格式调整树的层序遍历输出"""
    if not expected:
        return []
    expected_non_none_count = sum(1 for x in expected if x is not None)
    raw_non_none_count = sum(1 for x in raw_list if x is not None)
    if expected_non_none_count != raw_non_none_count:
        return raw_list
    expected_len = len(expected)
    result = raw_list[:expected_len]
    while len(result) < expected_len:
        result.append(None)
    if expected and expected[-1] is not None:
        while result and result[-1] is None:
            result.pop()
    return result


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[Any]]:
    if not root:
        return []
    result: List[Optional[Any]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result


def convert_for_check(test_case, raw_actual, method_signature):
    expected = test_case["expected"]
    return_annotation = method_signature.return_annotation
    if "pos" in test_case and not isinstance(test_case["expected"], bool):
        if raw_actual is None:
            return None
        limit = len(test_case["_original_list"])
        curr = test_case["head"]
        found = -1
        for idx in range(limit):
            if curr == raw_actual:
                found = idx
                break
            curr = curr.next
        return found
    else:
        if raw_actual is None:
            if return_annotation is ListNode or return_annotation == Optional[ListNode]:
                return []
            if return_annotation is None and "head" in test_case and hasattr(test_case["head"], "to_safe_list"):
                return test_case["head"].to_safe_list()[0]
            return None
        if isinstance(raw_actual, ListNode):
            return raw_actual.to_safe_list()[0]
        if is_tree_node(raw_actual):
            if is_scalar(expected):
                return raw_actual.val if raw_actual else None
            raw_list = tree_to_list(raw_actual)
            return adjust_tree_output(raw_list, expected)
        if hasattr(raw_actual, "to_list") and callable(raw_actual.to_list):
            return raw_actual.to_list()
        else:
            return raw_actual


def convert_for_print(test_case, raw_actual, head_arg, method_signature):
    return_annotation = method_signature.return_annotation
    if raw_actual is None:
        if return_annotation is ListNode or return_annotation == Optional[ListNode]:
            return []
        try:
            from libs.tree import TreeNode
            if return_annotation == TreeNode or return_annotation == Optional[TreeNode]:
                return None if is_scalar(test_case["expected"]) else []
        except ImportError:
            pass
        if return_annotation is None and head_arg is not None and hasattr(head_arg, "to_safe_list"):
            return head_arg.to_safe_list()[0]
        return None if is_scalar(test_case["expected"]) else []
    if isinstance(raw_actual, ListNode):
        return raw_actual.to_safe_list()[0]
    if is_tree_node(raw_actual):
        if is_scalar(test_case["expected"]):
            return raw_actual.val if raw_actual else None
        raw_list = tree_to_list(raw_actual)
        return adjust_tree_output(raw_list, test_case["expected"])
    if hasattr(raw_actual, "to_list") and callable(raw_actual.to_list):
        return raw_actual.to_list()
    else:
        return raw_actual


def preprocess_tree_params(test_cases, method):
    """预处理所有树参数（包括 args 中的树参数）"""
    from libs.tree import build_tree_from_list, TreeNode
    hints = get_type_hints(method)
    for test_case in test_cases:
        # 处理 top-level 参数
        for param, expected_type in hints.items():
            if expected_type is TreeNode or expected_type == Optional[TreeNode]:
                if param in test_case and isinstance(test_case[param], list):
                    test_case[param] = build_tree_from_list(test_case[param]) if test_case[param] else None
        # 处理 args 中的参数
        if "args" in test_case and isinstance(test_case["args"], list):
            for i, arg in enumerate(test_case["args"]):
                if isinstance(arg, list) and arg:  # 确保非空列表
                    test_case["args"][i] = build_tree_from_list(arg) if arg else None


def run_composite_tests(solution, test_case, signature_dict):
    """运行组合方法测试，例如 serialize -> deserialize"""
    case_id = str(test_case["case_id"])
    expected = test_case["expected"]
    methods = test_case["method"]
    args_list = test_case.get("args", [])

    try:
        intermediate_result = None
        for i, method_name in enumerate(methods):
            method = getattr(solution, method_name)
            signature = signature_dict[method_name]
            params = list(signature.parameters.keys())
            if i < len(args_list) and args_list[i] is not None:
                arg = args_list[i]
                if not isinstance(arg, (TreeNode, type(None))):
                    raise ValueError(f"Invalid argument type for {method_name}: {type(arg)}")
                intermediate_result = method(arg)
            else:
                intermediate_result = method(intermediate_result)

        actual = convert_for_check(test_case, intermediate_result, signature_dict[methods[-1]])
        printable = convert_for_print(test_case, intermediate_result, args_list[0] if args_list else None,
                                      signature_dict[methods[-1]])
        input_args = [f"{params[0]} = {args_list[0]}" if args_list and args_list[0] else ""] if params else []

        return {
            "passed": actual == expected,
            "case_label": f"Case {case_id}",
            "input": f"{'Input':>10} : {', '.join(input_args)}",
            "expected": f"{'Expected':>10} : {expected}",
            "actual": f"{'Actual':>10} : {printable}"
        }
    except Exception as e:
        return {
            "passed": False,
            "case_label": f"Case {case_id}",
            "error": f"Error executing composite methods: {e}"
        }


def run_tests():
    global _tests_executed
    if _tests_executed:
        return
    _tests_executed = True

    test_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(test_dir)
    if root_dir not in sys.path:
        sys.path.append(root_dir)
    caller_frame = inspect.currentframe().f_back
    if caller_frame is None:
        print("Error: Cannot determine caller frame.")
        return
    caller_file = os.path.basename(caller_frame.f_code.co_filename)
    problem_number = os.path.splitext(caller_file)[0]

    try:
        problem_module = importlib.import_module(f"{problem_number}")
    except ImportError as e:
        print(f"Error importing module {problem_number}: {e}")
        return
    if not hasattr(problem_module, 'test_cases'):
        print(f"No test_cases found in module {problem_number}")
        return
    test_cases = problem_module.test_cases

    solution_class = None
    for name, obj in inspect.getmembers(problem_module, inspect.isclass):
        if obj.__module__ == problem_module.__name__ and name != "TreeNode" and name != "ListNode":
            solution_class = obj
            break
    if not solution_class:
        print(f"No solution class (e.g., Solution or Codec) found in module {problem_number}")
        return
    solution = solution_class()

    method_names = [name for name in dir(solution) if callable(getattr(solution, name)) and not name.startswith('__')]
    if not method_names or not test_cases:
        print(f"No callable methods or test cases found in module {problem_number}")
        return

    first_test_case = test_cases[0]
    if "method" not in first_test_case:
        print("Test case must specify 'method' key")
        return

    signature_dict = {name: inspect.signature(getattr(solution, name)) for name in method_names}

    for test_case in test_cases:
        if isinstance(test_case["method"], str):
            method = getattr(solution, test_case["method"])
            preprocess_tree_params([test_case], method)
            preprocess_test_cases([test_case], signature_dict[test_case["method"]])
        else:
            method = getattr(solution, test_case["method"][0])
            preprocess_tree_params([test_case], method)

    results = []
    emojis = []
    total_tests = len(test_cases)
    passed_tests = 0
    key_width = 10

    for test_case in test_cases:
        if isinstance(test_case["method"], list):
            result = run_composite_tests(solution, test_case, signature_dict)
            passed = result["passed"]
            if passed:
                passed_tests += 1
                emojis.append('✅')
            else:
                emojis.append('☹️')
            padding = key_width - len(result["case_label"])
            if "error" in result:
                results.append(result["error"])
            else:
                results.extend([
                    f"{' ' * padding}{result['case_label']} : {'✅' if passed else '☹️'}",
                    result["input"],
                    result["expected"],
                    result["actual"],
                    ""
                ])
        else:
            method_name = test_case["method"]
            if method_name not in method_names:
                print(f"Method {method_name} not found")
                return
            method = getattr(solution, method_name)
            signature = signature_dict[method_name]
            expected = test_case["expected"]
            args = []
            for param_name, param in signature.parameters.items():
                if param_name not in test_case:
                    results.append(f"Missing parameter {param_name} in test case {test_case['case_id']}")
                    break
                arg = test_case[param_name]
                args.append(arg)
            else:
                try:
                    raw_actual = method(*args)
                    check_actual = convert_for_check(test_case, raw_actual, signature)
                    passed = (check_actual == expected)
                    if passed:
                        passed_tests += 1
                        emojis.append('✅')
                    else:
                        emojis.append('☹️')
                    printable = convert_for_print(test_case, raw_actual, args[0] if args else None, signature)
                    case_label = f"Case {test_case['case_id']}"
                    padding = key_width - len(case_label)
                    input_args = []
                    for i, k in enumerate(signature.parameters.keys()):
                        value = test_case[k]
                        if is_tree_node(value):
                            value = tree_to_list(value)
                        input_args.append(f"{k} = {value}")
                    results.extend([
                        f"{' ' * padding}{case_label} : {'✅' if passed else '☹️'}",
                        f"{'Input':>10} : {', '.join(input_args)}",
                        f"{'Expected':>10} : {expected}",
                        f"{'Actual':>10} : {printable}",
                        ""
                    ])
                except Exception as e:
                    results.append(f"Error executing {method_name} for test case {test_case['case_id']}: {e}")
                    emojis.append('☹️')

    pass_percentage = round((passed_tests / total_tests) * 100) if total_tests > 0 else 0
    title = f"LeetCode {problem_number} {''.join(emojis)}"
    output = [title, "", f"{pass_percentage}% passed"]
    if pass_percentage < 100:
        output.append("")
        output.extend(results)
    print("\n".join(output))


def preprocess_test_cases(test_cases, signature):
    if not signature:
        return
    has_head_param = any(param_name == "head" for param_name in signature.parameters)
    if not has_head_param:
        return
    for test_case in test_cases:
        if "head" in test_case and isinstance(test_case["head"], list):
            test_case["_original_list"] = test_case["head"].copy()
            linked_list = LinkedList(test_case["head"])
            if "pos" in test_case and test_case["pos"] != -1:
                linked_list.add_cycle(test_case["pos"])
            test_case["head"] = linked_list.head
