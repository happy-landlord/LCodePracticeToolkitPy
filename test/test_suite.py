import importlib
import os
import sys
import inspect
from typing import get_origin, get_args, Optional

from libs.linked_list import ListNode, LinkedList

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


def convert_for_check(test_case, raw_actual, method_signature):
    expected = test_case["expected"]
    return_annotation = method_signature.return_annotation

    if "pos" in test_case and not isinstance(expected, bool):
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
            # 返回新链表：None 表示空链表
            if return_annotation is ListNode or return_annotation == Optional[ListNode]:
                return []
            # 原地修改：检查 head 的当前状态
            if return_annotation is None and "head" in test_case and hasattr(test_case["head"], "to_safe_list"):
                return test_case["head"].to_safe_list()[0]
            return []
        if isinstance(raw_actual, ListNode):
            return raw_actual.to_safe_list()[0]
        elif hasattr(raw_actual, "to_list") and callable(raw_actual.to_list):
            return raw_actual.to_list()
        else:
            return raw_actual


def convert_for_print(test_case, raw_actual, head_arg, method_signature):
    expected = test_case["expected"]
    return_annotation = method_signature.return_annotation

    if raw_actual is None:
        # 返回新链表：None 表示空链表
        if return_annotation is ListNode or return_annotation == Optional[ListNode]:
            return []
        # 原地修改：使用传入的 head_arg
        if return_annotation is None and head_arg is not None and hasattr(head_arg, "to_safe_list"):
            return head_arg.to_safe_list()[0]
        return []
    if isinstance(raw_actual, ListNode):
        return raw_actual.to_safe_list()[0]
    elif hasattr(raw_actual, "to_list") and callable(raw_actual.to_list):
        return raw_actual.to_list()
    else:
        return raw_actual


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
    solution = problem_module.Solution()
    method_names = [name for name in dir(solution) if callable(getattr(solution, name)) and not name.startswith('__')]
    if not method_names or not test_cases:
        print(f"No callable methods or test cases found in module {problem_number}")
        return
    first_test_case = test_cases[0]
    if "method" not in first_test_case:
        print("Test case must specify 'method' key")
        return
    method_name = first_test_case["method"]
    if method_name not in method_names:
        print(f"Method {method_name} not found")
        return
    method = getattr(solution, method_name)
    signature = inspect.signature(method)

    preprocess_test_cases(test_cases, signature)

    results = []
    emojis = []
    total_tests = len(test_cases)
    passed_tests = 0
    key_width = 10

    for test_case in test_cases:
        case_id = str(test_case["case_id"])
        expected = test_case["expected"]
        args = []
        for param_name, param in signature.parameters.items():
            if param_name not in test_case:
                results.append(f"Missing parameter {param_name} in test case {case_id}")
                break
            arg = test_case[param_name]
            if param.annotation is not inspect.Parameter.empty:
                anno = param.annotation
                origin = get_origin(anno)
                if origin is None:
                    if anno is ListNode and isinstance(arg, list):
                        arg = ListNode.from_list(arg)
                else:
                    if ListNode in get_args(anno) and isinstance(arg, list):
                        arg = ListNode.from_list(arg)
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
                printable = convert_for_print(test_case, raw_actual, args[0], signature)
                case_label = f"Case {case_id}"
                padding = key_width - len(case_label)
                input_args = []
                for k in signature.parameters.keys():
                    value = test_case[k]
                    if k == "head" and "_original_list" in test_case:
                        if "pos" in test_case:
                            input_args.append(f"{k} = {test_case['_original_list']}, pos = {test_case['pos']}")
                        else:
                            input_args.append(f"{k} = {test_case['_original_list']}")
                    else:
                        input_args.append(f"{k} = {value}")
                case_output = [
                    f"{' ' * padding}{case_label} : {'✅' if passed else '☹️'}",
                    f"{'Input':>10} : {', '.join(input_args)}",
                    f"{'Expected':>10} : {expected}",
                    f"{'Actual':>10} : {printable}",
                    ""
                ]
                results.extend(case_output)
            except Exception as e:
                results.append(f"Error executing {method_name} for test case {case_id}: {e}")
                emojis.append('☹️')
    pass_percentage = round((passed_tests / total_tests) * 100) if total_tests > 0 else 0
    title = f"LeetCode {problem_number} {''.join(emojis)}"
    output = [title, "", f"{pass_percentage}% passed"]
    if pass_percentage < 100:
        output.append("")
        output.extend(results)
    print("\n".join(output))


def preprocess_test_cases(test_cases, signature):
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
