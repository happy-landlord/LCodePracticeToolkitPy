# test/test_suite.py
import importlib
import os
import sys
import inspect
from typing import get_origin, get_args

# 从链表模块引入 ListNode 和 LinkedList
from libs.linked_list import ListNode, LinkedList

_tests_executed = False


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
        print(f"Test case must specify 'method' key")
        return

    method_name = first_test_case["method"]
    if method_name not in method_names:
        print(f"Method {method_name} not found")
        return

    method = getattr(solution, method_name)
    signature = inspect.signature(method)

    # 预处理测试用例，特别是处理链表中的环
    preprocess_test_cases(test_cases, signature)

    # 存储所有测试结果和表情符号
    results = []
    emojis = []
    total_tests = len(test_cases)
    passed_tests = 0

    # 固定宽度
    key_width = 10

    # 执行所有测试用例
    for test_case in test_cases:
        case_id = str(test_case["case_id"])
        expected = test_case["expected"]

        args = []
        # 利用类型注解自动转换列表参数
        for param_name, param in signature.parameters.items():
            if param_name not in test_case:
                results.append(f"Missing parameter {param_name} in test case {case_id}")
                break
            arg = test_case[param_name]
            if param.annotation is not inspect.Parameter.empty:
                # 判断该参数是否应该是 ListNode 或 Optional[ListNode]
                anno = param.annotation
                origin = get_origin(anno)
                if origin is None:
                    # 非泛型注解，直接判断是否为 ListNode
                    if anno is ListNode and isinstance(arg, list):
                        arg = ListNode.from_list(arg)
                else:
                    # 泛型注解，如 Optional[ListNode] 通常是 Union[ListNode, NoneType]
                    if ListNode in get_args(anno) and isinstance(arg, list):
                        arg = ListNode.from_list(arg)
            args.append(arg)
        else:
            try:
                actual = method(*args)
                # 如果返回的是链表，则转换为列表进行比较
                if actual is None:
                    actual = []
                elif hasattr(actual, "to_list") and callable(actual.to_list):
                    actual = actual.to_list()
                passed = actual == expected
                if passed:
                    passed_tests += 1
                    emojis.append('✅')
                else:
                    emojis.append('☹️')

                case_label = f"Case {case_id}"
                padding = key_width - len(case_label)

                # 准备输入参数的可读形式
                input_args = []
                for k in signature.parameters.keys():
                    value = test_case[k]
                    # 对于链表参数，显示原始列表和位置信息（如果有）
                    if k == "head" and "pos" in test_case:
                        if "_original_list" in test_case:
                            input_args.append(f"{k} = {test_case['_original_list']}, pos = {test_case['pos']}")
                        else:
                            input_args.append(f"{k} = [链表], pos = {test_case['pos']}")
                    else:
                        input_args.append(f"{k} = {value}")

                case_output = [
                    f"{' ' * padding}{case_label} : {'✅' if passed else '☹️'}",
                    f"{'Input':>10} : {', '.join(input_args)}",
                    f"{'Expected':>10} : {expected}",
                    f"{'Actual':>10} : {actual}",
                    ""
                ]
                results.extend(case_output)
            except Exception as e:
                results.append(f"Error executing {method_name} for test case {case_id}: {e}")
                emojis.append('☹️')

    pass_percentage = round((passed_tests / total_tests) * 100) if total_tests > 0 else 0
    title = f"LeetCode {problem_number} {''.join(emojis)}"

    output = [
        title,
        "",
        f"{pass_percentage}% passed",
    ]

    if pass_percentage < 100:
        output.append("")
        output.extend(results)

    print("\n".join(output))


def preprocess_test_cases(test_cases, signature):
    """
    预处理测试用例，特别是处理可能含有环的链表
    """
    # 检查是否是链表相关题目（方法参数中有 head）
    has_head_param = False
    for param_name in signature.parameters:
        if param_name == "head":
            has_head_param = True
            break

    if not has_head_param:
        return

    for test_case in test_cases:
        # 处理链表中的环
        if "head" in test_case and "pos" in test_case:
            head = test_case["head"]
            pos = test_case["pos"]

            # 保存原始列表以便报告
            if isinstance(head, list):
                test_case["_original_list"] = head.copy()

            # 创建链表并添加环
            linked_list = LinkedList(head)
            if pos >= 0:  # 只有当 pos 有效时才添加环
                linked_list.add_cycle(pos)
            test_case["head"] = linked_list.head
