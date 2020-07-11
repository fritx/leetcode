// 169. 多数元素 - 简单
// https://leetcode-cn.com/problems/majority-element/
// https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/


// 5. 方法五：Boyer-Moore 投票算法
// 执行用时： 92 ms , 在所有 Go 提交中击败了 5.09% 的用户
// 内存消耗： 6.1 MB , 在所有 Go 提交中击败了 10.00% 的用户
func majorityElement(nums []int) int {
    x, votes := 0, 0
    for _, num := range nums {
        if votes == 0 {
            x = num
        }
        if num == x {
            votes += 1
        } else {
            votes += -1
        }
    }
    return x
}


// 4. 方法四：分治
// 执行用时： 24 ms , 在所有 Go 提交中击败了 65.64% 的用户
// 内存消耗： 6 MB , 在所有 Go 提交中击败了 20.00% 的用户
func majorityElement(nums []int) int {
    return recur(nums, 0, len(nums) - 1)
}
func recur(nums []int, lo int, hi int) int {
    // base case; the only element in an array of size 1 is the majority element.
    if lo == hi {
        return nums[lo]
    }
    // recurse on left and right halves of this slice.
    mid := (hi - lo) / 2 + lo
    left := recur(nums, lo, mid)
    right := recur(nums, mid + 1, hi)
    // if the two halves agree on the majority element, return it.
    if left == right {
        return left
    }
    // otherwise, count each element and return the "winner".
    left_cnt, right_cnt := 0, 0
    for _, n := range nums[lo : hi + 1] {
        if n == left {
            left_cnt += 1
        } else if n == right {
            right_cnt += 1
        }
    }
    if left_cnt > right_cnt {
        return left
    }
    return right
}


// 3. 方法三：随机化
// 执行用时： 24 ms , 在所有 Go 提交中击败了 65.64% 的用户
// // 内存消耗： 6 MB , 在所有 Go 提交中击败了 20.00% 的用户
func majorityElement(nums []int) int {
    majority_count := len(nums) / 2
    for {
        candidate := nums[rand.Intn(len(nums))]
        count := 0
        for _, num := range nums {
            if num == candidate {
                count += 1
            }
        }
        if count > majority_count {
            return candidate
        }
    }
}


// 2. 方法二：排序
// 执行用时： 24 ms , 在所有 Go 提交中击败了 65.64% 的用户
// 内存消耗： 5.9 MB , 在所有 Go 提交中击败了 100.00% 的用户
func majorityElement(nums []int) int {
    sort.Ints(nums)
    return nums[len(nums) / 2]
}

// 1. 方法一：哈希表
// 执行用时： 24 ms , 在所有 Go 提交中击败了 65.64% 的用户
// 内存消耗： 6 MB , 在所有 Go 提交中击败了 20.00% 的用户
// func majorityElement(nums []int) (int, error) {
func majorityElement(nums []int) int {
    cnt := make(map[int]int)
    for _, num := range nums {
        cnt[num] += 1
        if cnt[num] > len(nums) / 2 {
            // return num, nil
            return num
        }
    }
    // return -1, errors.New("not found")
    return -1
}
