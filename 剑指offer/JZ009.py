# -*- coding:utf-8 -*-

# 变态跳台阶
# https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&&tqId=11162&rp=1&ru=/activity/oj&qru=/ta/coding-interviews/question-ranking

# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 0 1 2 3 4 5 6
# 1 1 2 4 8

# 2. 直接乘2
# 运行时间：26ms
# 占用内存：5836k
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return pow(2, number - 1)


# 1. 滚动数组
# 运行时间：21ms
# 占用内存：5732k
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = []
        dp = [1, 1, 2]
        for i in range(1, number):
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[1] * 2
        return dp[1]
