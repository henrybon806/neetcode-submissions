class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        maxlen = 0
        window = set()

        for right in range(len(s)):
            curr = s[right]

            while s[right] in window:
                window.discard(s[left])
                left+=1
            
            window.add(curr)

            maxlen = max(maxlen, right-left)
        return maxlen + 1