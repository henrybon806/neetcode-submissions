class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0

        while left < right:
            l = heights[left]
            r = heights[right]
            dist = right-left
            minv = min(l,r)
            best = max(best, minv*dist)
            if l < r:
                left += 1
            else:
                right -= 1
        return best