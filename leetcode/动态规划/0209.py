# 209. 长度最小的子数组
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/

# 7
# [2, 3, 1, 2, 4, 3]
# >> 2
# 213
# [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
# >> 8

# 1. wip 笨方法 - 递归 - 状态转移方程还不正确
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        def check(v: int, lst: List[int]) -> int:
            size = len(lst)
            if size == 0:
                return float("inf")

            f = lst[0]
            if size == 1:
                return 1 if f >= v else float("inf")

            a = check(v, lst[1:])  # 不取第一项
            b = 1 + check(v - f, lst[1:])  # 取第一项
            return min(a, b)

        ret = check(s, nums)
        return 0 if ret > len(nums) else ret
