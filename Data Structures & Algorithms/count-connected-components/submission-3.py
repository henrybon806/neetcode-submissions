class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = list(range(n))
        self.size = [1] * n
        self.components = 0

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
            union(edge[0], edge[1])
        
        newparents = set()
        for parent in self.parents:
            newparents.add(find(parent))
            
        return len(newparents)
