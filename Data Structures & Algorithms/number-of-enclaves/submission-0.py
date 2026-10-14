class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.visited = set()

        def bfs(i,j):
            queue = deque([[i,j]])
            while queue:
                size = len(queue)
                for _ in range(size):
                    i,j = queue.popleft()
                    grid[i][j] = 2
                    for x, y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                        if x>= 0 and y>= 0 and x<len(grid) and y < len(grid[0]) and (x,y) not in self.visited:
                            if grid[x][y] == 1:
                                self.visited.add((x,y))
                                queue.append([x,y])

        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                    if grid[i][j] == 1:
                        self.visited.add((i,j))
                        bfs(i,j)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
        
        return count
        
