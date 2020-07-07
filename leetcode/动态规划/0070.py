# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/

# 3. 动态规划 滚动数组 (只保留3个变量)
# 执行用时: 16 ms , 在所有 Python 提交中击败了 86.14% 的用户
# 内存消耗: 12.9 MB , 在所有 Python 提交中击败了 6.67% 的用户
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        q = 0
        r = 1
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q
        return r


# 2. 动态规划 一维数组
# 执行用时: 20 ms , 在所有 Python 提交中击败了 66.55% 的用户
# 内存消耗: 12.7 MB , 在所有 Python 提交中击败了 6.67% 的用户
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


# 1. 递归
# 执行结果: 超时
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        each_max = 2
        if n == 0:
            return 1
        if n < 0:
            return 0
        sum = 0
        for i in range(each_max):
            each = i + 1
            sum = sum + self.climbStairs(n - each)
        return sum
