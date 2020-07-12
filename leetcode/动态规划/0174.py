# 174. 地下城游戏 - 困难
# https://leetcode-cn.com/problems/dungeon-game/
# https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/

# 1. 方法一：动态规划
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 86.15% 的用户
# 内存消耗： 14.3 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]
