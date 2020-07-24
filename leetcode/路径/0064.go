// 64. 最小路径和 - 中等
// https://leetcode-cn.com/problems/minimum-path-sum/
// https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/

// [[1,3,1],[1,5,1],[4,2,1]] - 7
// [[1,2],[1,1]] - 3
// [[1]] - 0


// 2. 动态规划 - 滑动窗口
// 执行用时： 8 ms , 在所有 Go 提交中击败了 89.76% 的用户
// 内存消耗： 4.3 MB , 在所有 Go 提交中击败了 33.33% 的用户
func minPathSum(grid [][]int) int {
    nRows, nCols := len(grid), len(grid[0])
    curArr := make([]int, nCols)
    curArr[0] = grid[0][0]
    for j := 1; j < nCols; j++ {
        curArr[j] = curArr[j - 1] + grid[0][j]
    }
    for i := 1; i < nRows; i++ {
        lastArr := curArr
        curArr = make([]int, nCols)
        curArr[0] = lastArr[0] + grid[i][0]
        for j := 1; j < nCols; j++ {
            curArr[j] = min(curArr[j - 1], lastArr[j]) + grid[i][j]
        }
    }
    return curArr[nCols - 1]
}


// 1. 递归+记忆化
// 执行用时： 20 ms , 在所有 Go 提交中击败了 6.10% 的用户
// 内存消耗： 6.3 MB , 在所有 Go 提交中击败了 16.67% 的用户
type Point struct {
    x, y int
}
func minPathSum(grid [][]int) int {
    memo := map[Point]int{}
    return recur(grid, len(grid) - 1, len(grid[0]) - 1, memo)
}
func recur(grid [][]int, x int, y int, memo map[Point]int) int {
    if x < 0 || y < 0 {
        return 0
    }
    p, cur := Point{x, y}, grid[x][y]
    if mo, ok := memo[p]; ok {
        return mo
    }
    if x == 0 && y == 0 {
        return cur
    }
    fromtop, fromleft := math.MaxInt32, math.MaxInt32
    if x > 0 {
        fromleft = recur(grid, x - 1, y, memo)
    }
    if y > 0 {
        fromtop = recur(grid, x, y - 1, memo)
    }
    memo[p] := min(fromleft, fromtop) + cur
    return memo[p]
}
func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}
