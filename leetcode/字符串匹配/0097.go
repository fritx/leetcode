// 97. 交错字符串 - 困难
// https://leetcode-cn.com/problems/interleaving-string/
// https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/


// 2. 方法一：动态规划
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func isInterleave(s1 string, s2 string, s3 string) bool {
    n, m, t := len(s1), len(s2), len(s3)
    if (n + m) != t {
        return false
    }
    f := make([][]bool, n + 1)
    for i := 0; i <= n; i++ {
        f[i] = make([]bool, m + 1)
    }
    f[0][0] = true
    for i := 0; i <= n; i++ {
        for j := 0; j <= m; j++ {
            p := i + j - 1
            if i > 0 {
                f[i][j] = f[i][j] || (f[i-1][j] && s1[i-1] == s3[p])
            }
            if j > 0 {
                f[i][j] = f[i][j] || (f[i][j-1] && s2[j-1] == s3[p])
            }
        }
    }
    return f[n][m]
}


// 1.1 递归 - 记忆化 - struct val as key
// https://gist.github.com/cevaris/24cc9da7b14731204c79
// https://play.golang.org/p/JC0a4GsaYO
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.7 MB , 在所有 Go 提交中击败了 100.00% 的用户
type A struct {
    s1, s2, s3 string
}
var memo = map[A]bool{}

func isInterleave(s1 string, s2 string, s3 string) bool {
    key := A{s1, s2, s3}
    if v, ok := memo[key]; ok {
        return v
    }
    ans := false
    if len(s3) == len(s1) + len(s2) {
        ans = len(s3) == 0 ||
            len(s1) > 0 && s1[0] == s3[0] && isInterleave(s1[1:len(s1)], s2, s3[1:len(s3)]) ||
            len(s2) > 0 && s2[0] == s3[0] && isInterleave(s1, s2[1:len(s2)], s3[1:len(s3)])
    }
    memo[key] = ans
    return ans
}


// 1. 递归 - 记忆化 - string as key
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.6 MB , 在所有 Go 提交中击败了 100.00% 的用户
var memo = map[string]bool{}

func isInterleave(s1 string, s2 string, s3 string) bool {
    key := s1 + "::" + s2 + "::" + s3
    if v, ok := memo[key]; ok {
        return v
    }
    ans := false
    if len(s3) == len(s1) + len(s2) {
        ans = len(s3) == 0 ||
            len(s1) > 0 && s1[0] == s3[0] && isInterleave(s1[1:len(s1)], s2, s3[1:len(s3)]) ||
            len(s2) > 0 && s2[0] == s3[0] && isInterleave(s1, s2[1:len(s2)], s3[1:len(s3)])
    }
    memo[key] = ans
    return ans
}
