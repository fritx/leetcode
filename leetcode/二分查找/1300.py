# 1300. 转变数组后最接近目标值的数组和
# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/

# 方法二：双重二分查找
# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/bian-shu-zu-hou-zui-jie-jin-mu-biao-zhi-de-shu-zu-/
# 执行用时: 64 ms , 在所有 Python3 提交中击败了 74.19% 的用户
# 内存消耗: 14.8 MB , 在所有 Python3 提交中击败了 25.00% 的用户
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)

        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1


# 方法一：枚举 + 二分查找
# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/bian-shu-zu-hou-zui-jie-jin-mu-biao-zhi-de-shu-zu-/
class Solution(object):
    def findBestValue(self, arr, target):
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans


# todo
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)

        def search(ar, tg, ):
          # noop

        t0 = arr[L] * n
        if t0 == target:
            return arr[L]
        elif t0 < target:
            search(arr, target, )
        else:

        sum = 0
        for num in arr
        sum = sum + num
        diff = target - sum

        L = 0
        R = n - 1
        min = 0
        max = 0

        d = arr[R] - arr[R - 1]
        if d == diff:
            return arr[R] - d
        elif d > diff:
            min = d
        else:

            max = d
