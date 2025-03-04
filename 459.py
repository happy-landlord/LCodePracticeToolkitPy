# 459.py
from test.test_suite import run_tests


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # 从 s[1] 开始找与 s[0] 相同的字符
        for i in range(1, n // 2 + 1):
            if s[i] == s[0]:
                l = i  # 可能的子字符串长度
                if n % l != 0:  # 快速排除
                    continue

                # 验证每个位置
                is_valid = True
                for j in range(l):  # 检查 s[j] 在每隔 l 的位置上是否相等
                    for k in range(l + j, n, l):  # 从 s[j+l] 开始，步长为 l
                        if s[j] != s[k]:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                if is_valid:
                    return True
        return False


test_cases = [
    {
        "method": "repeatedSubstringPattern",
        "s": "abab",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "aba",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "abcabcabcabc",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "a",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "aaaaaa",
        "expected": True,
        "case_id": 5
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "abababa",
        "expected": False,
        "case_id": 6
    },
    {
        "method": "repeatedSubstringPattern",
        "s": "abcdefabcdef",
        "expected": True,
        "case_id": 7
    }
]
run_tests()
