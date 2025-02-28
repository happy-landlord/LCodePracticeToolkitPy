# test/test_suite.py
import importlib
import os
import sys
import inspect
from typing import Any, Dict, List

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
    param_names = list(signature.parameters.keys())

    # 存储所有测试结果和表情符号
    results = []
    emojis = []
    total_tests = len(test_cases)
    passed_tests = 0

    # 计算最长的 case ID 长度
    max_case_id_len = max(len(str(test_case["case_id"])) for test_case in test_cases)
    key_width = 10  # Input/Expected/Actual 的固定宽度

    # 执行所有测试用例
    for test_case in test_cases:
        case_id = str(test_case["case_id"])
        expected = test_case["expected"]

        args = []
        for param_name in param_names:
            if param_name not in test_case:
                results.append(f"Missing parameter {param_name} in test case {case_id}")
                break
            args.append(test_case[param_name])
        else:
            try:
                actual = method(*args)
                passed = actual == expected
                if passed:
                    passed_tests += 1
                    emojis.append('✅')
                else:
                    emojis.append('☹️')

                # 动态计算 Case 行的 padding
                case_label = f"Case {case_id}"
                padding = key_width - len(case_label)

                # 格式化单个测试用例的输出
                case_output = [
                    f"{' ' * padding}{case_label} : {'✅' if passed else '☹️'}",
                    f"{'Input':>10} : {', '.join(f'{param_names[i]} = {args[i]}' for i in range(len(args)))}",
                    f"{'Expected':>10} : {expected}",
                    f"{'Actual':>10} : {actual}",
                    ""
                ]
                results.extend(case_output)
            except Exception as e:
                results.append(f"Error executing {method_name} for test case {case_id}: {e}")
                emojis.append('☹️')

    # 计算通过率
    pass_percentage = round((passed_tests / total_tests) * 100) if total_tests > 0 else 0

    # 构建标题行
    title = f"LeetCode {problem_number} {''.join(emojis)}"

    # 构建最终输出
    output = [
        title,
        "",
        f"{pass_percentage}% passed",
    ]

    # 如果不是 100% 通过，才添加具体 Case 详情
    if pass_percentage < 100:
        output.append("")
        output.extend(results)

    # 一次性打印所有内容
    print("\n".join(output))
