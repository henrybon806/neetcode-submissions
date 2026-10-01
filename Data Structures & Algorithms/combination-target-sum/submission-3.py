class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        def recurse(curr, targ, idx):
            if idx >= len(nums):
                return
            if targ - nums[idx] == 0:
                if curr+[nums[idx]] not in self.output:
                    self.output.append(curr+[nums[idx]])
            if targ - nums[idx] < 0:
                recurse(curr, targ, idx+1)
            else:
                recurse(curr, targ, idx+1)
                # recurse(curr+[nums[idx]], targ-nums[idx], idx+1)
                recurse(curr+[nums[idx]], targ-nums[idx], idx)
        recurse([], target, 0)
        return self.output