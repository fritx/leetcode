// 154. 寻找旋转排序数组中的最小值 II - 困难
// https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
// https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui--16/

// [3,5,1] - 1
// [3,1,3,3] - 1
// [3,3,1,3] - 1
// [2,2,2,0,1] - 0


// 1. 官方解 - 二分查找
// -时间复杂度：O(logN)  -空间复杂度：O(1)
// 执行用时： 4 ms , 在所有 Go 提交中击败了 92.84% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func findMin(nums []int) int {
    low, high := 0, len(nums) - 1
    for low < high {
        pivot := low + (high - low) / 2
        if nums[pivot] < nums[high] {
            high = pivot
        } else if nums[pivot] > nums[high] {
            low = pivot + 1
        } else {
            high--
        }
    }
    return nums[low]
}


// 0. 自解 - 二分查找 - 直观暴力二分
// -时间复杂度：O(logN)  -空间复杂度：O(1)
// 执行用时： 4 ms , 在所有 Go 提交中击败了 92.84% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func findMin(nums []int) int {
    // fmt.Println("findMin", nums)
    N := len(nums)
    if N == 0 {
        return -1
    }
    if N == 1 {
        return nums[0]
    }
    if N == 2 {
        return min(nums[0], nums[1])
    }
    if nums[N-1] > nums[0] {
        return nums[0]
    }
    t, left, right := 0, 0, N - 1
    for left < right {
        if right == left + 1 {
            return min(nums[left], nums[right])
        }
        mid := (left + right + 1) / 2
        // fmt.Println("left", left, "right", right, "mid", mid)
        // fmt.Println("nums[left]", nums[left], "nums[mid]", nums[mid])
        if nums[mid] < nums[left] {  // <
            right = mid
            t = mid
        } else if nums[mid] > nums[left] {  // >
            left = mid
        } else {  // =
            return min(findMin(nums[left:mid]), findMin(nums[mid:right+1]))
        }
    }
    return nums[t]
}
func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}
