class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        currmax = nums[0]
        currmin = nums[0]
        best = 0
        if len(nums) == 1:
            return nums[0]
        for i, num in enumerate(nums[1:]):
            # dp[i] = max(num, num*currmin, num*currmax)
            temp = currmin
            currmin = min(num, num*currmin, num*currmax)
            currmax = max(num, num*temp, num*currmax)
            best = max(best, currmax)
            # print(currmin, currmax, best)
        return max(best, max(nums))