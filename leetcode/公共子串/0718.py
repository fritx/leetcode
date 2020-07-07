# 718. 最长重复子数组
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/


# 5. 滑动窗口 - 简版
# 执行用时： 4524 ms , 在所有 Python3 提交中击败了 56.30% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 28.57% 的用户
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n, res = len(A), len(B), 0
        for diff in range(-(m - 1), n):  # 枚举对应关系
            l = 0
            for i in range(max(0, -diff), min(m, n - diff)):  # 遍历公共部分
                l = l + 1 if A[i] == B[i + diff] else 0
                res = max(res, l)
        return res


# 3. 二分查找 + 哈希
# 时间复杂度：O( (M+N) log(min(M, N)) )。
# 空间复杂度：O(N)。
# 执行用时： 156 ms , 在所有 Python3 提交中击败了 100.00% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 28.57% 的用户
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        base, mod = 113, 10**9 + 9

        def check(length: int) -> bool:
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + A[i]) % mod
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)

            hashB = 0
            for i in range(length):
                hashB = (hashB * base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, len(B)):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# 3. 官方解 - 滑动窗口
# 时间复杂度： O((N+M)×min(N,M))。
# 空间复杂度： O(1)。
# 执行用时： 1756 ms , 在所有 Python3 提交中击败了 92.32% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 28.57% 的用户
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        m, n, ans = len(A), len(B), 0

        for i in range(m):
            leng = m - i
            if leng <= ans:
                break
            ans = max(ans, maxLength(i, 0, leng))
        for i in range(n):
            leng = n - i
            if leng <= ans:
                break
            ans = max(ans, maxLength(0, i, leng))

        return ans


# 2. 官方解 - 动态规划
# 时间复杂度： O(N×M)。
# 空间复杂度： O(N×M)。
# 执行用时： 6520 ms , 在所有 Python3 提交中击败了 14.28% 的用户
# 内存消耗： 38.9 MB , 在所有 Python3 提交中击败了 14.29% 的用户
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans


# 1. 暴力法 - 超时
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        ans, i = 0, 0
        for i in range(len(A)):
            if len(A) - i < ans:
                break
            for j in range(len(B)):
                if len(B) - j < ans:
                    break
                for k in range(min(len(A) - i, len(B) - j)):
                    if A[i + k] != B[j + k]:
                        break
                    ans = max(ans, k + 1)
        return ans
