class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        total = 0
        cur_max = cur_min = 0
        best_max = nums[0]
        best_min = nums[0]

        for i in range(len(nums)):
            total += nums[i]
            cur_max = max(cur_max+nums[i],nums[i])
            cur_min = min(cur_min+nums[i],nums[i])
            best_max=max(best_max,cur_max)
            best_min=min(best_min,cur_min)
        if best_max<0:
            return best_max
        return max(best_max, total - best_min)
