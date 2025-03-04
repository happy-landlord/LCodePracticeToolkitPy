# 125.py
from test.test_suite import run_tests


# 125. Valid Palindrome
#
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#
# Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.
#
# ### Constraints:
# - `1 <= s.length <= 2 * 10^5`
# - `s` consists only of printable ASCII characters.
#
# ### Examples:
#
# #### Example 1:
# **Input:** s = "A man, a plan, a canal: Panama"
# **Output:** true
# **Explanation:** After removing non-alphanumeric characters and converting to lowercase, `"amanaplanacanalpanama"` is a palindrome.
#
# #### Example 2:
# **Input:** s = "race a car"
# **Output:** false
# **Explanation:** After removing non-alphanumeric characters and converting to lowercase, `"raceacar"` is not a palindrome.
#
# #### Example 3:
# **Input:** s = " "
# **Output:** true
# **Explanation:** After removing non-alphanumeric characters, `s` is an empty string `""`, which is considered a palindrome.
#
# #### Example 4:
# **Input:** s = "0P"
# **Output:** false
# **Explanation:** After removing non-alphanumeric characters, `"0p"` is not a palindrome since `'0'` and `'p'` are different.
#
# #### Example 5:
# **Input:** s = "ab@a"
# **Output:** true
# **Explanation:** After removing `@`, the remaining string `"aba"` is a palindrome.
#
# ---

# 这道题字母和数字都算，用isalnum()，不用isalpha()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if not (s[p1].isalnum()):
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1

        return True


test_cases = [
    {
        "method": "isPalindrome",
        "s": "A man, a plan, a canal: Panama",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isPalindrome",
        "s": "race a car",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "isPalindrome",
        "s": " ",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "isPalindrome",
        "s": "0P",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isPalindrome",
        "s": "ab@a",
        "expected": True,
        "case_id": 5
    }
]

run_tests()
