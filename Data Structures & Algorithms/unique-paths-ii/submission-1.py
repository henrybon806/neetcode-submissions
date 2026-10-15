class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i!=0 and j!=0:
                    curr = 0
                    if obstacleGrid[i-1][j] != 1:
                        curr += dp[i-1][j]
                    if obstacleGrid[i][j-1] != 1:
                        curr += dp[i][j-1]
                    dp[i][j] = curr
                elif i!=0:
                    curr = 0
                    if obstacleGrid[i-1][j] != 1:
                        curr += dp[i-1][j]
                    dp[i][j] = curr
                elif j!=0:
                    curr = 0
                    if obstacleGrid[i][j-1] != 1:
                        curr += dp[i][j-1]
                    dp[i][j] = curr
        return dp[-1][-1]
                