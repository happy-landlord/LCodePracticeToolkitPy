# # 242. Valid Anagram
#
# ## Problem Description
# Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
#
# An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# ## Constraints:
# - 1 <= s.length, t.length <= 5 * 10^4
# - `s` and `t` consist of lowercase English letters.
#
# ## Examples:
#
# **Example 1:**
# ```
# Input: s = "anagram", t = "nagaram"
# Output: true
# ```
#
# **Example 2:**
# ```
# Input: s = "rat", t = "car"
# Output: false
# ```

from collections import Counter

from test.test_suite import run_tests


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


test_cases = [
    {
        "method": "isAnagram",
        "s": "anagram",
        "t": "nagaram",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isAnagram",
        "s": "rat",
        "t": "car",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "isAnagram",
        "s": "a",
        "t": "a",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "isAnagram",
        "s": "ab",
        "t": "a",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isAnagram",
        "s": "listen",
        "t": "silent",
        "expected": True,
        "case_id": 5
    },
    {
        "method": "isAnagram",
        "s": "hello",
        "t": "hello",
        "expected": True,
        "case_id": 6
    },
    {
        "method": "isAnagram",
        "s": "aacc",
        "t": "ccac",
        "expected": False,
        "case_id": 7
    }
]

run_tests()
