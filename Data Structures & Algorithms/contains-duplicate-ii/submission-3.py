class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()

        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            if len(seen) > k:
                seen.remove(nums[r - k])
        
        return False