class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.output = []
        self.columns = set()
        self.diag = set()
        self.diagN = set()
        
        def backtrack(index, path, row):
            if index == n:
                self.output.append(path[:])
                return
            if row >= n:
                return
            i=row
            for j in range(n):
                if j not in self.columns and i-j not in self.diag and i+j not in self.diagN:
                    self.columns.add(j)
                    self.diagN.add(i+j)
                    self.diag.add(i-j)
                    
                    print(len(path), i)
                    path[i] = path[i][:j] + 'Q' + path[i][j+1:]
                    backtrack(index+1,path, i+1)
                    path[i] = "."*n

                    self.columns.remove(j)
                    self.diagN.remove(i+j)
                    self.diag.remove(i-j)
        
        board = ["." * n for _ in range(n)] 
        backtrack(0, board, 0)
        return self.output