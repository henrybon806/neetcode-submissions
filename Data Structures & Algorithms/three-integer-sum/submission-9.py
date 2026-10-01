class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            left = i
            right = len(nums)-1
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                curr = nums[left] + nums[right] + nums[i]
                if curr == 0:
                    output.add((nums[left], nums[right], nums[i]))
                    right -= 1
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1

        return [[x[0],x[1],x[2]] for x in output]
