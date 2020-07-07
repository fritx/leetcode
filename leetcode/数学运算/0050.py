# 50. Pow(x, n)
# https://leetcode-cn.com/problems/powx-n/
# https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/

# 3.1 快速幂 + 迭代 (2)
# 执行用时： 20 ms , 在所有 Python 提交中击败了 79.31% 的用户
# 内存消耗： 12.6 MB , 在所有 Python 提交中击败了 50.00% 的用户
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n is 0 or x is 1:
            return 1
        if n < 0:
            x, n = 1 / x, -n
        stack = []
        while n > 1:
            stack.append(n % 2)
            n //= 2
        y = x
        while stack:
            m = stack.pop()
            y = y * y * x if m else y * y
        return y


# 3. 快速幂 + 迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 2.1 分治法 - 快速幂 + 递归
# 时间-O(logN) 空间-O(logN) 这是由于递归的函数调用会使用栈空间。
# 执行用时： 24 ms , 在所有 Python 提交中击败了 54.82% 的用户
# 内存消耗： 12.5 MB , 在所有 Python 提交中击败了 50.00% 的用户
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 2. 分治法 - 快速幂 + 递归
# 时间-O(logN) 空间-O(logN) 这是由于递归的函数调用会使用栈空间。
# 执行用时： 36 ms , 在所有 Python 提交中击败了 6.54% 的用户
# 内存消耗： 12.8 MB , 在所有 Python 提交中击败了 50.00% 的用户
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n is 1:
                return x
            a, b = n // 2, n % 2
            v = helper(x, a)
            return v * v * x if b else v * v

        if n is 0 or x is 1:
            return 1
        if n < 0:
            x, n = 1 / x, -n

        return helper(x, n)


# 1. 暴力法
# 时间-O(N) 空间-O(1)
# 执行结果: 出错 - MemoryError
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        for _ in range(n):
            ans = ans * x
        return ans
