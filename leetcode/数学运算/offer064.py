# 剑指 Offer 64. 求1+2 +…+n


# 1. 递归
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 56.93% 的用户
# 内存消耗： 21.4 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def sumNums(self, n: int) -> int:
        if n == 0:
            return 0
        return self.sumNums(n - 1) + n


# 0. builtin
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n + 1))
