class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        memory = {}
        def backtrack(index, prev, path):
            if (index, tuple(prev), tuple(path)) in memory:
                return memory[(index, tuple(prev), tuple(path))]
            if path == list(word):
                return True
            if len(path) > len(word) or index in prev:
                return False
            if index[0] < 0 or index[1] < 0 or index[0] >= len(board) or index[1] >= len(board[0]):
                return False

            poss = False
            for i in range(len(path), len(word)):
                path.append(board[index[0]][index[1]])
                prev.append(index)
                for pos in [(index[0]-1, index[1]), (index[0], index[1]-1), (index[0]+1, index[1]), (index[0], index[1]+1)]:
                    if pos not in prev:
                        poss = poss or backtrack(pos, prev, path)
                prev.pop()
                path.pop()
            memory[(index, tuple(prev), tuple(path))] = poss
            return poss
        
        poss = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                poss = backtrack((i,j), [], []) or poss
        return poss