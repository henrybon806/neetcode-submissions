class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        def backtrack(index, path):
            if index == len(nums):
                if len(path) == len(nums):
                    self.output.append(path[:])
                return 
            for x in range(len(nums)):
                if nums[x] in path:
                    continue
                
                path.append(nums[x])
                backtrack(index+1, path)
                path.pop()

                backtrack(index+1,path)

        backtrack(0,[])
        return self.output