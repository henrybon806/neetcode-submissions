class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = {}
        def recurse(curr, num):
            if num >= len(nums):
                return 0
            if (curr, num) in memory:
                return memory[(curr, num)]
            if num == len(nums) - 1:
                if curr - nums[num] == 0 and curr + nums[num] == 0:
                    return 2
                elif curr - nums[num] == 0 or curr + nums[num] == 0:
                    return 1
            memory[(curr, num)] = recurse(curr-nums[num], num+1) + recurse(curr+nums[num], num+1)
            return memory[(curr, num)]
        return recurse(target, 0)