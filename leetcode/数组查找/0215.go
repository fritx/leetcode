
// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// 方法一：基于快速排序的选择方法
// 时间复杂度：O(n)O(n)，如上文所述，证明过程可以参考「《算法导论》9.2：期望为线性的选择算法」。
// 空间复杂度：O(\log n)O(logn)，递归使用栈空间的空间代价的期望为 O(\log n)O(logn)。
func findKthLargest(nums []int, k int) int {
    rand.Seed(time.Now().UnixNano())
    return quickSelect(nums, 0, len(nums)-1, len(nums)-k)
}
func quickSelect(a []int, l, r, index int) int {
    q := randomPartition(a, l, r)
    if q == index {
        return a[q]
    } else if q < index {
        return quickSelect(a, q + 1, r, index)
    }
    return quickSelect(a, l, q - 1, index)
}
func randomPartition(a []int, l, r int) int {
    i := rand.Int() % (r - l + 1) + l
    a[i], a[r] = a[r], a[i]
    return partition(a, l, r)
}
func partition(a []int, l, r int) int {
    x := a[r]
    i := l - 1
    for j := l; j < r; j++ {
        if a[j] <= x {
            i++
            a[i], a[j] = a[j], a[i]
        }
    }
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1
}

// 方法二：基于堆排序的选择方法
// 时间复杂度：O(n \log n)O(nlogn)，建堆的时间代价是 O(n)O(n)，删除的总代价是 O(k \log n)O(klogn)，因为 k < nk<n，故渐进时间复杂为 O(n + k \log n) = O(n \log n)O(n+klogn)=O(nlogn)。
// 空间复杂度：O(\log n)O(logn)，即递归使用栈空间的空间代价。
func findKthLargest(nums []int, k int) int {
    heapSize := len(nums)
    buildMaxHeap(nums, heapSize)
    for i := len(nums) - 1; i >= len(nums) - k + 1; i-- {
        nums[0], nums[i] = nums[i], nums[0]
        heapSize--
        maxHeapify(nums, 0, heapSize)
    }
    return nums[0]
}
func buildMaxHeap(a []int, heapSize int) {
    for i := heapSize/2; i >= 0; i-- {
        maxHeapify(a, i, heapSize)
    }
}
func maxHeapify(a []int, i, heapSize int) {
    l, r, largest := i * 2 + 1, i * 2 + 2, i
    if l < heapSize && a[l] > a[largest] {
        largest = l
    }
    if r < heapSize && a[r] > a[largest] {
        largest = r
    }
    if largest != i {
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, largest, heapSize)
    }
}
