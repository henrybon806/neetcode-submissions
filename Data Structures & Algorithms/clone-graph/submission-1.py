"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        visited = {}

        def explore(node):
            if node is None:
                return None
            if node in visited:
                return visited[node]
            neighbor = []
            new = Node()
            new.val = node.val
            visited[node] = new
            for nod in node.neighbors:
                neighbor.append(explore(nod))
            new.neighbors = neighbor
            return new
    
        main = Node()
        main.val = node.val
        visited[node] = main
        neighbor = []
        for nod in node.neighbors:
            neighbor.append(explore(nod))
        main.neighbors = neighbor
        return main