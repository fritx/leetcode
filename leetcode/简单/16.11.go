// 面试题 16.11. 跳水板
// https://leetcode-cn.com/problems/diving-board-lcci/
// https://leetcode-cn.com/problems/diving-board-lcci/solution/tiao-shui-ban-by-leetcode-solution/
// https://leetcode-cn.com/problems/diving-board-lcci/solution/li-yong-zui-da-zui-xiao-chang-du-an-zhao-gu-ding-b/

// 1. 暴力法 - 数学
func divingBoard(shorter int, longer int, k int) []int {
    if k == 0 {
        return []int{}
    }
    if shorter == longer {
        return []int{shorter * k}
    }
    lengths := make([]int, k + 1)
    for i := 0; i <= k; i++ {
        lengths[i] = shorter * (k - i) + longer * i
    }
    return lengths
}
