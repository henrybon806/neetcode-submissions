class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != int(target):
            return False
        memory = {}
        def recurse(curr, n):
            if (curr, tuple(n)) in memory:
                return memory[(curr, tuple(n))]
            if curr > target:
                return False
            elif curr == target:
                return True
            if len(n) == 0:
                return False
            memory[(curr, tuple(n))] = recurse(curr, n[1:]) or recurse(curr + n[0], n[1:])
            return memory[(curr, tuple(n))]
        return recurse(0, nums)