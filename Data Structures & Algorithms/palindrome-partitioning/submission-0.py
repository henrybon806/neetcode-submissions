class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        def backtrack(index, path):
            if index == len(s):
                self.output.append(path[:])
                return
            
            for i in range(index, len(s)):
                new = s[index: i+1]
                if new == new[::-1] and len(new) > 0:
                    path.append(new)
                    backtrack(index+len(new),path)
                    path.pop()
        backtrack(0,[])
        return self.output
                