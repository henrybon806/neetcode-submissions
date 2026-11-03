class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        for word in strs:
            poss = sorted(word)
            curr = Counter(poss)
            if str(curr) in storage:
                storage[str(curr)].append(word)
            else:
                storage[str(curr)] = [word]
        res = []
        for cal in storage:
            res.append(storage[cal])
        return res