class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = [-1] * (len(nums) - (k - 1))

        for l in range(len(nums) - (k - 1)):
            curr = nums[l]
            top = nums[l]
            canceled = False
            for j in range(l+1,l+k):
                if nums[j] != curr + 1:
                    canceled = True
                    break
                curr += 1
                top = max(top, nums[j])
            if not canceled:
                res[l] = top
        return res
            
