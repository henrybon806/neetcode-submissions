class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memory = {}
        def recurse(s1,s2,s3):
            if (s1,s2,s3) in memory:
                return memory[(s1,s2,s3)]
            if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
                return True
            if len(s3) == 0:
                return False
            if len(s1) == 0:
                return s2 == s3
            elif len(s2) == 0:
                return s1 == s3
            if (len(s1) == 0 and len(s2) == 0) and len(s3) != 0:
                return False
            if s1[0] == s3[0] and s2[0] == s3[0]:
                memory[(s1,s2,s3)] = recurse(s1[1:], s2, s3[1:]) or recurse(s1, s2[1:], s3[1:])
            elif s1[0] == s3[0]:
                memory[(s1,s2,s3)] = recurse(s1[1:], s2, s3[1:])
            elif s2[0] == s3[0]:
                memory[(s1,s2,s3)] = recurse(s1, s2[1:], s3[1:])
            else:
                memory[(s1,s2,s3)] = False
            return memory[(s1,s2,s3)]
        return recurse(s1,s2,s3)