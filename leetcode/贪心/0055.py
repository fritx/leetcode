# 55. 跳跃游戏 - 中等
# https://leetcode-cn.com/problems/jump-game/

# 1. 贪心
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 93.07% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 6.90% 的用户
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if i > max_i:
                return False
            elif i+jump > max_i:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        return max_i >= i
