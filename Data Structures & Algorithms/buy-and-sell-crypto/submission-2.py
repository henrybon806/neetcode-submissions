class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = []
        cmax = -float('inf')
        for i in range(len(prices)):
            if not seen:
                seen.append(prices[i])
            else:
                curr = prices[i] - min(seen)
                if curr > cmax:
                    cmax = curr
                seen.append(prices[i])
        return max(cmax, 0)
            