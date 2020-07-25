// 167. 两数之和 II - 输入有序数组 - 简单
// https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
// https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/liang-shu-zhi-he-ii-shu-ru-you-xu-shu-zu-by-leet-2/


// 3. 方法二：二分查找
// -时间复杂度：O(nlogn)  -空间复杂度：O(1)
// 执行用时： 4 ms , 在所有 Go 提交中击败了 96.75% 的用户
// 内存消耗： 3 MB , 在所有 Go 提交中击败了 100.00% 的用户
func twoSum(numbers []int, target int) []int {
    for i := 0; i < len(numbers); i++ {
        low, high := i + 1, len(numbers) - 1
        for low <= high {
            mid := (high - low) / 2 + low
            if numbers[mid] == target - numbers[i] {
                return []int{i + 1, mid + 1}
            } else if numbers[mid] > target - numbers[i] {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
    }
    return []int{-1, -1}
}


// 2. 方法一：双指针
// -时间复杂度：O(n)  -空间复杂度：O(1)
// 执行用时： 4 ms , 在所有 Go 提交中击败了 96.75% 的用户
// 内存消耗： 3 MB , 在所有 Go 提交中击败了 100.00% 的用户
func twoSum(numbers []int, target int) []int {
    low, high := 0, len(numbers) - 1
    for low < high {
        sum := numbers[low] + numbers[high]
        if sum == target {
            return []int{low + 1, high + 1}
        } else if sum < target {
            low++
        } else {
            high--
        }
    }
    return []int{-1, -1}
}


// 1. 一遍哈希表
// -时间复杂度：O(n)  -空间复杂度：O(n)
// 执行用时： 4 ms , 在所有 Go 提交中击败了 96.75% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 33.33% 的用户
func twoSum(numbers []int, target int) []int {
    hash := map[int]int{}

    for i, n := range numbers {
        if j, ok := hash[target - n]; ok {
            return []int{j + 1, i + 1}
        }
        hash[n] = i
    }
    return nil
}
