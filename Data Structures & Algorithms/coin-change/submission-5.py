class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 or amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        dp = [float('inf')] * (amount+1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(coins[0]+1, amount+1):
            for coin in coins:
                if coin < amount:
                    if i - coin > 0:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1