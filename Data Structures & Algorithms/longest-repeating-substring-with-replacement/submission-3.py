class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        curr = {}
        best = 0

        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r], 0) + 1
            while (r-l+1) - max(curr.values()) > k:
                curr[s[l]] -= 1
                if curr[s[l]] == 0:
                    del curr[s[l]]
                l+=1
            best = max(best, r-l+1)
        return best