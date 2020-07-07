// 27. 移除元素
// 执行结果： 通过
// 执行用时 : 76 ms , 在所有 JavaScript 提交中击败了 30.86% 的用户
// 内存消耗 : 33 MB , 在所有 JavaScript 提交中击败了 100.00% 的用户
let removeElement = function(nums, val) {
    let i = 0
    while (i < nums.length) {
        if (nums[i] === val) nums.splice(i, 1)
        else i++
    }
    return nums.length
};
