# 96. 不同的二叉搜索树 - 中等
# https://leetcode-cn.com/problems/unique-binary-search-trees/


# 3. 方法二：数学 - 卡塔兰数公式
# C0 = 1, C(n+1) = 2(2n+1)/(n+2)Cn
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)


# 2. 方法一：动态规划
# - G(n) = ∑i = 1..n F(i, n) = F(0, n) + F(1, n) + ... + F(n, n)
# - G(0) = G(1) = 1
# - F(i, n) = G(i-1) G(n-i)
# = > G(n) = ∑i = 1..n G(i-1) G(n-i)
# G(n) 的值依赖于 G(0)..G(n-1)
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]


# 1. 递归+记忆化
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        ans = 1
        if n >= 2:
            ans = 0
            for mid in range(n):
                curr = self.numTrees(mid - 0) * self.numTrees(n - 1 - mid)
                ans += curr
        self.memo[n] = ans
        return ans
