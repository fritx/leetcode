// 45. 跳跃游戏 II - 困难
// https://leetcode-cn.com/problems/jump-game-ii/
// https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/

// 2. 方法二：正向查找可到达的最大位置
func jump(nums []int) int {
    length := len(nums)
    end := 0
    maxPosition := 0
    steps := 0
    for i := 0; i < length - 1; i++ {
        maxPosition = max(maxPosition, i + nums[i])
        if i == end {
            end = maxPosition
            steps++
        }
    }
    return steps
}
func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

// 1. 方法一：反向查找出发位置 - 超时
func jump(nums []int) int {
    position := len(nums) - 1
    steps := 0
    for position > 0 {
        for i := 0; i < position; i++ {
            if i + nums[i] >= position {
                position = i
                steps++
                break
            }
        }
    }
    return steps
}
