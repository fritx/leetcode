// 121. 买卖股票的最佳时机 - 简单
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/

// [7,1,5,3,6,4]
// [2,2,5]
// [1,1,0]


// 3. 方法二：一次遍历
// 执行用时： 4 ms , 在所有 Go 提交中击败了 97.00% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 57.14% 的用户

// https://stackoverflow.com/questions/6878590/the-maximum-value-for-an-int-type-in-go
// const MaxUint = ^uint(0)
// const MinUint = 0
// const MaxInt = int(MaxUint >> 1)
// const MinInt = -MaxInt - 1
// const MaxInt = math.MaxInt64
// const MaxInt = math.MaxInt32
const MaxInt = math.MaxInt16

func maxProfit(prices []int) int {
    maxprofit, minprice := 0, MaxInt
    for _, price := range prices {
        maxprofit = max(maxprofit, price - minprice)
        minprice = min(minprice, price)
    }
    return maxprofit
}


// 2. 方法一：暴力法 - 双重循环
// 执行用时： 256 ms , 在所有 Go 提交中击败了 9.26% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func maxProfit(prices []int) int {
    ans := 0
    for i := 0; i < len(prices)-1; i++ {
        for j := i+1; j < len(prices); j++ {
            // fmt.Printf("i=%d, j=%d\n", i, j)
            ans = max(ans, prices[j] - prices[i])
        }
    }
    return ans
}


// 1. 直观法 - 找出极值 两两比对
// 执行用时： 4 ms , 在所有 Go 提交中击败了 97.00% 的用户
// 内存消耗： 3.2 MB , 在所有 Go 提交中击败了 14.29% 的用户
func maxProfit(prices []int) int {
    // assert len(prices) >= 2
    dir, start := 0, 1
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

    ans := 0
    for j := 0; j < len(high); j++ {
        for i := 0; i < len(low); i++ {
            if low[i] >= high[j] {
                break
            }
            ans = max(ans, prices[high[j]] - prices[low[i]])
        }
    }

    return ans
}

func max(x int, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}
