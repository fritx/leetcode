// 35. 搜索插入位置 - 简单
// https://leetcode-cn.com/problems/search-insert-position/


// 1. 二分查找
// 执行用时： 4 ms , 在所有 Go 提交中击败了 90.19% 的用户
// 内存消耗： 3.4 MB , 在所有 Go 提交中击败了 16.67% 的用户
func searchInsert(nums []int, target int) int {
    return binaryFind(nums, target)
}
func binaryFind(nums []int, tar int) int {
    L, R := 0, len(nums) - 1
    for L <= R {
        mid := (L + R) / 2
        // fmt.Println(map[interface{}]interface{}{
        //     "L": L, "R": R, "mid": mid,
        // })
        if nums[mid] == tar {
            return mid
        } else if nums[mid] > tar {
            R = mid - 1
        } else {
            L = mid + 1
        }
    }
    return L
}
