class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = []
        best = 0
        idx = 0
        while idx < len(prices):
            if len(seen) != 0:
                if best < prices[idx] - min(seen):
                    best = prices[idx] - min(seen)
            seen.append(prices[idx])
            idx +=1 
        return best
            