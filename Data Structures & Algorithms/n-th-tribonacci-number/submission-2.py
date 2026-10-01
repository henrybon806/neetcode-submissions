class Solution:
    def tribonacci(self, n: int) -> int:
        
        memory = {}
        def recurse(n):
            if n in memory:
                return memory[n]
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            memory[n] = recurse(n-1) + recurse(n-2) + recurse(n-3)
            return memory[n]
        return recurse(n)