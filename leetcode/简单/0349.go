// 349. 两个数组的交集 - 简单
// https://leetcode-cn.com/problems/intersection-of-two-arrays/

// 1. 哈希表
// 执行用时： 4 ms , 在所有 Go 提交中击败了 88.20% 的用户
// 内存消耗： 3 MB , 在所有 Go 提交中击败了 100.00% 的用户
func intersection(nums1 []int, nums2 []int) []int {
    mp := map[int]bool{}
    ans := make([]int, 0)
    for _, n := range nums1 {
        mp[n] = true
    }
    for _, n := range nums2 {
        if mp[n] == true {
            ans = append(ans, n)
            // mp[n] = false
            delete(mp, n)
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
