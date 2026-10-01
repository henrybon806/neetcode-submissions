class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robbery(nums):
            if len(nums) == 0:
                return 0
            dp = [0]*len(nums)
            dp[0] = nums[0]
            idx = 1
            while idx < len(nums):
                if idx == 1:
                    dp[idx] = max(nums[1], nums[0])
                elif idx == 2:
                    dp[idx] = max(dp[0]+nums[idx], dp[1])
                if idx > 2:
                    dp[idx] = max(dp[idx - 1], dp[idx-2]+nums[idx])
                idx += 1
            return dp[-1]
        return max(robbery(nums[1:]), robbery(nums[:-1]))