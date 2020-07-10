// 309. 最佳买卖股票时机含冷冻期 - 中等
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
// http://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/


// 2. 动态规划 - 空间优化
// 0：持有股票、1：冷冻期、2：持有现金
func maxProfit(prices []int) int {
    n := len(prices)
    if n <= 1 {
        return 0
    }
    f0, f1, f2 := -prices[0], 0, 0
    for i := 1; i < n; i++ {
        newf0 := max(f0, f2 - prices[i])
        newf1 := f0 + prices[i]
        newf2 := max(f1, f2)
        f0, f1, f2 = newf0, newf1, newf2
    }
    return max(f1, f2)
}


// 1. 动态规划
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.5 MB , 在所有 Go 提交中击败了 100.00% 的用户
func maxProfit(prices []int) int {
    N := len(prices)
    if N <= 1 {
        return 0
    }

    // 0：持有现金、1：持有股票、2：冷冻期
    // 状态转移：0 → 1 → 2 → 0 → 1 → 2 → 0
    dp := make([][3]int, N)

    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i := 1; i < N; i++ {
        // 这两行调换顺序也是可以的
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])  // 0→0 2→0 一直持有现金or解冻
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  // 1→1 0→1 一直持有股票or买入
        dp[i][2] = dp[i-1][1] + prices[i]  // 1→2 卖出
    }
    return max(dp[N-1][0], dp[N-1][2])
}

func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}
