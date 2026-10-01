class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memory = {}
        def recurse(idx1,idx2,idx3):
            if (idx1,idx2,idx3) in memory:
                return memory[(idx1,idx2,idx3)]
            if idx1 == len(s1) and idx2 == len(s2) and idx3 == len(s3):
                return True
            if idx3 == len(s3) or (idx1 == len(s1) and idx2 == len(s2)):
                return False
            if idx2 == len(s2):
                return s1[idx1:] == s3[idx3:]
            elif idx1 == len(s1):
                return s2[idx2:] == s3[idx3:]

            if s1[idx1] == s3[idx3] and s2[idx2] == s3[idx3]:
                memory[(idx1,idx2,idx3)] = recurse(idx1+1, idx2, idx3+1) or recurse(idx1, idx2+1, idx3+1)
            elif s1[idx1] == s3[idx3]:
                memory[(idx1,idx2,idx3)] = recurse(idx1+1, idx2, idx3+1)
            elif s2[idx2] == s3[idx3]:
                memory[(idx1,idx2,idx3)] = recurse(idx1, idx2+1, idx3+1)
            else:
                memory[(idx1,idx2,idx3)] = False
            return memory[(idx1,idx2,idx3)]

        return recurse(0,0,0)