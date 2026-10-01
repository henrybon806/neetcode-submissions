class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        idx = 2
        while idx < len(cost):
            dp[idx] = min(dp[idx-1] + cost[idx], dp[idx-2] + cost[idx])
            idx+=1
        dp[idx] = min(dp[idx - 1], dp[idx-2])
        return dp[-1]