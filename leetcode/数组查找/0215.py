# 215. 数组中的第K个最大元素
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/


# [3, 2, 1, 5, 6, 4]
# 2
# [3, 2, 3, 1, 2, 4, 5, 5, 6]
# 4
# [3, 2, 3, 1, 2, 4, 5, 5, 6]
# 9 - 边界处理

# 2. 自解 - 使用数组splice，耗时严重
# 执行用时： 3520 ms , 在所有 Python3 提交中击败了 5.01% 的用户
# 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 15.79% 的用户
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        buf = []

        while len(buf) < k:
            mx = float('-inf')
            dct = {}
            for idx, n in enumerate(nums):
                if n >= mx:
                    mx = n
                    if n in dct:
                        dct[n].append(idx)
                    else:
                        dct[n] = [idx]
            for i, idx in enumerate(dct[mx]):
                idx = idx - i
                buf.append(mx)
                nums = nums[0:idx] + nums[idx+1:]

        return buf[-1]


# 1. 自解 - 笨方法
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 91.81% 的用户
# 内存消耗： 14.1 MB , 在所有 Python3 提交中击败了 15.79% 的用户
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
