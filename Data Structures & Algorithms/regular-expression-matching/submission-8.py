class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        def recurse(s, pidx):
            if (s,pidx) in memory:
                return memory[(s,pidx)]
            if len(s)==0 and (len(p[pidx:]) == 2 and p[-1] == '*'):
                return True
            if (pidx >= len(p) or p[pidx] == '*') and len(s) == 0:
                return True
            elif pidx >= len(p) or len(s) == 0:
                return False
            if s == p[pidx:]:
                return True
            if p[pidx] == '.' or s[0] == p[pidx]:
                if pidx < len(p)-1 and p[pidx+1] == '*':
                    memory[(s,pidx)] =  recurse(s[1:], pidx) or recurse(s,pidx+2)
                else:
                    memory[(s,pidx)] = recurse(s[1:],pidx+1)
            else:
                if pidx < len(p)-1 and p[pidx+1] == '*':
                    memory[(s,pidx)] = recurse(s,pidx+2) 
                else:
                    memory[(s,pidx)] = False
            return memory[(s,pidx)]
        return recurse(s,0)
