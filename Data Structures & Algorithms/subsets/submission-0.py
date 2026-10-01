class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        def recurse(curr, idx):
            if idx >= len(nums):
                self.output.append(curr)
                return
            recurse(curr+[nums[idx]], idx+1)
            recurse(curr, idx+1)
        recurse([], 0)
        return self.output