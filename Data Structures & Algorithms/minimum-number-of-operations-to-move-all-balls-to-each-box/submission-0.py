class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i != j:
                    res[i] += abs(i-j) * int(boxes[j])
        return res