class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i,j):
            for u,v in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if u >=0 and v >= 0 and u < len(board) and v < len(board[0]) and board[u][v] == 'O':
                    board[u][v] = 'Z'
                    dfs(u,v)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1) or (j == 0 or j == len(board[0])-1):
                    if board[i][j] == 'O':
                        board[i][j] = 'Z'
                        dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'