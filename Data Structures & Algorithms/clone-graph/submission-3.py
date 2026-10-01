"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = []
        self.copies = {}

        def explore(node, copy):
            if node is None:
                return
            if node in self.visited:
                return self.copies[node]
            self.visited.append(node)
            self.copies[node] = copy
            copy.val = node.val
            
            neighbors = []
            for newnode in node.neighbors:
                neighbors.append(explore(newnode, Node()))
            copy.neighbors = neighbors
            return copy
        
        return explore(node, Node())
