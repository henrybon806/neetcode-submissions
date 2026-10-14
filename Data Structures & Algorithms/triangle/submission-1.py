class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = {}
        def findmin(idx,l,r,curr):
            if (idx,l,r,curr) in self.memo:
                return self.memo[(idx,l,r,curr)]
            if idx >= len(triangle):
                return curr
            if r < len(triangle[idx]):
                self.memo[(idx,l,r,curr)] = min(findmin(idx+1,l,r,curr+triangle[idx][l]), findmin(idx+1,l+1,r+1,curr+triangle[idx][r]))
                return self.memo[(idx,l,r,curr)]
            self.memo[(idx,l,r,curr)] = findmin(idx+1,l,r,curr+triangle[idx][l])
            return self.memo[(idx,l,r,curr)]
        
        return findmin(1,0,1,triangle[0][0])

            