class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memory = {}
        def recurse(word1,word2):
            if (word1, word2) in memory:
                return memory[(word1,word2)]
            if word1 == word2:
                return 0
            if len(word1) == 0:
                return len(word2)
            elif len(word2) == 0:
                return len(word1)
            if word1[0] == word2[0]:
                memory[(word1,word2)] = recurse(word1[1:], word2[1:])
            else:
                memory[(word1,word2)] = 1 + min(recurse(word1[1:], word2), recurse(word1, word2[1:]), recurse(word1[1:], word2[1:]))
            return memory[(word1,word2)]
        return recurse(word1, word2)