class Solution:
    def rob(self, nums: List[int]) -> int:
        
        self.memory = {}
        def explore(idx, prod):
            if (idx, prod) in self.memory:
                return self.memory[(idx, prod)]
            if idx >= len(nums):
                return prod
            
            curr = 0
            curr = max(explore(idx+2,prod+nums[idx]), explore(idx+1,prod))
            self.memory[(idx, prod)] = curr
            return curr
        
        return explore(0,0)