# 1392. 最长快乐前缀 - 困难
# https://leetcode-cn.com/problems/longest-happy-prefix/
# https://leetcode-cn.com/problems/longest-happy-prefix/solution/zui-chang-kuai-le-qian-zhui-by-leetcode-solution/

# 如何更好地理解和掌握 KMP 算法? - 海纳的回答 - 知乎
# https: // www.zhihu.com/question/21923021/answer/281346746

# 输入：s = "ababab"
# 输出："abab"
# 解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
# 输入：s = "leetcodeleet"
# 输出 ： "leet"
# 输入：s = "a"
# 输出：""


# 4.2 尝试算KmpPmt而不是next
# 执行用时： 260 ms , 在所有 Python3 提交中击败了 97.85% 的用户
# 内存消耗： 18 MB , 在所有 Python3 提交中击败了 100.00% 的用户
def getKmpPmt(s: List) -> List[int]:
    pmt = [0 for _ in range(len(s))]
    currlen = 0

    for i in range(1, len(s)):
        while currlen > 0 and s[i] != s[currlen]:
            currlen = pmt[currlen - 1]
        if s[i] == s[currlen]:
            currlen += 1
        pmt[i] = currlen

    return pmt


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = getKmpPmt(s)[-1]
        return s[:n]


# 4.1 Python kmp 求next数组 击败87% 用户
# https://leetcode-cn.com/problems/longest-happy-prefix/solution/python-kmp-qiu-nextshu-zu-ji-bai-87-yong-hu-by-hao/
# 执行用时： 392 ms , 在所有 Python3 提交中击败了 70.82% 的用户
# 内存消耗： 18.2 MB , 在所有 Python3 提交中击败了 100.00% 的用户
def getKmpNext(data: List) -> List[int]:
    nxt = [0 for _ in range(len(data))]
    nxt[0] = -1
    j, k = 0, -1

    while j < len(data) - 1:
        if k == -1 or data[j] == data[k]:
            j, k = j + 1, k + 1
            nxt[j] = k
        else:
            k = nxt[k]

    return nxt


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = getKmpNext(s + ' ')[-1]
        return s[:n]


# 4. 方法二：KMP 算法
# KMP 算法 是一种高效的字符串匹配算法。KMP 算法的实现简单，但流程和证明较为复杂
# 执行用时： 384 ms , 在所有 Python3 提交中击败了 71.67% 的用户
# 内存消耗： 17.8 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        return s[:fail[-1] + 1]


# 3. 方法一：Rabin-Karp 字符串编码
# Rabin-Karp 字符串编码是一种将字符串映射成整数的编码方式，可以看成是一种哈希算法。
# 执行用时： 880 ms , 在所有 Python3 提交中击败了 45.92% 的用户
# 内存消耗： 14.1 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        prefix, suffix = 0, 0
        base, mod, mul = 31, 1000000007, 1
        happy = 0
        for i in range(1, n):
            prefix = (prefix * base + (ord(s[i - 1]) - 97)) % mod
            suffix = (suffix + (ord(s[n - i]) - 97) * mul) % mod
            if prefix == suffix:
                happy = i
            mul = mul * base % mod
        return s[:happy]


# 2. 记录相同首字母 双重循环 - 超时
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)

        for offset in range(1, N + 1):
            matched = True
            for i in range(offset, N):
                if s[i] != s[i - offset]:
                    matched = False
                    break
            if matched:
                return s[0: N - offset]

        return ""


# 1. 暴力 双指针 双重循环 - 超时
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)

        for R in range(N - 1, 0, -1):
            prefix = s[0:R]
            plen = len(prefix)
            matched = True
            for q in range(1, len(prefix) + 1):
                if prefix[-q] != s[-q]:
                    matched = False
                    break
            if matched:
                return ans

        return ""


# 0.1 暴力切片
# 执行用时： 1532 ms , 在所有 Python3 提交中击败了 36.91% 的用户
# 内存消耗： 14.2 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[:-i] == s[i:]:
                return s[:-i]
        return ""


# 0. 新思路：双向扫描法 O(N)
# https://leetcode-cn.com/problems/longest-happy-prefix/solution/xin-si-lu-shuang-xiang-sao-miao-fa-on-by-yidadaa/
class Solution:
    def longestPrefix(self, s: str) -> str:
        l, r = 0, len(s) - 1  # 左右指针
        ls, rs = '', ''  # 用于存储左右指针扫描过的字符
        ret = ''  # 最长快乐前缀
        while l < len(s) and r >= 0:
            lmove, rmove = False, False  # 用两个布尔变量控制左右指针是否应该移动
            if len(ls) == len(rs):
                if ls == rs and ls != s:
                    ret = ls  # 如果前缀和后缀相等，保存为快乐前缀
                lmove = True
                rmove = True
            elif len(ls) < len(rs):
                lmove = True  # 如果前缀比后缀短，那么移动左指针
            else:
                rmove = True  # 否则移动右指针

            if lmove:
                while l < len(s) and s[l] != s[-1]:  # 左指针负责寻找字符串中与字符串结尾字符相等的字符
                    ls += s[l]
                    l += 1
                ls += s[l]
                l += 1
            if rmove:
                while r >= 0 and s[r] != s[0]:  # 右指针负责寻找字符串中与字符串开始字符相等的字符
                    rs = s[r] + rs
                    r -= 1
                rs = s[r] + rs
                r -= 1
        return ret
