class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.parents = {(i,j):(i,j) for i in range(len(board)) for j in range(len(board[0]))}
        self.parents[(-1,-1)] = (-1,-1)
        self.size = {(i,j):1 for i in range(len(board)) for j in range(len(board[0]))}
        self.size[(-1,-1)] = 1

        for i in range(len(board)):
            self.parents[(i,0)] = (-1,-1)
            self.parents[(i,len(board[0])-1)] = (-1,-1)
            self.size[(-1,-1)] += 1
        for i in range(len(board[0])):
            self.parents[(0,i)] = (-1,-1)
            self.parents[(len(board)-1,i)] = (-1,-1)
            self.size[(-1,-1)] += 1

        def find(i):
            if self.parents[i] == i:
                return i
            self.parents[i] = find(self.parents[i])
            return self.parents[i]
        
        def union(a,b):
            one = find(a)
            two = find(b)
            if one == two: 
                return
            if self.size[one] < self.size[two]:
                self.parents[one] = self.parents[two]
                self.size[two] += self.size[one]
            else:
                self.parents[two] = self.parents[one]
                self.size[one] += self.size[two]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    for pos in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[0]):
                            continue 
                        if board[pos[0]][pos[1]] == 'O':
                            union((i,j),pos)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                par = find((i,j))
                if board[i][j] == 'O' and par != (-1,-1):
                    board[i][j] = 'X'
                    
