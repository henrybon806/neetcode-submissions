class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newstr = ""
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            elif s[left].isalnum(): 
                right -= 1
            elif s[right].isalnum(): 
                left += 1
            else:
                left += 1
                right -= 1
        return True