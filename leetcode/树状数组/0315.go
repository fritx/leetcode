
// 315. 计算右侧小于当前元素的个数 - 困难
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/

// 「树状数组」是一种可以动态维护序列前缀和的数据结构，它的功能是：
// - 单点更新 update(i, v)： 把序列 i 位置的数加上一个值 v，在该题中 v = 1
// - 区间查询 query(i)： 查询序列 [1⋯i] 区间的区间和，即 i 位置的前缀和


// 3. 方法一：离散化树状数组
// 执行用时： 16 ms , 在所有 Go 提交中击败了 60.77% 的用户
// 内存消耗： 5.5 MB , 在所有 Go 提交中击败了 100.00% 的用户
var a, c []int

func countSmaller(nums []int) []int {
    resultList := []int{}
    discretization(nums)
    c = make([]int, len(nums) + 5)
    for i := len(nums) - 1; i >= 0; i-- {
        id := getId(nums[i])
        resultList = append(resultList, query(id - 1))
        update(id)
    }
    for i := 0; i < len(resultList)/2; i++ {
        resultList[i], resultList[len(resultList)-1-i] = resultList[len(resultList)-1-i], resultList[i]
    }
    return resultList
}
func lowBit(x int) int {
    return x & (-x)
}
func update(pos int) {
    for pos < len(c) {
        c[pos]++
        pos += lowBit(pos)
    }
}
func query(pos int) int {
    ret := 0
    for pos > 0 {
        ret += c[pos]
        pos -= lowBit(pos)
    }
    return ret
}
func discretization(nums []int) {
    set := map[int]struct{}{}
    for _, num := range nums {
        set[num] = struct{}{}
    }
    a = make([]int, 0, len(nums))
    for num := range set {
        a = append(a, num)
    }
    sort.Ints(a)
}
func getId(x int) int {
    return sort.SearchInts(a, x) + 1
}


// 2. 暴力法 - 判断前后是否相等
// 执行用时： 948 ms , 在所有 Go 提交中击败了 5.38% 的用户
// 内存消耗： 4.3 MB , 在所有 Go 提交中击败了 100.00% 的用户
func countSmaller(nums []int) []int {
    ans := make([]int, len(nums))
    for i := len(nums) - 2; i >= 0; i-- {
        if nums[i] == nums[i + 1] {
            ans[i] = ans[i + 1]
        } else {
            for j := i; j < len(nums); j++ {
                if nums[j] < nums[i] {
                    ans[i] += 1
                }
            }
        }
    }
    return ans
}


// 1. 暴力法
// 执行用时： 876 ms , 在所有 Go 提交中击败了 5.38% 的用户
// 内存消耗： 4.3 MB , 在所有 Go 提交中击败了 100.00% 的用户
func countSmaller(nums []int) []int {
    ans := make([]int, len(nums))
    for i := 0; i < len(nums) - 1; i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[j] < nums[i] {
                ans[i] += 1
            }
        }
    }
    return ans
}
