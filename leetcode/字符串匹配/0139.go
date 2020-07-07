// 139. 单词拆分
// https://leetcode-cn.com/problems/word-break/

// https://leetcode-cn.com/problems/word-break/solution/dan-ci-chai-fen-by-leetcode-solution/
// https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/

// "leetcode"
// ["leet", "code"]
// "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
// ["abbcbda", "cbdaaa", "b", "dadaaad", "dccbbbc", "dccadd", "ccbdbc", "bbca", "bacbcdd", "a", "bacb", "cbc", "adc", "c", "cbdbcad", "cdbab", "db", "abbcdbd", "bcb", "bbdab", "aa", "bcadb", "bacbcb", "ca", "dbdabdb",
//     "ccd", "acbb", "bdc", "acbccd", "d", "cccdcda", "dcbd", "cbccacd", "ac", "cca", "aaddc", "dccac", "ccdc", "bbbbcda", "ba", "adbcadb", "dca", "abd", "bdbb", "ddadbad", "badb", "ab", "aaaaa", "acba", "abbb"]

// 官方解 - 动态规划
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.2 MB , 在所有 Go 提交中击败了 100.00% 的用户
func wordBreak(s string, wordDict []string) bool {
    wordDictSet := make(map[string]bool)
    for _, w := range wordDict {
        wordDictSet[w] = true
    }
    dp := make([]bool, len(s) + 1)
    dp[0] = true
    for i := 1; i <= len(s); i++ {
        for j := 0; j < i; j++ {
            if dp[j] && wordDictSet[s[j:i]] {
                dp[i] = true
                break
            }
        }
    }
    return dp[len(s)]
}
