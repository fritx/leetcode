// 174. 地下城游戏 - 困难
// https://leetcode-cn.com/problems/dungeon-game/
// https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/

// 1. 方法一：动态规划
// 执行用时： 8 ms , 在所有 Go 提交中击败了 34.15% 的用户
// 内存消耗： 3.7 MB , 在所有 Go 提交中击败了 100.00% 的用户
func calculateMinimumHP(dungeon [][]int) int {
    n, m := len(dungeon), len(dungeon[0])
    dp := make([][]int, n + 1)
    for i := 0; i < len(dp); i++ {
        dp[i] = make([]int, m + 1)
        for j := 0; j < len(dp[i]); j++ {
            dp[i][j] = math.MaxInt32
        }
    }
    dp[n][m - 1], dp[n - 1][m] = 1, 1
    for i := n - 1; i >= 0; i-- {
        for j := m - 1; j >= 0; j-- {
            minn := min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(minn - dungeon[i][j], 1)
        }
    }
    return dp[0][0]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
