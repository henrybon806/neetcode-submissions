class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        maxfreq = 0
        best = 0

        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1
            maxfreq = max(maxfreq, window[curr])

            while right-left+1 - maxfreq > k:
                window[s[left]] -= 1
                left += 1
            best = max(best, right-left+1)
        
        return best