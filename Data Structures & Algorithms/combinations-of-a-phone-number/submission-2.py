class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.output = []
        self.numDict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        def backtrack(index, path):
            if index == len(digits):
                if len(path) > 0:
                    self.output.append(path)
                return
            poss = self.numDict[int(digits[index])]
            for i in range(len(poss)):
                path += poss[i]
                backtrack(index+1,path)
                path = path[:-1]
        backtrack(0,"")
        return self.output
