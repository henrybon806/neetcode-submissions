class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.choices = ['(', ')']

        def backtrack(index, path, openv, closev):
            if len(path) == 2*n and path not in self.output:
                if path not in self.output and openv == closev:
                    self.output.append(path)
                return

            if closev < openv:
                path += ')'
                backtrack(index+1,path,openv, closev+1)
                path = path[:-1]

            path += '('
            backtrack(index+1,path, openv+1, closev)
            path = path[:-1]

        backtrack(0,"",0,0)
        return self.output