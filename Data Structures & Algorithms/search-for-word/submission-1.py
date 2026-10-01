class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        def backtrack(r,c,k):
            if (r,c) in visited:
                return
            if k == len(word):
                return True
            if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != word[k]:
                return False
            
            visited.append((r,c))
            found = backtrack(r-1,c,k+1) or backtrack(r,c-1,k+1) or backtrack(r+1,c,k+1) or backtrack(r,c+1,k+1)
            visited.pop()
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
