# -*- coding:utf-8 -*-

# 题目描述
# 写一个函数，求两个整数之和，要求在函数体内不得使用 +、-、*、/ 四则运算符号。
# https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215
# https://www.nowcoder.com/questionTerminal/59ac416b4b944300b617d4f7f111b215

# 3. by GooHub
class Solution:
    def Add(self, num1, num2):
        # write code here
        # 由于题目要求不能使用四则运算，那么就需要考虑使用位运算
        # 两个数相加可以看成两个数的每个位先相加，但不进位，然后在加上进位的数值
        # 如12+8可以看成1+0=1 2+8=0，由于2+8有进位，所以结果就是10+10=20
        # 二进制中可以表示为1000+1100 先每个位置相加不进位，
        # 则0+0=0 0+1=1 1+0=1 1+1=0这个就是按位异或运算
        # 对于1+1出现进位，我们可以使用按位与运算然后在将结果左移一位
        # 最后将上面两步的结果相加，相加的时候依然要考虑进位的情况，直到不产生进位
        # 注意python没有无符号右移操作，所以需要越界检查
        # 按位与运算：相同位的两个数字都为1，则为1；若有一个不为1，则为0。
        # 按位异或运算：相同位不同则为1，相同则为0。
        while num2:
            result = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1 ^ 0xffffffff)
        return result

# 2. by 尹斗俊喊你去学习
# 不得不吐槽下Python对位操作简直是深坑一座- -
# 主要原因还是因为python没有无符号又移操作，所以需要越界检查一波～
# 运行时间：22ms
# 占用内存：5856k


class Solution:
    def Add(self, a, b):
        while(b):
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)


# 1. 以下python中有问题
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp
        return num1
