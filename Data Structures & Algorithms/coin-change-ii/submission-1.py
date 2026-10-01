class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        memory = {}
        def recurse(amount, coin):
            if coin >= len(coins):
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if (amount, coin) in memory:
                return memory[(amount, coin)]
            memory[(amount, coin)] = recurse(amount-coins[coin], coin) + recurse(amount, coin+1)
            return memory[(amount, coin)]
        return recurse(amount, 0)