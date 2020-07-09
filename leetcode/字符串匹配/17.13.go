// 面试题 17.13. 恢复空格 - 中等
// https://leetcode-cn.com/problems/re-space-lcci/
// https://leetcode-cn.com/problems/re-space-lcci/solution/hui-fu-kong-ge-by-leetcode-solution/


// 2. 方法二：字符串哈希
// 字符串哈希：可参考「1392. 最长快乐前缀」官方题解中的「背景知识」。
// 我们使用字典树的目的是查找某一个串 s 是否在一个串的集合 S 当中，并且当我们知道 s 是否在 S 中之后，可以快速的知道在 s 后添加某一个新的字母得到的新串 s' 是否在 S 中，这个转移的过程是 O(1) 的。
// 执行用时： 52 ms , 在所有 Go 提交中击败了 87.50% 的用户
// 内存消耗： 4.8 MB , 在所有 Go 提交中击败了 100.00% 的用户
const (
    P = math.MaxInt32
    BASE = 41
)

func respace(dictionary []string, sentence string) int {
    hashValues := map[int]bool{}
    for _, word := range dictionary {
        hashValues[getHash(word)] = true
    }
    f := make([]int, len(sentence) + 1)
    for i := 1; i < len(f); i++ {
        f[i] = len(sentence)
    }
    for i := 1; i <= len(sentence); i++ {
        f[i] = f[i-1] + 1
        hashValue := 0
        for j := i; j >= 1; j-- {
            t := int(sentence[j-1] - 'a') + 1
            hashValue = (hashValue * BASE + t) % P
            if hashValues[hashValue] {
                f[i] = min(f[i], f[j-1])
            }
        }
    }
    return f[len(sentence)]
}

func getHash(s string) int {
    hashValue := 0
    for i := len(s) - 1; i >= 0; i-- {
        hashValue = (hashValue * BASE + int(s[i] - 'a') + 1) % P
    }
    return hashValue
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}


// 1. 方法一：Trie + 动态规划
// 字典树 Trie
// 定义 dp[i] 表示考虑前 i 个字符最少的未识别的字符数量，从前往后计算 dp 值。
// 执行用时： 84 ms , 在所有 Go 提交中击败了 37.50% 的用户
// 内存消耗： 52 MB , 在所有 Go 提交中击败了 100.00% 的用户
func respace(dictionary []string, sentence string) int {
    n, inf := len(sentence), 0x3f3f3f3f
    root := &Trie{next: [26]*Trie{}}
    for _, word := range dictionary {
        root.insert(word)
    }
    dp := make([]int, n + 1)
    for i := 1; i < len(dp); i++ {
        dp[i] = inf
    }
    for i := 1; i <= n; i++ {
        dp[i] = dp[i-1] + 1
        curPos := root
        for j := i; j >= 1; j-- {
            t := int(sentence[j-1] - 'a')
            if curPos.next[t] == nil {
                break
            } else if curPos.next[t].isEnd {
                dp[i] = min(dp[i], dp[j-1])
            }
            if dp[i] == 0 {
                break
            }
            curPos = curPos.next[t]
        }
    }
    return dp[n]
}

type Trie struct {
    next [26]*Trie
    isEnd bool
}

func (this *Trie) insert(s string) {
    curPos := this
    for i := len(s) - 1; i >= 0; i-- {
        t := int(s[i] - 'a')
        if curPos.next[t] == nil {
            curPos.next[t] = &Trie{next: [26]*Trie{}}
        }
        curPos = curPos.next[t]
    }
    curPos.isEnd = true
}

func min(x, y int) int {
    if x < y {
				return x
		}
		return y
}
