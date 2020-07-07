# 62. 不同路径 - 中等
# https://leetcode-cn.com/problems/unique-paths/

# 3. 递归+记忆化
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 51.43% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def __init__(self):
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1

        key = "{} -- {}".format(m, n)
        if key in self.memo:
            return self.memo[key]

        ret = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self.memo[key] = ret
        return ret


# 2. 滚动窗口
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 51.43% 的用户
# 内存消耗： 13.4 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1

        prevarr = [0] * (m + 1)

        for i in range(n + 1):  # 遍历cols
            currarr = [0] * (m + 1)
            for j in range(m + 1):  # 遍历rows
                if i == 1 and j == 1:
                    currarr[j] = 1
                else:
                    currarr[j] = prevarr[j] + currarr[j - 1]
            prevarr = currarr  # 滚动

        return prevarr[m]


# 1. dp动态规划
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 74.10% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):  # 遍历cols
            for j in range(m + 1):  # 遍历rows
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[i][j]
