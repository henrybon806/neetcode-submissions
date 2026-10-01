import sys; sys.setrecursionlimit(20000)

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        self.best = 100000
        self.options = []
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j+=1
        return dp[n]
        # for i in range()
        
        # self.counts = []
        # self.memory = {}
        # def recurse(n):
        #     if n == 0:
        #         return 0
        #     if n in self.memory:
        #         return self.memory[n]

        #     best = float('inf')
        #     for num in self.options:
        #         if num <= n:
        #             best = min(best, 1+recurse(n-num))
        #     self.memory[n] = best
        #     return best
            
        # return recurse(n)
