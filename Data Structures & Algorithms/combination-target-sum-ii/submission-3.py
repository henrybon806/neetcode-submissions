class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        candidates.sort()
        def recurse(curr, targ, idx):
            if targ == 0:
                self.output.append(curr)
                return 
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > targ:
                    break
                recurse(curr+[candidates[i]], targ-candidates[i], i+1)

        recurse([], target, 0)
        return self.output