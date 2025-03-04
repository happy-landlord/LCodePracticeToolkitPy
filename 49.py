# 49.py
from collections import Counter, defaultdict
from pprint import pprint

from test.test_suite import run_tests


# 49. Group Anagrams

# Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.
#
# An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# ### Constraints:
# - `1 <= strs.length <= 10^4`
# - `0 <= strs[i].length <= 100`
# - `strs[i]` consists of lowercase English letters.
#
# ### Examples:
#
# #### Example 1:
# **Input:** strs = ["eat","tea","tan","ate","nat","bat"]
# **Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# #### Example 2:
# **Input:** strs = [""]
# **Output:** [[""]]
#
# #### Example 3:
# **Input:** strs = ["a"]
# **Output:** [["a"]]
#
# ---

class Solution:
    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # coded = {}
    # for i, s in enumerate(strs):
    #     c_s = Counter(s)
    #     key = ''
    #     for k in sorted(c_s):
    #         key += (str(k) + str(c_s[k]))
    #
    #     if key in coded:
    #         coded[key].append(i)
    #     else:
    #         coded[key] = [i]
    #
    # pprint(coded)
    # result = []
    #
    # for group in coded:
    #     print(coded[group])
    #     print([strs[v] for v in coded[group]])
    #     result.append([strs[v] for v in coded[group]])
    # return result

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            sorted_key = tuple(sorted(word))  # 作为哈希键
            hashmap[sorted_key].append(word)

        return list(hashmap.values())


test_cases = [
    {
        "method": "groupAnagrams",
        "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        "case_id": 1
    },
    {
        "method": "groupAnagrams",
        "strs": [""],
        "expected": [[""]],
        "case_id": 2
    },
    {
        "method": "groupAnagrams",
        "strs": ["a"],
        "expected": [["a"]],
        "case_id": 3
    },
    {
        "method": "groupAnagrams",
        "strs": ["abc", "bca", "cab", "xyz", "zyx", "yxz", "qwe"],
        "expected": [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"], ["qwe"]],
        "case_id": 4
    },
    {
        "method": "groupAnagrams",
        "strs": ["aaa", "bbb", "ccc", "aaa", "abc", "bac", "cab"],
        "expected": [["aaa", "aaa"], ["bbb"], ["ccc"], ["abc", "bac", "cab"]],
        "case_id": 5
    }
]

run_tests()
