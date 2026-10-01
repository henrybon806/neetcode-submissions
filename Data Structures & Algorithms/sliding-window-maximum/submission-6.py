class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        heap = []
        heapq.heapify(heap)

        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            if right - left + 1 < k:
                continue
            
            while heap[0][1] < left:
                    heapq.heappop(heap)
            output.append(-heap[0][0])
            left += 1

        return output
