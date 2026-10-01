import heapq as hp

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        distDict = {}
        for point in points:
            heapq.heappush(dist, (math.sqrt((point[0])**2 + (point[1])**2), point))
            # distDict[dist[-1]] = point
        output = []
        for i in range(k):
            curr = heapq.heappop(dist)
            output.append(curr[1])
        return output

