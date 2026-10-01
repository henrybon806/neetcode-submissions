class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[0] = 1
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            idx = i - 1
            while idx >= 0:
                if nums[i] > nums[idx]:
                    dp[i] = max(dp[idx] + 1, dp[i])
                idx -= 1
            if idx >= 0:
                dp[i] = max(dp[idx] + 1, dp[i])
            # if idx < 0:
            #     dp[i] = 1
        print(dp)
        return max(dp)