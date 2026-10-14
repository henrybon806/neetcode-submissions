class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0] * len(boxes)
        count = 0
        csum = 0
        for i in range(len(boxes)):
            left[i] = count + csum
            csum += count
            count += int(boxes[i])

        right = [0] * len(boxes)
        count = 0
        csum = 0
        for i in range(len(boxes)-1,-1,-1):
            right[i] = count + csum
            csum += count
            count += int(boxes[i])
        
        return[x+y for x,y in zip(left,right)]
            