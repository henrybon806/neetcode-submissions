class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.parents = list(range(n))
        self.size = [1] * n

        def find(i):
            if i == self.parents[i]:
                return i
            self.parents[i] = find(self.parents[i])
            return self.parents[i]
        
        def union(a,b):
            a = find(a)
            b = find(b)
            if self.size[a] < self.size[b]:
                self.parents[a] = self.parents[b]
                self.size[b] += self.size[a]
            else:
                self.parents[b] = self.parents[a]
                self.size[a] += self.size[b]
            
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return False
            union(edge[0], edge[1])
        
        return max(self.size) == n