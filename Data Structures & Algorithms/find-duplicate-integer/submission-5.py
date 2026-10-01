class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        while True:
            temp = nums[nums[0]]
            if temp == nums[0]:
                return nums[0]
            nums[nums[0]] = nums[0]
            nums[0] = temp
        return nums[0]
