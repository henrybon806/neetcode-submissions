class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxv = -1
        prev = prices[0]

        for price in prices:
            maxv = max(maxv, price - prev)
            prev = min(prev, price)
        return maxv