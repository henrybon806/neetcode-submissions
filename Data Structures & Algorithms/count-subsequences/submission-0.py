class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memory = {}
        def recurse(s, t):
            if (s,t) in memory:
                return memory[(s,t)]
            
            if len(t) == 0:
                return 1
            elif len(s) == 0 and len(t) != 0:
                return 0
                
            if s[0] == t[0]:
                memory[(s,t)] = recurse(s[1:],t[1:]) + recurse(s[1:], t)
            else:
                memory[(s,t)] = recurse(s[1:], t)
            return memory[(s,t)]
        return recurse(s,t)
