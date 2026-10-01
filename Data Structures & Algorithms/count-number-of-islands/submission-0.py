class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.islands = 0
        def explore(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == '0':
                return
            self.visited.add((i,j))
            poss = [(i-1,j), (i,j-1), (i+1,j),(i,j+1)]
            for pos in poss:
                if pos not in self.visited:
                    explore(pos[0], pos[1])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited:
                    if grid[i][j] == '1': 
                        self.islands += 1
                    # visited.add((i,j))
                    explore(i,j)
        return self.islands
