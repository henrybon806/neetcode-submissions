class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.queue = []
        self.visited = set()
        self.days = -1

        def explore():
            while self.queue:
                size = len(self.queue)
                print(grid)
                for i in range(size):
                    curr = self.queue.pop(0)
                    for pos in [(curr[0]-1, curr[1]),(curr[0], curr[1]-1),(curr[0], curr[1]+1),(curr[0]+1, curr[1])]:
                        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid) and pos[1]< len(grid[0]) and pos not in self.visited:
                            if grid[pos[0]][pos[1]] == 1:
                                grid[pos[0]][pos[1]] = 2
                                self.queue.append(pos)
                                self.visited.add(pos)

                self.days += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.queue.append((i,j))
        explore()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(self.days, 0)