# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
# or right at any point in time.
#
#  An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
#
#  Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
#
#  The testcases are generated so that the answer will be less than or equal to
# 2 * 10⁹.
#
#
#  Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#  Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#
#  Constraints:
#
#
#  m == obstacleGrid.length
#  n == obstacleGrid[i].length
#  1 <= m, n <= 100
#  obstacleGrid[i][j] is 0 or 1.
#
#
#  Related Topics Array Dynamic Programming Matrix 👍 8699 👎 508


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        # dynamic programming problem
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # boundary values are 0, so not need to care too much about them.
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # initial dp list
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        store = obstacleGrid[0][0]
        obstacleGrid[0][0] = -1
        # iterate row and column to update the number of possible ways from 0,0 to each position
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        obstacleGrid[0][0] = store
        return dp[m - 1][n - 1]
# leetcode submit region end(Prohibit modification and deletion)
