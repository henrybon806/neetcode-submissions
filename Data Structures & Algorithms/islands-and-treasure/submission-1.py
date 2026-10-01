class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.visited = set()
        self.queue = []
        self.new = []

        def explore():
            layer = 0
            while self.queue:
                size = len(self.queue)
                self.new = []
                for i in range(size):
                    curr = self.queue.pop(0)
                    if grid[curr[0]][curr[1]] != -1:
                        if grid[curr[0]][curr[1]] != 0:
                            grid[curr[0]][curr[1]] = min(grid[curr[0]][curr[1]], layer)
                        for pos in [(curr[0]-1,curr[1]), (curr[0],curr[1]-1), (curr[0],curr[1]+1), (curr[0]+1,curr[1])]:
                            if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid) and pos[1] < len(grid[0]) and pos not in self.visited:
                                self.visited.add(pos)
                                self.new.append(pos)
                self.queue.extend(self.new)
                layer += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.queue.append((i,j))
        explore()