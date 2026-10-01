class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        best = 0
        maxfreq = 0

        for right in range(len(s)):
            curr = s[right]
            freq[curr] = freq.get(curr, 0) + 1
            maxfreq = max(maxfreq, freq[curr])
            
            while (right - left + 1) - maxfreq > k:
                # if s[left] == curr:
                freq[s[left]] -= 1
                    # if freq[s[left]] == 0:
                    #     del freq[s[left]]
                left += 1
            
            best = max(best, right-left+1)
        return best

            