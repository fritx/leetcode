# 287. 寻找重复数
# https://leetcode-cn.com/problems/find-the-duplicate-number/

# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
# 可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

# 说明
# 1. 不能更改原数组（假设数组是只读的）。
# 2. 只能使用额外的 O(1) 的空间。
# 3. 时间复杂度小于 O(n2) 。
# 4. 数组中只有一个重复的数字，但它可能不止重复出现一次。


# 5. 奇妙的方法 - 借助负数&绝对值
# 执行用时： 84 ms , 在所有 Python3 提交中击败了 83.16% 的用户
# 内存消耗： 16.1 MB , 在所有 Python3 提交中击败了 35.71% 的用户
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
        return None


# 4. 二分查找 - 但是用到了.sort()
# 执行用时： 116 ms , 在所有 Python3 提交中击败了 23.78% 的用户
# 内存消耗： 16 MB , 在所有 Python3 提交中击败了 35.71% 的用户
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        L, R, ans = 0, N - 1, None
        while L <= R:
            mid, cnt = (L + R) // 2, 0
            for n in nums:
                cnt += 1 if nums[mid] <= mid else 0
            if cnt <= mid:
                L = mid + 1
            else:
                R = mid - 1
                ans = mid
        return ans


# 3. 快慢指针 - 通过地址跳转 识别为链表结构
# 执行用时： 80 ms , 在所有 Python3 提交中击败了 92.22% 的用户
# 内存消耗： 16.2 MB , 在所有 Python3 提交中击败了 35.71% 的用户
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        head = 0
        while True:
            head = nums[head]
            slow = nums[slow]
            if slow == head:
                break
        return head


# 2. HashSet哈希表 - 空间复杂度不满足题意
# 执行用时： 100 ms , 在所有 Python3 提交中击败了 45.73% 的用户
# 内存消耗： 17.7 MB , 在所有 Python3 提交中击败了 7.14% 的用户
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return None

# 1. 暴力法 双重循环 - 时间复杂度不满足题意
