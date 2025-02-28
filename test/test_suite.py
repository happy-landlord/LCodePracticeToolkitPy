# test/test_suite.py
import importlib
import os
import sys
import inspect
from typing import Any, Dict, List

# Global flag to track if tests have been executed
_tests_executed = False


def run_tests():
    global _tests_executed
    if _tests_executed:
        return  # Exit if tests have already been executed

    _tests_executed = True  # Set the flag to True to prevent running tests again

    """运行当前调用者的测试用例"""
    # 获取当前文件的目录（test 目录）
    test_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取项目根目录（test 目录的父目录）
    root_dir = os.path.dirname(test_dir)

    # 将项目根目录添加到 sys.path
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    # 使用 inspect 模块获取调用者的文件名（例如 1768.py 或 389.py）
    caller_frame = inspect.currentframe().f_back
    if caller_frame is None:
        print("Error: Cannot determine caller frame. Ensure run_tests() is called from a valid context.")
        return

    caller_file = os.path.basename(caller_frame.f_code.co_filename)
    problem_number = os.path.splitext(caller_file)[0]  # 从调用者的文件名获取问题号（如 1768）

    try:
        # 动态导入相应的模块（问题模块，如 1768）
        problem_module = importlib.import_module(f"{problem_number}")
    except ImportError as e:
        print(f"Error importing module {problem_number}: {e}")
        return

    # 获取所有的测试用例
    if hasattr(problem_module, 'test_cases'):
        test_cases = problem_module.test_cases
    else:
        print(f"No test_cases found in module {problem_number}")
        return

    # 创建 Solution 实例
    solution = problem_module.Solution()

    # 动态检测 Solution 类中的所有可调用方法
    method_names = [name for name in dir(solution) if callable(getattr(solution, name)) and not name.startswith('__')]
    if not method_names:
        print(f"No callable methods found in Solution for module {problem_number}")
        return

    # 假设测试用例中的第一个用例定义了方法名和参数格式
    if not test_cases:
        print(f"No test cases defined for module {problem_number}")
        return

    first_test_case = test_cases[0]
    if "method" not in first_test_case:
        print(f"Test case must specify 'method' key to indicate which Solution method to test.")
        return

    method_name = first_test_case["method"]
    if method_name not in method_names:
        print(f"Method {method_name} not found in Solution for module {problem_number}")
        return

    method = getattr(solution, method_name)

    # 使用 inspect 获取方法签名，确定参数名称
    signature = inspect.signature(method)
    param_names = list(signature.parameters.keys())

    # 验证测试用例格式
    total_tests = len(test_cases)
    passed_tests = 0

    # 打印标题
    print(f"🎉🎉🎉🎉🎉 LeetCode {problem_number} 🎉🎉🎉🎉🎉\n")

    # 遍历所有测试用例
    for test_case in test_cases:
        case_id = test_case["case_id"]
        expected = test_case["expected"]

        # 提取输入参数，匹配方法签名
        args = []
        for param_name in param_names:
            if param_name not in test_case:
                print(f"Missing parameter {param_name} in test case {case_id} for method {method_name}")
                break
            args.append(test_case[param_name])
        else:
            # 调用方法
            try:
                actual = method(*args)
            except Exception as e:
                print(f"Error executing {method_name} for test case {case_id}: {e}")
                continue

            # 判断是否通过
            if actual == expected:
                result = "✅"
                passed_tests += 1
            else:
                result = "☹️"

            # 输出每个测试用例的结果
            print(f"Test Case {case_id}: {result}")
            print(f"  Input: {', '.join(f'{param_names[i]} = {args[i]}' for i in range(len(args)))}")
            print(f"  Expected: {expected}")
            print(f"  Actual  : {actual}\n")

    # 输出总结
    percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f"Summary: {passed_tests}/{total_tests} tests passed ({percentage:.2f}%)\n")
