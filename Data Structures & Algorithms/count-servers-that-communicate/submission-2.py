class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for jj in range(cols):
                if grid[i][jj] == 1 and (i, jj) not in visited:
                    dfs(i, jj)
            for ii in range(rows):
                if grid[ii][j] == 1 and (ii, j) not in visited:
                    dfs(ii, j)

        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    component = []
                    stack = [(i, j)]
                    visited.add((i, j))
                    while stack:
                        ci, cj = stack.pop()
                        component.append((ci, cj))
                        for jj in range(cols):
                            if grid[ci][jj] == 1 and (ci, jj) not in visited:
                                visited.add((ci, jj))
                                stack.append((ci, jj))
                        for ii in range(rows):
                            if grid[ii][cj] == 1 and (ii, cj) not in visited:
                                visited.add((ii, cj))
                                stack.append((ii, cj))
                    if len(component) > 1:
                        total += len(component)

        return total