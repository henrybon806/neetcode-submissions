"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodes = {}
        def clone_node(clone):
            nonlocal nodes
            if not clone or clone in nodes:
                return node
            copy = Node()
            copy.val = clone.val
            nodes[clone] = copy
            for neigh in clone.neighbors:
                clone_node(neigh)
        clone_node(node)
        head = node
        for node in nodes:
            res = []
            for neigh in node.neighbors:
                res.append(nodes[neigh])
            nodes[node].neighbors = res
        return nodes[head]

