class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left = 0
        dq = deque()

        for right in range(len(nums)):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            dq.append(right)
            if dq[0] < left:
                dq.popleft()      
            if right -left+1 == k:   
                output.append(nums[dq[0]])
                left += 1
        return output
