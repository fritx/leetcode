// 1. 两数之和 - 简单
// https://leetcode-cn.com/problems/two-sum/
// https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/


// 3. 方法三：一遍哈希表
// 执行用时： 4 ms , 在所有 Go 提交中击败了 96.78% 的用户
// 内存消耗： 3.8 MB , 在所有 Go 提交中击败了 51.79% 的用户
func twoSum(nums []int, target int) []int {
    hash := map[int]int{}

    for i, n := range nums {
        if j, ok := hash[target - n]; ok {
            return []int{j, i}
        }
        hash[n] = i
    }
    // return []int{}
    return nil
}

// 2. 方法二：两边哈希表

// 1. 方法一：暴力法
