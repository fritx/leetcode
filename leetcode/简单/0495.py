# 495. 提莫攻击
# https://leetcode-cn.com/problems/teemo-attacking/

# 2.
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/teemo-attacking/solution/ti-mo-gong-ji-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 执行用时: 248 ms , 在所有 Python 提交中击败了 74.29% 的用户
# 内存消耗: 13.8 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration


# 1. 一般法
# 执行用时: 244 ms , 在所有 Python 提交中击败了 83.81% 的用户
# 内存消耗: 13.7 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        n = len(timeSeries)
        for i in range(n):
            d = timeSeries[i] - timeSeries[i - 1] if i > 0 else duration
            d = d if d < duration else duration
            ans = ans + d
        return ans
