# 67. 二进制求和
# https://leetcode-cn.com/problems/add-binary/
# https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/

# 4. 方法二：位运算
# 如果不允许使用加减乘除，则可以使用位运算替代上述运算中的一些加减乘除的操作。
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 93.68% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


# 3. 方法一：模拟
# 我们可以借鉴「列竖式」的方法，末尾对齐，逐位相加。在十进制的计算中「逢十进一」，二进制中我们需要「逢二进一」。
# 执行用时： 60 ms , 在所有 Python3 提交中击败了 12.59% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA, lenB = len(a), len(b)
        ans, carry, n = "", 0, max(lenA, lenB)

        for i in range(n):
            if i < lenA:
                carry += ord(a[lenA-i-1]) - ord('0')
            if i < lenB:
                carry += ord(b[lenB-i-1]) - ord('0')
            ans = str(int(carry % 2)) + ans
            carry //= 2  # 整除
        if carry > 0:
            ans = '1' + ans
        return ans


# 2. 直接使用工具函数
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 93.68% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


# 1. 笨方法 - 自解
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 30.20% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 6.25% 的用户
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, i, carry = "", 1, 0
        while carry or i <= len(a) or i <= len(b):
            curr = ""
            ai = a[-i] if i <= len(a) else '0'
            bi = b[-i] if i <= len(b) else '0'
            if ai == '1':
                if bi == '1':
                    curr = '1' if carry else '0'
                    carry = 1
                else:
                    curr = '0' if carry else '1'
                    carry = 1 if carry else 0
            else:
                if bi == '1':
                    curr = '0' if carry else '1'
                    carry = 1 if carry else 0
                else:
                    curr = '1' if carry else '0'
                    carry = 0
            ans, i = curr + ans, i + 1
        return ans
