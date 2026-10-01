class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num in seen:
                continue
            else:
                seen.append(num)
        nums[:] = seen
        return len(seen)