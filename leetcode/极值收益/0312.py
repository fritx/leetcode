# 312. 戳气球 - 困难
# https://leetcode-cn.com/problems/burst-balloons/
# https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/


# 2. 方法二：动态规划
# 执行用时： 652 ms , 在所有 Python3 提交中击败了 24.13% 的用户
# 内存消耗： 16 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        # 按行打印二维数组
        # print("rec[][]=")
        # for i in range(len(rec)):
        #     for j in range(len(rec[i])):
        #         print(rec[i][j], end='\t')

        return rec[0][n + 1]


# 1. 方法一：记忆化搜索 - 递归 分治 逆向思维
# 执行用时： 604 ms , 在所有 Python3 提交中击败了 29.48% 的用户
# 内存消耗： 16.1 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0

            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best

        return solve(0, n + 1)
