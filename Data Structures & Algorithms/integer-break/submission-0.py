class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


'''
dp[i] = the maximum product of some elements that sum to i
dp[0] = 0
dp[1] = 1 (1*1)
dp[2] = 2 (2*1)
dp[3] = 3 (3*1)
dp[4] = 4 (2*2)
dp[5] = 6 (3*2)
'''