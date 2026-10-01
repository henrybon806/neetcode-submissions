class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memory = {}
        def recurse(nums, idx):
            if nums == None:
                return 0
            if (tuple(nums), idx) in memory:
                return memory[(tuple(nums), idx)]
            if len(nums) == 1:
                return nums[0]
            if idx >= len(nums):
                return 0
            left = nums[idx-1] if idx-1>=0 else 1
            right = nums[idx+1] if idx+1<len(nums) else 1
            memory[(tuple(nums), idx)] = max(left*nums[idx]*right + recurse(nums[:idx] + (nums[idx+1:]), 0), recurse(nums, idx+1))
            return memory[(tuple(nums), idx)]
        return recurse(nums, 0)
