class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):
            total = 0
            for child in adj[node]:
                if child == parent:
                    continue
                cost = dfs(child, node)
                if cost > 0 or hasApple[child]:
                    total += cost + 2

            return total

        return dfs(0, -1)
