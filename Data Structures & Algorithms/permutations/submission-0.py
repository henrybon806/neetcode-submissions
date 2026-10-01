class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        def backtrack(index, path):
            if index == len(nums):
                if len(path) == len(nums):
                    self.output.append(path[:])
                return 
            for x in nums:
                if x in path:
                    continue
                
                path.append(x)
                backtrack(index+1, path)
                path.pop()

                backtrack(index+1,path)

        backtrack(0,[])
        return self.output