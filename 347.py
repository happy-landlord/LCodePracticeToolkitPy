# 347.py
from collections import Counter

from test.test_suite import run_tests
# 347. Top K Frequent Elements

# Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
# - k is in the range [1, the number of unique elements in the array]
# - It is guaranteed that the answer is unique
#
# **Follow up**: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# 时间复杂度：
# 计算Counter: O(n)
# 排序频率: O(m log m)，其中m是不同数字的数量
# 遍历Counter: O(m)
# 总体: O(n + m log m)

# 空间复杂度：O(m)，存储Counter和结果列表
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         c_n = Counter(nums)
#         threshold = sorted(list(c_n.values()), reverse=True)[k - 1]
#         return [x for x in c_n if c_n[x] >= threshold]

# 用堆
# from collections import Counter
# import heapq
#
# # 时间复杂度: O(n + n log k)，其中n是数组长度
# # 空间复杂度: O(n)
# # 优点: 适用于大数据集且k较小的情况，不需要对所有频率排序
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         # O(n)
#         count = Counter(nums)
#         # O(n log k)
#         return heapq.nlargest(k, count.keys(), key=count.get)

# (最优解)桶排序
# 时间复杂度: O(n)
#
# 统计频率: O(n)
# 创建桶数组: O(n)
# 将元素放入桶中: O(n)
# 收集结果: 最坏情况O(n)，但通常会提前返回
# 总体: O(n)
#
# 空间复杂度: O(n)
#
# count_map: 最坏情况下存储n个不同的元素，O(n)
# buckets数组: O(n)
# 总体: O(n)
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 步骤1: 统计每个元素的频率
        count_map = Counter(nums)

        # 步骤2: 创建桶数组，每个桶存储相同频率的元素
        # 频率范围是1到n，因此创建n+1个桶(索引0不使用)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        # 步骤3: 将元素放入对应频率的桶中
        for num, freq in count_map.items():
            buckets[freq].append(num)

        # 步骤4: 从高频到低频收集元素
        result = []
        for freq in range(n, 0, -1):  # 从n到1倒序遍历
            result.extend(buckets[freq])
            if len(result) >= k:
                return result[:k]

        return result  # 正常情况下不会执行到这一步


# 还有一种快速选择解法，平均时间复杂度O(n)，缺点：实现复杂，最坏情况下退化为O(n²)

test_cases = [
    {
        "method": "topKFrequent",
        "nums": [1, 1, 1, 2, 2, 3],
        "k": 2,
        "expected": [1, 2],
        "case_id": 1
    },
    {
        "method": "topKFrequent",
        "nums": [1],
        "k": 1,
        "expected": [1],
        "case_id": 2
    },
    {
        "method": "topKFrequent",
        "nums": [4, 1, -1, 2, -1, 2, 3],
        "k": 2,
        "expected": [-1, 2],
        "case_id": 3
    },
    {
        "method": "topKFrequent",
        "nums": [3, 3, 3, 3, 2, 2, 1, 5, 5, 5, 5, 5, 5, 5],
        "k": 3,
        "expected": [5, 3, 2],
        "case_id": 4
    },
    {
        "method": "topKFrequent",
        "nums": [-5, -5, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3],
        "k": 3,
        "expected": [3, 2, 1],
        "case_id": 5
    }
]
run_tests()
