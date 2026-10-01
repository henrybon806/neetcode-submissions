class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def backtrack(start, csum):
            if start == len(nums):
                self.total += csum
                return
            
            # for i in range(start, len(nums)):
            csum ^= nums[start]
            backtrack(start+1, csum)
            csum ^= nums[start]
            backtrack(start+1, csum)

        backtrack(0, 0)
        return self.total