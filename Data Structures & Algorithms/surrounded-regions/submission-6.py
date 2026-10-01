class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.parents = list(range(len(board)*len(board[0])+1))
        self.size = [1] * (len(board)*len(board[0])+1)

        n = len(board) * len(board[0])
        for i in range(len(board)):
            self.parents[i * len(board[0])] = n                     
            self.parents[i * len(board[0]) + len(board[0]) - 1] = n
        for j in range(len(board[0])):
            self.parents[j] = n                                  
            self.parents[(len(board)-1) * len(board[0]) + j] = n 

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
                    for pos in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if not (0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0])):
                            continue 
                        if board[pos[0]][pos[1]] == 'O':
                            union(i*len(board[0])+j,pos[0]*len(board[0])+pos[1])
        border = find(n)
        for i in range(len(board)):
            for j in range(len(board[0])):
                par = find(i*len(board[0])+j)
                if board[i][j] == 'O' and par != border:
                    board[i][j] = 'X'
                    
