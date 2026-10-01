class MedianFinder:

    def __init__(self):
        self.length = 0
        self.heap = []

    def addNum(self, num: int) -> None:
        self.length += 1
        self.heap.append(num)
        self.heap.sort()

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.heap[(self.length//2)-1] + self.heap[(self.length//2)]) / 2
        return self.heap[(self.length//2)]
        