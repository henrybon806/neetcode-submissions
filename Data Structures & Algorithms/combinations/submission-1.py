class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.output = []
        
        def backtrack(i, path):
            if i > n:
                return
            if len(path) == k:
                self.output.append(path[:])
                return

            for j in range(i+1, n+1):
                path.append(j)
                backtrack(j, path)
                path.pop()
        
        backtrack(0, [])
        return self.output
                

