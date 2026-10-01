class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {}
        def recurse(s):
            if s in wordDict or (s in memory and memory[s] == True):
                return True
            words = []
            for word in wordDict:
                if word in s:
                    words.append(word)
            poss = False
            for word in words:
                if s.index(word) == 0:
                    if s[s.index(word) + len(word):] not in memory:
                        memory[s[s.index(word) + len(word):]] = recurse(s[s.index(word) + len(word):])
                    poss = poss or memory[s[s.index(word) + len(word):]]
            return poss
        return recurse(s)