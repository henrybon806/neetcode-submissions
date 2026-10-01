class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memory = {}
        def recurse(r, c):
            if (r, c) in memory:
                return memory[(r,c)]
            position = [(r-1, c), (r,c-1), (r+1, c), (r,c+1)]
            passes = []
            for pos in position:
                if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(matrix) and pos[1] < len(matrix[0]):
                    if matrix[pos[0]][pos[1]] > matrix[r][c]:
                        passes.append(recurse(pos[0], pos[1]) + 1)
            if len(passes) > 0:
                memory[(r,c)] = max(passes)
            else:
                memory[(r,c)] = 0
            return memory[(r,c)]
        output = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output.append(recurse(i,j))
        return max(output) + 1
            
            