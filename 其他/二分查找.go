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
