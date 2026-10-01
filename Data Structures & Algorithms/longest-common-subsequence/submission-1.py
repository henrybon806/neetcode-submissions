class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        memory = {}
        def recurse(text1, text2):
            if (text1, text2) in memory:
                return memory[(text1, text2)]
            if text1 == text2:
                return len(text1)
            if len(text1) == 1:
                return 1 if text1 in text2 else 0
            elif len(text2) == 1:
                return 1 if text2 in text1 else 0
            if text1[0] == text2[0]:
                memory[(text1, text2)] = recurse(text1[1:], text2[1:]) + 1
            else:
                memory[(text1, text2)] = max(recurse(text1[1:], text2), recurse(text1, text2[1:]))
            return memory[(text1, text2)]
        return recurse(text1, text2)