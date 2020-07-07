# 14. 最长公共前缀
# https://leetcode-cn.com/problems/longest-common-prefix/

# 执行用时: 20 ms , 在所有 Python 提交中击败了 82.36% 的用户
# 内存消耗: 13 MB , 在所有 Python 提交中击败了 5.88% 的用户
class Solution:
    def longestCommonPrefix(self, strs):
        N = len(strs)
        if N == 0:
            return ""
        s0 = strs[0]
        if N == 1:
            return s0
        l0 = len(s0)
        e = 0
        failed = False
        while not failed:
            for i in range(1, N):
                if not (e < len(strs[i]) and e < l0 and strs[i][e] == s0[e]):
                    failed = True
                    break
            e = e + 1
        return s0[:e - 1]


class Solution
   def longestCommonPrefix(self, strs):
        N = len(strs)
        if N == 0:
            return ""
        if N == 1:
            return strs[0]
        ans = self.lcp(strs[0], strs[1])
        if N == 2:
            return ans
        return self.longestCommonPrefix([ans].extend(strs[2:]))

    def lcp(self, a, b):


# 递归
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        N=len(strs)
        if N == 0:
            return ""
        if N == 1:
            return strs[0]

        s0, s1=strs[0], strs[1]
        l0, l1=len(s0), len(s1)
        i0=0
        ans=""
        while i0 < l0:
            c0=s0[i0]
            i1=0
            while i1 < l1:
                j=0
                while i1 + j < l1:
                    if s1[i1 + j] == s0[i0 + j]:
                        j=j + 1
                if j > len(ans):
                    ans=s1[0:j]
                i1=i1 + 1
            i0=i0 + 1

        if N == 2:
            return ans
        return longestCommonPrefix([ans].extend(strs[2:]))


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        N=len(strs)
        if N == 0:
            return ""
        if N == 1:
            return strs[1]

        strs=sorted(strs, key=lambda s: len(s), reverse=True)
        L0=len(strs[0])
        ans=""

        for start in range(L0):
            curr=start
            failed=False
            while curr < L0:
                start_arr=[0] * N
                for p in range(1, N):
                    sp=strs[p]
                    l=len(sp)
                    j=start_arr[p]
                    while j < l and sp[j] == strs[0][curr + j]:
                        j=j + 1
                    start_arr[p]=j
                    if not j:
                        break
                if not start_arr[-1]:
                    failed=True
                    break
                curr=curr + 1
            if failed:
                continue
            an=strs[0][start:curr + 1]
            if len(an) > len(ans):
                ans=an

        return ans
