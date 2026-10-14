class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0] * len(boxes)
        count = 0
        csum = 0
        for i in range(len(boxes)):
            left[i] = count + csum
            csum += count
            count += int(boxes[i])

        count = 0
        csum = 0
        for i in range(len(boxes)-1,-1,-1):
            left[i] += count + csum
            csum += count
            count += int(boxes[i])
        
        return left
            