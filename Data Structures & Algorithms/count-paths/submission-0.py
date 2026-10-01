class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        memory = {}
        def recurse(m, n):
            if (m, n) in memory:
                return memory[(m, n)]
            if m == 1 or n == 1:
                return 1
            memory[(m, n)] = recurse(m-1, n) + recurse(m, n-1)
            return memory[(m, n)]
        return recurse(m, n) 