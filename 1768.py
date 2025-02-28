from test.test_suite import run_tests


class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     result = ''
    #     l = min(len(word1), len(word2))
    #
    #     for i in range(l):
    #         print(f"l:{l},i:{i}")
    #         result += word1[i]
    #         result += word2[i]
    #     result += (word1[l:])
    #     result += (word2[l:])
    #     return result

    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        return ''.join([word1[i] + word2[i] for i in range(l)]) + word1[l:] + word2[l:]
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     l1 = list(word1)
    #     l2 = list(word2)
    #     result = []
    #     r = min(len(l1), len(l2))
    #     print("r:", {r})
    #     while l1 and l2:
    #         result.append(l1.pop(0))
    #         result.append(l2.pop(0))
    #     print(f"l1:{l1}")
    #     print(f"l2:{l2}")
    #     result.extend((l2 if l2 else l1))
    #     print(result)
    #     return ''.join(result)


test_cases = [
    {
        "method": "mergeAlternately",
        "word1": "abc",
        "word2": "pqr",
        "expected": "apbqcr",
        "case_id": 1
    },
    {
        "method": "mergeAlternately",
        "word1": "ab",
        "word2": "pqrs",
        "expected": "apbqrs",
        "case_id": 2
    },
    {
        "method": "mergeAlternately",
        "word1": "abcd",
        "word2": "pq",
        "expected": "apbqcd",
        "case_id": 3
    }
]

run_tests()
