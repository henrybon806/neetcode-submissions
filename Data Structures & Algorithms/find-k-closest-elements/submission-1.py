class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        valid = []

        for num in arr:
            heapq.heappush(valid, (-abs(num - x), -num))
            if len(valid) > k:
                heapq.heappop(valid)
        
        return sorted(-v for _, v in valid)