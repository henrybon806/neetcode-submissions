class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.pac = set()
        self.atl = set()
        self.output = set()

        def explore(i,j,prev,visited):
            if i < 0 or j <0 or i >= len(heights) or j >= len(heights[0]) or (heights[i][j] < prev) or (i,j) in visited:
                return
            visited.add((i,j))
            for (newi,newj) in [(i-1,j), (i,j-1), (i,j+1),(i+1,j)]:
                explore(newi,newj,heights[i][j],visited)
                            
        for i in range(len(heights[0])):
            explore(0,i,0,self.pac)
            explore(len(heights)-1,i,0,self.atl)
        for i in range(len(heights)):
            explore(i,0,0,self.pac)
            explore(i,len(heights[0])-1,0,self.atl)

        return [list(cell) for cell in self.pac & self.atl]