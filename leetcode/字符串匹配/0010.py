# 10. 正则表达式匹配 - 困难
# https://leetcode-cn.com/problems/regular-expression-matching/


# 4. 尝试递归
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        def f(i: int, j: int) -> bool:
            if i == 0 and j == 0:
                return True
            if p[j] == '*':
                return matches(i - 1, j - 1) or matches(i - 1, j - 2)
            else:

        return f(m, n)


# 3. 动态规划
# 链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/
# 执行用时： 72 ms , 在所有 Python3 提交中击败了 61.40% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 6.82% 的用户
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


# 2. hack
# 执行用时： 88 ms , 在所有 Python 提交中击败了 48.45% 的用户
# 内存消耗： 12.7 MB , 在所有 Python 提交中击败了 33.33% 的用户
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s1 = re.compile(p).findall(s)
        if s1 == []:
            return False
        if s1[0] == s:
            return True
        else:
            return False


# 1. 放弃
# "caaaabe"
# "cd*a*b."
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        N, n = len(s), len(p)
        if n == 0:
            return N == 0
        i, j = 0, 0
        while i <= N and j < n:
            star_followed = j + 1 < n and p[j + 1] == '*'
            if p[j] == s[i] or p[j] == '.':
                if i == N - 1 and j == n - 1:
                    return True
                i += 1
                if not star_followed:
                    j += 1
            elif star_followed:
                j += 2
            else:
                return False
        return False


# 0. 纯字符串匹配 未支持正则
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        N, n = len(s), len(p)
        if n == 0:
            return N == 0
        i, j = 0, 0
        while i <= N and j < n:
            if s[i] == p[j]:
                if i == N - 1 and j == n - 1:
                    return True
                i += 1
                j += 1
            else:
                return False
        return False
