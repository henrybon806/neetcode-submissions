class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        memory = {}
        def recurse(day, hold):
            if (day, hold) in memory:
                return memory[(day, hold)]
            if day >= len(prices):
                return 0
            if hold:
                memory[(day, hold)] = max(recurse(day+1, hold), recurse(day+2,not hold) + prices[day])
            else:
                memory[(day, hold)] = max(recurse(day+1, hold), recurse(day+1, not hold) - prices[day])
            return memory[(day, hold)]
        return recurse(0, 0)