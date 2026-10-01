class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        nums.sort()
        def backtrack(index, path):
            if path[:] not in self.output:
                self.output.append(path[:])
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return self.output