class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cursum = numbers[0] + numbers[-1]
        left = 0
        right = len(numbers)-1
        while left < right:
            if cursum == target:
                return [left+1, right+1]
            if cursum > target:
                cursum -= numbers[right]
                right -= 1
                cursum += numbers[right]
            else:
                cursum -= numbers[left]
                left += 1
                cursum += numbers[left]
        return []