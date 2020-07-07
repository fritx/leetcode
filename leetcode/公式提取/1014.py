# 2. 枚举 O(n)
# 执行用时: 468 ms , 在所有 Python 提交中击败了 73.56% 的用户
# 内存消耗: 17.2 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx, ans = A[0] + 0, -1
        for j in range(1, len(A)):
            ans = max(ans, mx + A[j] - j)
            mx = max(mx, A[j] + j)  # 边遍历边维护
        return ans


# 1. 枚举 O(n^2) - 超时
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        if N <= 1:
            return 0
        ans = 0
        for i in range(0, N - 1):
            for j in range(i + 1, N):
                tmp = A[i] + A[j] - (j - i)
                if tmp > ans:
                    ans = tmp
        return ans
