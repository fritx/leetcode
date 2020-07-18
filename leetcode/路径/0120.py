# 120. 三角形最小路径和 - 中等
# https://leetcode-cn.com/problems/triangle/
# https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/

# 结语
# 本题还有一些其它的动态规划方法，例如：
# - 从三角形的底部开始转移，到顶部结束；
# - 直接在给定的三角形数组上进行状态转移，不使用额外的空间。
# 读者可以自行尝试。如果在面试中遇到类似的题目，需要和面试官进行沟通，可以询问「是否有空间复杂度限制」「是否可以修改原数组」等问题，给出符合条件的算法。


# 5. Python一趟遍历O(1)空间4行极简
# https://leetcode-cn.com/problems/triangle/solution/pythonxian-xing-shi-jian-yuan-di-kong-jian-4xing-j/
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 98.99% 的用户
# 内存消耗： 14.1 MB , 在所有 Python3 提交中击败了 9.09% 的用户
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c:c+2])
        return triangle[0][0]


# 4. 动态规划-自底向上遍历（Python3）
# https://leetcode-cn.com/problems/triangle/solution/dong-tai-gui-hua-zi-di-xiang-shang-bian-li-python3/
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 50.65% 的用户
# 内存消耗： 13.9 MB , 在所有 Python3 提交中击败了 18.18% 的用户
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0

        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


# 3. 方法二：动态规划 + 空间优化
# 时间复杂度：O(n^2)，其中 nn 是三角形的行数。
# 空间复杂度：O(n)。
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 88.46% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 18.18% 的用户
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]

        return min(f[(n - 1) % 2])


# 2. 方法一：动态规划
# 时间复杂度：O(n^2)，其中 nn 是三角形的行数。
# 空间复杂度：O(n^2。我们需要一个 n*n 的二维数组存放所有的状态。
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 50.65% 的用户
# 内存消耗： 14.7 MB , 在所有 Python3 提交中击败了 9.09% 的用户
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])


# 1. 递归+记忆化 - 貌似python超时
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)
        memo = [[-1] * size for _ in range(size)]
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle: List[List[int]], i: int, j: int, memo: List[List[int]]) -> int:
        if i > len(triangle) - 1 or j > i:
            return 0
        if memo[i][j] > -1:
            return memo[i][j]
        L = self.dfs(triangle, i + 1, j, memo)
        R = self.dfs(triangle, i + 1, j + 1, memo)
        ans = triangle[i][j] + min(L, R)
        memo[i][j] = ans
        return ans
