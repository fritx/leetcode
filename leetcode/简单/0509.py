# 509. 斐波那契数
# https://leetcode-cn.com/problems/fibonacci-number/

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

# 执行用时： 28 ms , 在所有 Python3 提交中击败了 98.88% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n == 0:
            return a
        if n == 1:
            return b
        for _ in range(n - 1):
            a, b = b, a + b
        b = b % 1000000007
        return b
