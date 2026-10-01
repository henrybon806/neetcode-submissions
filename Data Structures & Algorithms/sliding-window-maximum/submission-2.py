class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        currmax = 0
        heap = []
        heapq.heapify(heap)

        for right in range(len(nums)):
            # currmax = max(currmax, nums[right])
            heapq.heappush(heap, (-nums[right], right))
            if right - left + 1 < k:
                continue
            elif right - left + 1 == k:
                curr = heapq.heappop(heap)
                while curr[1] < left:
                     curr = heapq.heappop(heap)
                output.append(-curr[0])
                left += 1
                if curr[1] >= left:
                    heapq.heappush(heap, curr)

        return output
