
// 二分查找target所在位置or应插入位置 - 2
// https://leetcode-cn.com/problems/search-insert-position/solution/sou-suo-cha-ru-wei-zhi-by-leetcode-solution/
func binaryFindInsert(nums []int, target int) int {
    n := len(nums)
    left, right := 0, n - 1
    ans := n
    for left <= right {
        mid := (right - left) >> 1 + left
        if target <= nums[mid] {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return ans
}

// 二分查找target所在位置or应插入位置 - 1
func binaryFindInsert(nums []int, tar int) int {
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

// 二分查找target所在位置
func binaryFind(nums []int, tar int) int {
    L, R := 0, len(nums) - 1
    for L <= R {
        mid := (L + R) / 2
        if nums[mid] == tar {
            return mid
        } else if nums[mid] > tar {
            R = mid - 1
        } else {
            L = mid + 1
        }
    }
    return -1
}
