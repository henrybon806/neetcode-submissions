class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        nums.sort()

        def backtrack(idx, path, indices):
            if len(path) == len(nums):
                self.permutations.append(path[:])
                return

            if idx >= len(nums):
                return

            for i in range(len(nums)):
                if i in indices:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in indices:
                    continue
                indices.add(i)
                path.append(nums[i])
                backtrack(idx+1, path, indices)
                path.pop()
                indices.remove(i)
        
        backtrack(0, [], set())
        return self.permutations