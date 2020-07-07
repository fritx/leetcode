# 41. 缺失的第一个正数 - 困难 (官方等级)
# https://leetcode-cn.com/problems/first-missing-positive/
# 链接：https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/


# 4. 方法二：置换
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# 3. 方法一：哈希表
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


# 2. 自解 - 取消正数filter - 不满足时间O(n)
# 执行用时： 32 ms , 在所有 Python3 提交中击败了 97.48% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 16.67% 的用户
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for n in nums:
            if n == ans:
                ans = ans + 1
        return ans


# 1. 自解 - sort之前 增设正数filter - 不满足时间O(n)
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 28.26% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 16.67% 的用户
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pnums = []
        for n in nums:
            if n > 0:
                pnums.append(n)

        pnums.sort()
        ans = 1
        for n in pnums:
            if n == ans:
                ans = ans + 1
        return ans
