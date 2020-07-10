// 122. 买卖股票的最佳时机 II - 简单
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode/

// [7,1,5,3,6,4]
// [1,2,3,4,5]


// 5. 动态规划 - 确定状态、确定状态转移方程、确定起始、确定终止
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
// 执行用时： 4 ms , 在所有 Go 提交中击败了 95.75% 的用户
// 内存消耗： 3.6 MB , 在所有 Go 提交中击败了 60.00% 的用户
func maxProfit(prices []int) int {
    N := len(prices)

    // 0：持有现金
    // 1：持有股票
    // 状态转移：0 → 1 → 0 → 1 → 0 → 1 → 0
    dp := make([][2]int, N)

    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i := 1; i < N; i++ {
        // 这两行调换顺序也是可以的
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    }
    return dp[N-1][0]
}


// 4. 方法三：简单的一次遍历 - 只加正数 贪心算法
// 执行用时： 8 ms , 在所有 Go 提交中击败了 18.84% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 60.00% 的用户
func maxProfit(prices []int) int {
    maxprofit := 0
    for i := 1; i < len(prices); i++ {
        if prices[i] > prices[i-1] {
            maxprofit += prices[i] - prices[i-1]
        }
    }
    return maxprofit
}

// 3. 方法二：峰谷法
// 执行用时： 4 ms , 在所有 Go 提交中击败了 95.75% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func maxProfit(prices []int) int {
    valley, peak := prices[0], prices[0]
    maxprofit, i := 0, 0
    for i < len(prices)-1 {
        for i < len(prices)-1 && prices[i] >= prices[i+1] {
            i++
        }
        valley = prices[i]
        for i < len(prices)-1 && prices[i] <= prices[i+1] {
            i++
        }
        peak = prices[i]
        maxprofit += peak - valley
    }
    return maxprofit
}


// 1.1 直观法2 - 一次遍历累加
// 执行用时： 8 ms , 在所有 Go 提交中击败了 18.84% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 60.00% 的用户
func maxProfit(prices []int) int {
    ans, dir := 0, 0
    pmin := math.MaxInt16
    prices = append(prices, math.MinInt16)
    for i, _ := range prices {
        // fmt.Printf("i=%d, num=%d\n", i, num)
        if i == 0 {
            continue
        }
        pmin = min(pmin, prices[i-1])
        if prices[i] > prices[i-1] {  // 涨
            if dir < 0 || i == 1 { // 涨的拐点 重置
                // fmt.Printf("low %d =%d\n", i, prices[i-1])
                pmin = prices[i-1]
            }
            dir = 1
        } else if prices[i] < prices[i-1] {  // 跌
            if dir > 0 || i == 1 { // 跌的拐点 盈利一波
                // fmt.Printf("high %d =%d\n", i, prices[i-1])
                // fmt.Printf("sell %d-%d\n", prices[i-1], pmin)
                ans += prices[i-1] - pmin
            }
            dir = -1
        }
    }
    return ans
}


// 1. 直观法 - 找出极值 两两叠加
// 执行用时： 8 ms , 在所有 Go 提交中击败了 18.84% 的用户
// 内存消耗： 3.4 MB , 在所有 Go 提交中击败了 60.00% 的用户
func maxProfit(prices []int) int {
    // assert len(prices) >= 2
    dir, start :=0,  1
    low, high := make([]int, 0, len(prices)), make([]int, 0, len(prices))
    for i := 1; i < len(prices); i++ {
        if prices[i] - prices[i-1] > 0 {
            if dir < 0 || start == 1 {
                low = append(low, i-1)
            }
            dir = 1
        } else if prices[i] - prices[i-1] < 0 {
            if dir > 0 || start == 1 {
                high = append(high, i-1)
            }
            dir = -1
        }
        if dir != 0 {
            start = 0
        }
    }
    if dir > 0 {
        high = append(high, len(prices)-1)
    } else {
        low = append(low, len(prices)-1)
    }
    // fmt.Printf("low=%v\n", low)
    // fmt.Printf("high=%v\n", high)

    ans, i, j := 0, 0, 0
    for {
        if i >= len(low) || j >= len(high) {
            break
        }
        if high[j] >= low[i] {
            ans += prices[high[j]] - prices[low[i]]
            i++
        }
        j++
    }

    return ans
}

func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}
func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}
