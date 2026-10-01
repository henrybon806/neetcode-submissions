class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = {}
        target = Counter(s1)

        for right in range(len(s2)):
            curr = s2[right]
            freq[curr] = freq.get(curr, 0) + 1

            if freq == target:
                return True
            
            while right-left+1 >= len(s1):
                freq[s2[left]] -= 1
                if freq[s2[left]] == 0:
                    del freq[s2[left]]
                left += 1
        
        return freq == target