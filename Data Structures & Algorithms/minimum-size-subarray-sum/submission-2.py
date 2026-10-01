class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cursum = 0
        best = 100001

        for right in range(len(nums)):
            curr = nums[right]
            cursum += curr

            # if cursum >= target:
            #     best = min(best, right-left+1)
            #     left+=1
            # print(cursum)
            while cursum >= target:
                best = min(best, right-left+1)
                cursum -= nums[left]
                left += 1
        
        return best if best < 100001 else 0