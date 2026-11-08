class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        myset = set(nums)
        best = 1
        for i in range(len(nums)):
            if nums[i]-1 not in myset:
                j = nums[i] + 1
                curr = 1
                while j in myset:
                    curr += 1
                    j += 1
                best = max(best, curr)
        return best