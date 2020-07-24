// 1025. 除数博弈 - 简单
// https://leetcode-cn.com/problems/divisor-game/
// https://leetcode-cn.com/problems/divisor-game/solution/chu-shu-bo-yi-by-leetcode-solution/

// 2 - 1 - 赢
// 3 - 2,1 - 输
// 4 - 3/2 - 赢
// 5 - 4 - 输
// 6 - 5/4/3 - 赢


// 3. 数学 - 找规律
func divisorGame(N int) bool {
    return N % 2 == 0
}


// 2. 动态规划
func divisorGame(N int) bool {
    f := make([]bool, N + 5)
    f[1], f[2] = false, true
    for i := 3; i <= N; i++ {
        for j := 1; j < i; j++ {
            if i % j == 0 && !f[i - j] {
                f[i] = true
                break
            }
        }
    }
    return f[N]
}


// 1. 递归+记忆化
// 执行用时： 4 ms , 在所有 Go 提交中击败了 37.50% 的用户
// 内存消耗： 2.2 MB , 在所有 Go 提交中击败了 100.00% 的用户
var memo = map[int]bool{
    1: false,
    2: true,
}

func divisorGame(N int) bool {
    if _, ok := memo[N]; ok {
        return memo[N]
    }
    memo[N], xarr := false, getValidX(N)
    for _, x := range xarr {
        if !divisorGame(N - x) {  // 如果对手必输 则自己必赢
            memo[N] = true
            break
        }
    }
    return memo[N]
}
func getValidX(N int) []int {
    arr := []int{}
    for x := 1; x < N; x++ {
        if N % x == 0 {
            arr = append(arr, x)
        }
    }
    return arr
}

