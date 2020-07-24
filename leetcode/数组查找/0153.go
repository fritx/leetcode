// 153. 寻找旋转排序数组中的最小值 - 中等
// https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
// https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-lie-shu-zu-zhong-de-zui-xi/

// [3,4,5,1,2] - 1
// [2,3,1] - 1


// 1.1 官方解 - 二分查找 (2)
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.5 MB , 在所有 Go 提交中击败了 57.14% 的用户
func findMin(nums []int) int {
    // If the list has just one element then return that element.
     N := len(nums)
    if N == 1 {
        return nums[0]
    }

    // initializing left and right pointers.
    left, right := 0, N - 1

    // if the last element is greater than the first element then there is no rotation.
    // e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    // Hence the smallest element is first element. A[0]
    if nums[right] > nums[0] {
        return nums[0]
    }

    // Binary search way
    for right >= left {
        // Find the mid element
        mid := left + (right - left) / 2

        // if the mid element is greater than its next element then mid+1 element is the smallest
        // This point would be the point of change. From higher to lower value.
        if nums[mid] > nums[mid + 1] {
            return nums[mid + 1]
        }

        // if the mid element is lesser than its previous element then mid element is the smallest
        if nums[mid - 1] > nums[mid] {
            return nums[mid]
        }

        // if the mid elements value is greater than the 0th element this means
        // the least value is still somewhere to the right as we are still dealing with elements
        // greater than nums[0]
        if nums[mid] > nums[0] {
            left = mid + 1
        } else {
            // if nums[0] is greater than the mid value then this means the smallest value is somewhere to
            // the left
            right = mid - 1
        }
    }
    return -1
}


// 1. 自解 - 二分查找
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.5 MB , 在所有 Go 提交中击败了 57.14% 的用户
func findMin(nums []int) int {
    N := len(nums)
    if N == 1 {
        return nums[0]
    }
    if N == 2 {
        return min(nums[0], nums[1])
    }
    t, L, R := 0, 0, N - 1
    if nums[L] > nums[R] {  // 数组旋转了
        for L < R - 1 {  // 二分查找
            m := (L + R) / 2
            if nums[m] > nums[R] {
                L = m
                t = R
            } else {
                R = m
                t = m
            }
        }
    }
    return nums[t]  // 数组未旋转
}
func min(x int, y int) int {
    if x < y {
        return x
    }
    return y
}
