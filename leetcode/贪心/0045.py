# 45. 跳跃游戏 II - 困难
# https://leetcode-cn.com/problems/jump-game-ii/
# https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/


# 4. 方法二：正向查找可到达的最大位置
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 84.34% 的用户
# 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 12.50% 的用户
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, steps = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    steps += 1
        return steps


# 3. 方法一：反向查找出发位置 - 超时
class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0
        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        return steps


# 2. 反向 双重循环 - 超时 [1,1,1,...,1]
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        steps, curr = 0, N - 1
        while curr > 0:
            found = False
            for i in range(curr):
                if i + nums[i] >= curr:
                    curr, steps, found = i, steps + 1, True
                    break
            if not found:
                return -1
        return steps


# 1. 递归+记忆化 - 依然超时 [1,1,1,...,1]
class Solution:
    def __init__(self):
        self.memo = {}

    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N in self.memo:
            return self.memo[N]
        if N == 2:
            return 1
        if N == 1:
            return 0
        if N == 0 or nums[0] == 0:
            return -1
        min_r = float("inf")
        for i in range(1, nums[0] + 1):
            r = self.jump(nums[i:])
            if r >= 0:
                min_r = min(min_r, r)
        ret = 1 + min_r
        self.memo[N] = ret
        return ret
