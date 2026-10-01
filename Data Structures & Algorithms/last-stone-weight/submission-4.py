import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negS = [-stone for stone in stones]
        heapq.heapify(negS)
        while len(negS) > 1:
            one = -heapq.heappop(negS)
            two = -heapq.heappop(negS)
            if one != two:
                one = one - two
                heapq.heappush(negS, -one)
        if len(negS) == 0:
            return 0
        return -negS[0]