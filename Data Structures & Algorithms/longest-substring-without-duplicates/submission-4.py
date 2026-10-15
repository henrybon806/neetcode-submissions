class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0
        for r in range(len(s)):
            while s[r] in seen and l <= r:
                seen.discard(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r-l+1)
        return best