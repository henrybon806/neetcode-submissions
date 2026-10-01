class Solution:
    def rob(self, nums: List[int]) -> int:
        
        self.memory = {}
        def explore(idx,nums, prod):
            if (idx, tuple(nums), prod) in self.memory:
                return self.memory[(idx, tuple(nums), prod)]
            if idx >= len(nums):
                return prod
            
            curr = 0
            curr = max(explore(idx+2,nums,prod+nums[idx]), explore(idx+1,nums,prod))
            self.memory[(idx, tuple(nums), prod)] = curr
            return curr
        
        return explore(0,nums,0)