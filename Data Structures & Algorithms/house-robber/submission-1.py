class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        idx = 1
        while idx < len(nums):
            if idx == 1:
                dp[1] = nums[1]
            elif idx == 2:
                dp[2] = dp[0] + nums[2]
            if idx > 2:
                dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 3] + nums[idx])
            idx += 1
        print(dp)
        return max(dp)