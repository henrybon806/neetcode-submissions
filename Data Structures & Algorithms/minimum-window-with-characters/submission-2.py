class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        window = {}
        minTarget = Counter(t)
        count = 0
        need = len(minTarget)
        best = None

        for i in range(len(s)):
            curr = s[i]
            if curr in t:
                window[curr] = window.get(curr, 0) + 1
                if window[curr] == minTarget[curr]:
                    count += 1

            while count == need:
                if best is None or i-left+1 < len(best):
                    best = s[left:i+1]
                
                leftc = s[left]
                if leftc in minTarget:
                    window[leftc] -= 1
                    if window[leftc] < minTarget[leftc]:
                        count -= 1
                left += 1
        
        return best or ""
            
