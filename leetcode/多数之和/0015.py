# 执行用时: 556 ms , 在所有 Python 提交中击败了 55.07% 的用户
# 内存消耗: 18 MB , 在所有 Python 提交中击败了 5.26% 的用户
class Solution:
    def threeSum(self, nums):
        target = 0
        ans = []
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] * nums[right] > 0:
                    break
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                if s <= target:
                    left += 1
                if s >= target:
                    right -= 1
        return ans
