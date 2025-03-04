# 128.py
from test.test_suite import run_tests


# 128. Longest Consecutive Sequence

# Given an unsorted array of integers `nums`, return the **length of the longest consecutive elements sequence**.
#
# You must write an algorithm that runs in **O(n) time**.
#
# ### Constraints:
# - `0 <= nums.length <= 10^5`
# - `-10^9 <= nums[i] <= 10^9`
#
# ### Examples:
#
# #### Example 1:
# **Input:** nums = [100, 4, 200, 1, 3, 2]
# **Output:** 4
# **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore, its length is `4`.
#
# #### Example 2:
# **Input:** nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# **Output:** 9
#
# #### Example 3:
# **Input:** nums = []
# **Output:** 0
#
# #### Example 4:
# **Input:** nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# **Output:** 7
#
# #### Example 5:
# **Input:** nums = [1, 2, 0, 1]
# **Output:** 3
#
# Key Insight: Each number in the set is only visited once as part of a sequence. Why? You only start counting from the smallest number in a sequence (when num - 1 not in s is true), and every subsequent number in that sequence is skipped in the outer loop because it fails the `num - 1 not in s` check. Thus, the inner while loop collectively across all iterations processes each element in s at most once.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        max_length = 0

        for num in s:
            if num - 1 not in s:  # 只从“序列起点”开始计算
                length = 1
                while num + length in s:
                    length += 1
                max_length = max(max_length, length)

        return max_length


test_cases = [
    {
        "method": "longestConsecutive",
        "nums": [100, 4, 200, 1, 3, 2],
        "expected": 4,
        "case_id": 1
    },
    {
        "method": "longestConsecutive",
        "nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        "expected": 9,
        "case_id": 2
    },
    {
        "method": "longestConsecutive",
        "nums": [],
        "expected": 0,
        "case_id": 3
    },
    {
        "method": "longestConsecutive",
        "nums": [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        "expected": 7,
        "case_id": 4
    },
    {
        "method": "longestConsecutive",
        "nums": [1, 2, 0, 1],
        "expected": 3,
        "case_id": 5
    }
]

run_tests()
