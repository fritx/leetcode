# 1480. 一维数组的动态和
# https://leetcode-cn.com/problems/running-sum-of-1d-array/

# 执行用时： 40 ms , 在所有 Python3 提交中击败了 75.83% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            last = 0 if i == 0 else ans[-1]
            ans.append(last + n)
        return ans
