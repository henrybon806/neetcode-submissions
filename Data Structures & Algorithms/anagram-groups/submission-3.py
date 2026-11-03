class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        for word in strs:
            poss = str(sorted(word))
            if poss in storage:
                storage[poss].append(word)
            else:
                storage[poss] = [word]
        res = []
        for cal in storage:
            res.append(storage[cal])
        return res