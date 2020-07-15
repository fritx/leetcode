// 96. 不同的二叉搜索树 - 中等
// https://leetcode-cn.com/problems/unique-binary-search-trees/
// https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/


// 3. 方法二：数学 - 卡塔兰数公式
// C0 = 1, C(n+1) = 2(2n+1)/(n+2)Cn
func numTrees(n int) int {
    C := 1
    for i := 0; i < n; i++ {
        C = C * 2 * (2 * i + 1) / (i + 2);
    }
    return C
}


// 2. 方法一：动态规划
// - G(n) = ∑i=1..n F(i, n) = F(0, n) + F(1, n) + ... + F(n, n)
// - G(0) = G(1) = 1
// - F(i, n) = G(i-1) G(n-i)
// => G(n) = ∑i=1..n G(i-1) G(n-i)
// G(n) 的值依赖于 G(0)..G(n-1)
func numTrees(n int) int {
    G := make([]int, n + 1)
    G[0], G[1] = 1, 1
    for i := 2; i <= n; i++ {
        for j := 1; j <= i; j++ {
            G[i] += G[j-1] * G[i-j]
        }
    }
    return G[n]
}


// 1. 递归+记忆化
var mp = map[int]int{}

func numTrees(n int) int {
    m, ok := mp[n]
    if ok {
        return m
    }
    ans := 1
    if n >= 2 {
        ans = 0
        for mid := 0; mid < n; mid++ {
            ans += numTrees(mid - 0) * numTrees(n - 1 - mid)
        }
    }
    mp[n] = ans
    return ans
}
