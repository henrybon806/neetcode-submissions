class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(index, prev, path):
            if path == list(word):
                return True
            if len(path) > len(word) or index in prev:
                return False
            if index[0] < 0 or index[1] < 0 or index[0] >= len(board) or index[1] >= len(board[0]):
                return False
            if board[index[0]][index[1]] != word[len(path)]:
                return False

            poss = False
            path.append(board[index[0]][index[1]])
            prev.append(index)
            for pos in [(index[0]-1, index[1]), (index[0], index[1]-1), (index[0]+1, index[1]), (index[0], index[1]+1)]:
                if pos not in prev:
                    poss = poss or backtrack(pos, prev, path)
            prev.pop()
            path.pop()
            return poss
        
        poss = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                poss = backtrack((i,j), [], []) or poss
        return poss