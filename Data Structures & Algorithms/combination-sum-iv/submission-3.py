class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.output = 0
        self.memory = {}

        def recurse(targ):
            if targ in self.memory:
                return self.memory[targ]
            if targ == 0:
                return 1
            elif targ < 0:
                return 0 
            total = 0
            for num in nums:
                total += recurse(targ-num)
            self.memory[targ] = total
            return total
        
        return recurse(target)