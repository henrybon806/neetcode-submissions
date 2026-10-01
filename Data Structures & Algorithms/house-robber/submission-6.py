class Solution:
    def rob(self, nums: List[int]) -> int:
        
        self.memory = {}
        def explore(idx):
            if idx >= len(nums):
                return 0
            if (idx) in self.memory:
                return self.memory[(idx)]
            
            curr = max(nums[idx] + explore(idx+2), explore(idx+1))
            self.memory[(idx)] = curr
            return curr
        
        return explore(0)