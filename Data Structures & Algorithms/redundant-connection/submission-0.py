class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = list(range(max(max(edge) for edge in edges)+1))
        self.size = [1] * len(self.parents)

        def find(i):
            if i == self.parents[i]:
                return i
            self.parents[i] = find(self.parents[i])
            return self.parents[i]
        
        def union(a,b):
            a = find(a)
            b = find(b)
            if self.size[a] < self.size[b]:
                self.parents[a] = b
                self.size[b] += self.size[a]
            else:
                self.parents[b] = a
                self.size[a] += self.size[b]
            
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            union(edge[0], edge[1])
        return None