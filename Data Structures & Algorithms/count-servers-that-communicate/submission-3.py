class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rowCount = [0] * rows
        colCount = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                    total += 1

        return total