# 63. 不同路径 II - 中等
# https://leetcode-cn.com/problems/unique-paths-ii/

# 1. 动态规划 - 维护二维数组
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 93.44% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 14.29% 的用户
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        if not rows:
            return 0
        cols = len(obstacleGrid[0])
        if not cols:
            return 0
        dp = [[0] * cols for _ in range(rows)]

        for ir in range(rows):
            for ic in range(cols):
                if obstacleGrid[ir][ic] == 1:  # 增设障碍判断 (优先级最高)
                    dp[ir][ic] = 0
                elif ir == 0 and ic == 0:
                    dp[ir][ic] = 1
                else:
                    prv = dp[ir - 1][ic] if ir else 0
                    pcv = dp[ir][ic - 1] if ic else 0
                    dp[ir][ic] = prv + pcv

        return dp[-1][-1]
