class Solution:
    def trap(self, height: List[int]) -> int:
        leftsum = [0] * len(height)
        currmax = 0

        for i in range(len(height)):
            if height[i] > currmax:
                currmax = height[i]
                continue
            leftsum[i] = max(currmax - height[i], 0)
        rightsum = [0] * len(height)
        currmax = 0
        for i in range(len(height)-1, 0 , -1):
            if height[i] > currmax:
                currmax = height[i]
            rightsum[i] = max(currmax-height[i], 0)
        output = 0
        for i in range(len(leftsum)):
            output += min(leftsum[i], rightsum[i])
        return output