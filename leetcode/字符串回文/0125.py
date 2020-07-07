# 125. 验证回文串
# https://leetcode-cn.com/problems/valid-palindrome/

# 3. 筛选+逆序
# 执行用时： 40 ms , 在所有 Python 提交中击败了 80.75% 的用户
# 内存消耗： 14.8 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


# 2. 使用了 .alnum()
# 执行用时： 44 ms , 在所有 Python 提交中击败了 72.42% 的用户
# 内存消耗： 13.1 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True


# 1. 判断code或None
# 执行用时： 60 ms , 在所有 Python 提交中击败了 48.50% 的用户
# 内存消耗： 12.9 MB , 在所有 Python 提交中击败了 100.00% 的用户
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        i, j = 0, N - 1

        def getcode(c):
            code = ord(c)
            if code >= 65 and code <= 90:  # A-Z
                code += 32
            if code >= 97 and code <= 122:  # a-z
                return code
            if code >= 48 and code <= 57:  # 0-9
                return code
            return None

        while i < j:
            while i < j and getcode(s[i]) is None:
                i += 1
            while i < j and getcode(s[j]) is None:
                j -= 1
            if i < j:
                if getcode(s[i]) is getcode(s[j]):
                    i += 1
                    j -= 1
                else:
                    return False
        return True
