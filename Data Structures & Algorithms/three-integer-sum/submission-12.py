class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            left = i+1
            right = len(nums)-1
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                curr = nums[left] + nums[right] + nums[i]
                if i > 0 and nums[i-1] == nums[i]:
                    left += 1
                    continue
                if curr == 0:
                    output.add((nums[left], nums[right], nums[i]))
                    right -= 1
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1

        return [list(x) for x in output]
