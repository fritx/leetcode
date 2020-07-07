# 16. 最接近的三数之和
# https://leetcode-cn.com/problems/3sum-closest/
# https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/

# 提示：
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

# 示例：
# [-1,2,1,-4], target=1
# ans=2, (-1 + 2 + 1 = 2)
# [84,-17,32,-89,55,79,27,-60,36,-51,39,-89,-77,97,38,-72,6,-49,-74,44,-24,95,-33,-13,-75,-25,8,-61,87,49,-71,12,76,-81,-65,79,-81,39,25,-49,48,45,-54,74,-95,64,-42,-7,-3,68,-46,-56,-17,5,-13,74,-95,84,56,-88,-79,82,-60,-5,43,-29,51,-81,47,42,-6,-54,100,48,61,71,19,-27,7,40,-37,72,20,88,-4,60,10,44,-17,30,-60,-18,19,-90,-9,-42,-65,-100,32,85,-82,80,23,0,49,-19,97,-54,14,7,5,-35,-29,-20,-53,30,14,-92,66,45,54,90,33,-99,18,-2,21,25,3,78,-16,-56,84,1,4,-30,76,-40,-28,88,44,2,-59,-82,73,50,-67,-53,-85,32,66,79,-47,-82,57,87,-91,98]
# -216
# [0, 0, 0]
# 1
# [1, 1, -1, -1, 3]
# 1

# 4. 完善自官方解
# 执行用时： 112 ms , 在所有 Python3 提交中击败了 76.85% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 9.38% 的用户
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n, ans = len(nums), 10**7  # 合理的预设值
        if n <= 3:
            return sum(nums)
        nums.sort()  # 排序

        def update(curr: int):
            nonlocal ans
            if abs(curr - target) < abs(ans - target):
                ans = curr

        for i in range(n - 2):  # 枚举i
            j, k = i + 1, n - 1  # 枚举j,k
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                update(s)
                if s > target:
                    copy = nums[k]
                    while k > j and nums[k] == copy:
                        k = k - 1
                else:
                    copy = nums[j]
                    while j < k and nums[j] == copy:
                        j = j + 1

        return ans

# 3. 排序+双指针 - 官方解
# 执行用时： 116ms, 在所有Python3 提交中击败了 71.80% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 9.38% 的用户


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best


# 2. 笨方法 尝试剪枝 - 自解
# 执行用时： 6520 ms , 在所有 Python3 提交中击败了 5.02% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 9.38% 的用户
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # tmp = list(set(nums))  # 去重  # 不能去重
        # if len(tmp) >= 3:
        #     nums = tmp
        N, ans = len(nums), None
        if N <= 3:
            return sum(nums)
        nums.sort()  # 排序
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                lastDiff = None
                toContinue = False
                for k in range(j + 1, N):
                    summ = nums[i] + nums[j] + nums[k]
                    if summ == target:
                        return target
                    currDiff = abs(summ - target)
                    if lastDiff is not None and currDiff > lastDiff:
                        toContinue = True
                        break
                    lastDiff = currDiff
                    if ans is None or currDiff < abs(ans - target):
                        ans = summ
                if toContinue:
                    continue
        return ans


# 1. 笨方法 三重循环 - 自解
# 执行结果：超时
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N, ans = len(nums), None
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    summ = nums[i] + nums[j] + nums[k]
                    if ans is None or abs(summ - target) < abs(ans - target):
                        ans = summ
        return ans
