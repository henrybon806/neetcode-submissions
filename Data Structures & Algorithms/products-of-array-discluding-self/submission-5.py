class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i, num in enumerate(nums):
            if i > 0:
                left[i] = left[i-1] * nums[i-1]
        # nums.reverse()
        right = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if i < len(nums)-1:
                right[i] = right[i+1] * nums[i+1]
                left[i] = left[i] * right[i]
        # for i in range(len(nums)):
        #     left[i] = left[i] * right[i]
        return left