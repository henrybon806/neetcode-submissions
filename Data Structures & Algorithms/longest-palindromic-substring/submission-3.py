class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        left = 0
        right = 1
        dp = []
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            dp.append(s[left+1:right])
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            dp.append(s[left+1:right])

        return max(dp, key=len)