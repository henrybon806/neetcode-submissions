class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxv = 0

        def explore(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + explore(i-1, j) + explore(i, j-1) + explore(i+1, j) + explore(i, j+1)

    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxv = max(maxv, explore(i, j))
        return maxv