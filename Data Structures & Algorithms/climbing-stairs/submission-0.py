class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def recurse(n):
            if n in memory:
                return memory[n]
            if n <= 2:
                return n
            memory[n] = recurse(n-1) + recurse(n-2)
            return memory[n]
        return recurse(n)