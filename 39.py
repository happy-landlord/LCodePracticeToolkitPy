from typing import List

from test.test_suite import run_tests


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()  # 排序以便剪枝
#         all_combinations = []
#
#         def dfs(index: int, current_combination: List[int], remaining: int) -> None:
#             print(f"DFS Call: index={index}, current_combination={current_combination}, remaining={remaining}")
#
#             if remaining == 0:  # 找到有效组合
#                 print(f"Found valid combination: {current_combination}")
#                 all_combinations.append(current_combination[:])
#                 return
#             if remaining < 0 or index >= len(candidates):  # 越界或超过目标，终止
#                 print(f"Backtracking: index={index}, remaining={remaining}")
#                 return
#
#             # 选择当前数字，允许重复使用
#             print(f"Trying to include {candidates[index]}")
#             dfs(index, current_combination + [candidates[index]], remaining - candidates[index])
#
#             # 剪枝：如果下一个数字大于 remaining，无需继续尝试
#             if index + 1 < len(candidates) and candidates[index + 1] <= remaining:
#                 print(f"Skipping {candidates[index]}, moving to next index")
#                 dfs(index + 1, current_combination, remaining)
#             else:
#                 print(f"Skipping {candidates[index]}, no need to try larger numbers (remaining={remaining})")
#
#         print(f"Starting combinationSum with candidates={candidates}, target={target}")
#         dfs(0, [], target)
#         print(f"Final combinations: {all_combinations}")
#         return all_combinations
#


class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            if target == 0:  # 当前和等于目标值，记录结果
                result.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:  # 剪枝：当前数字大于剩余目标值
                    break
                path.append(candidates[i])  # 加入当前数字
                backtrack(i, target - candidates[i], path)  # 递归，允许重复使用当前数字
                path.pop()  # 回溯，移除当前数字

        candidates.sort()  # 排序以便剪枝
        backtrack(0, target, [])
        return result



test_cases = [
    {
        "method": "combinationSum",
        "candidates": [2, 3, 6, 7],
        "target": 7,
        "expected": [[2, 2, 3], [7]],
        "case_id": 1
    },
    {
        "method": "combinationSum",
        "candidates": [2, 3, 5],
        "target": 8,
        "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        "case_id": 2
    },
    {
        "method": "combinationSum",
        "candidates": [2],
        "target": 1,
        "expected": [],
        "case_id": 3
    },
    {
        "method": "combinationSum",
        "candidates": [1],
        "target": 4,
        "expected": [[1, 1, 1, 1]],
        "case_id": 4
    }
]

run_tests()
