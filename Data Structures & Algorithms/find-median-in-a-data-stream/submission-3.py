class MedianFinder:

    def __init__(self):
        self.length = 0
        self.minHeap = []
        heapq.heapify(self.minHeap)
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        self.length += 1
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            item1 = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, item1)
            item2 = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.maxHeap, -item2)
            return (item1+item2) / 2
        item1 = heapq.heappop(self.minHeap)
        heapq.heappush(self.minHeap, item1)
        return item1
        