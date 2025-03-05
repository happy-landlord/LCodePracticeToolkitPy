# 739.py
from test.test_suite import run_tests

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 解法1：单调栈（Monotonic Stack）
        # 使用栈来维护一个单调递减的温度序列。当遇到一个更高的温度时，弹出栈顶元素并计算等待天数。栈中存储的是温度的索引，而不是温度值。

        # 从左到右版本：
        # 初始化结果数组，默认每个位置等待天数为 0
        # n = len(temperatures)
        # wait_days = [0] * n
        # # 栈存储温度的索引，保持单调递减（栈顶温度最低）
        # stack = []
        #
        # # 从左到右遍历每一天的温度
        # for curr_day in range(n):
        #     # 当前温度比栈顶温度高时，弹出栈顶，计算等待天数
        #     while stack and temperatures[curr_day] > temperatures[stack[-1]]:
        #         prev_day = stack.pop()  # 弹出较冷的日子
        #         wait_days[prev_day] = curr_day - prev_day  # 计算等待天数
        #     # 将当前日子压入栈，等待未来更高的温度
        #     stack.append(curr_day)
        #
        # return wait_days

        # 解法1：单调栈（Monotonic Stack）从右到左版本：
        # 初始化结果数组，表示每一天等待更高温度的天数
        n = len(temperatures)
        wait_days = [0] * n
        # 栈存储未来日子（索引），保持单调递减（栈顶温度最低）
        future_days = []

        # 从最后一天向前遍历
        for current_day in range(n - 1, -1, -1):
            # 当前温度 >= 栈顶温度时，移除栈顶，因为它不可能是“下一个更高温度”
            while future_days and temperatures[current_day] >= temperatures[future_days[-1]]:
                future_days.pop()

            # 如果栈不为空，栈顶就是未来第一个更高温度的日子
            if future_days:
                next_warmer_day = future_days[-1]
                wait_days[current_day] = next_warmer_day - current_day

            # 将当前日子加入栈，作为未来日子的候选
            future_days.append(current_day)

        return wait_days
        # 解法2：从右向左遍历（动态规划思想）
        # 思路：从数组末尾开始向前遍历，利用已经计算的结果。对于每一天
        # i，检查右边的日子中是否有更高温度，并利用之前的结果跳跃式查找。

        # n = len(temperatures)
        # result = [0] * n
        # for i in range(n - 2, -1, -1):
        #     j = i + 1
        #     while j < n and temperatures[j] <= temperatures[i]:
        #         if result[j] == 0:
        #             j = n  # 跳到末尾，表示后面没有更高的温度
        #         else:
        #             j += result[j]  # 跳到下一个可能的更高温度的位置
        #     if j < n:
        #         result[i] = j - i
        # return result


test_cases = [
    {
        "method": "dailyTemperatures",
        "temperatures": [73, 74, 75, 71, 69, 72, 76, 73],
        "expected": [1, 1, 4, 2, 1, 1, 0, 0],
        "case_id": 1
    },
    {
        "method": "dailyTemperatures",
        "temperatures": [30, 40, 50, 60],
        "expected": [1, 1, 1, 0],
        "case_id": 2
    },
    {
        "method": "dailyTemperatures",
        "temperatures": [30, 60, 90],
        "expected": [1, 1, 0],
        "case_id": 3
    },
    {
        "method": "dailyTemperatures",
        "temperatures": [90, 80, 70, 60],
        "expected": [0, 0, 0, 0],
        "case_id": 4
    },
    {
        "method": "dailyTemperatures",
        "temperatures": [50, 60, 50, 60, 50, 60, 70],
        "expected": [1, 5, 1, 3, 1, 1, 0],
        "case_id": 5
    },
    {
        "method": "dailyTemperatures",
        "temperatures": [100, 100, 100, 100],
        "expected": [0, 0, 0, 0],
        "case_id": 6
    }
]
run_tests()
