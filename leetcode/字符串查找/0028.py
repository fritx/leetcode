# 28. 实现 strStr()
# https: // leetcode-cn.com/problems/implement-strstr/submissions/

# 4.  Rabin Karp - 常数复杂度 滚动哈希
# 作者：LeetCode
# 链接：https: // leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31

        # lambda-function to convert character to integer
        def h_to_int(i): return ord(haystack[i]) - ord('a')
        def needle_to_int(i): return ord(needle[i]) - ord('a')

        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0

        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL +
                 h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start


# 3. 双指针
# 作者：LeetCode
# 链接：https: // leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 执行用时: 24 ms , 在所有 Python 提交中击败了 61.26% 的用户
# 内存消耗: 12.9 MB , 在所有 Python 提交中击败了 11.11% 的用户
class Solution:
    def strStr(self, haystack, needle):
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1

            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L

            # otherwise, backtrack
            pn = pn - curr_len + 1

        return -1


# 2. 回退时优化 todo


# 1. 暴力法
# 执行用时: 24 ms , 在所有 Python 提交中击败了 61.26% 的用户
# 内存消耗: 12.9 MB , 在所有 Python 提交中击败了 11.11% 的用户
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n > m:
            return -1
        if n <= 0:
            return 0
        i = 0
        j = 0
        while i < m:
            if haystack[i] == needle[j]:
                if j == n - 1:
                    return i - n + 1
                j = j + 1
            else:
                i = i - j
                j = 0
            i = i + 1
        return -1
