class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.visited = set()
        self.expected = set()

        def explore(i,j):
            if (i,j) in self.visited or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'X':
                return
            self.visited.add((i,j))
            for pos in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                explore(pos[0],pos[1])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1) and board[i][j] == 'O':
                    explore(i,j) 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in self.visited:
                    board[i][j] = 'X'