# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/

# https://leetcode-cn.com/problems/word-break/solution/dan-ci-chai-fen-by-leetcode-solution/
# https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/

# "leetcode"
# ["leet", "code"]
# "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
# ["abbcbda", "cbdaaa", "b", "dadaaad", "dccbbbc", "dccadd", "ccbdbc", "bbca", "bacbcdd", "a", "bacb", "cbc", "adc", "c", "cbdbcad", "cdbab", "db", "abbcdbd", "bcb", "bbdab", "aa", "bcadb", "bacbcb", "ca", "dbdabdb",
#     "ccd", "acbb", "bdc", "acbccd", "d", "cccdcda", "dcbd", "cbccacd", "ac", "cca", "aaddc", "dccac", "ccdc", "bbbbcda", "ba", "adbcadb", "dca", "abd", "bdbb", "ddadbad", "badb", "ab", "aaaaa", "acba", "abbb"]

# 2. 官方解 - 动态规划


# 3. BFS + 避免遍历重复节点


# 2. 递归 + 记忆化


# 1. 自解 - 笨方法 字典 + 内部递归
# 执行结果：超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dct = {}
        for word in wordDict:
            dct[word] = True
        # print(dct)

        def check(v: str) -> bool:
            # print(str(["check v", v]))
            n = len(v)
            for i in range(n):
                s0, s1 = v[0:i], v[i:]
                pre = check(s0)
                # print(str([s0, s1, s1 in dct, pre]))
                if s1 in dct and (i <= 0 or pre):
                    return True
            return False

        return check(s)
