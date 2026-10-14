class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        curr = 1
        for r in range(len(nums)):
            curr *= nums[r]
            while curr >= k and l <= r:
                curr /= nums[l]
                l+=1
            if curr < k:
                count += r-l+1
        return count