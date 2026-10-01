class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxv = 0

        def explore(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            around = [(i-1,j), (i,j-1), (i,j+1), (i+1,j)]
            total = 0
            for pos in around:
                total += explore(pos[0], pos[1])
            return 1 + total 

    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxv = max(maxv, explore(i, j))
        return maxv