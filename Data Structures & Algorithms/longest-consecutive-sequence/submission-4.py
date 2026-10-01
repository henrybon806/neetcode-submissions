class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        best = 0
        for num in nums1:
            if num - 1 not in nums1:
                length = 1
                while num + length in nums1:
                    length += 1
                best = max(best, length)
        return best
