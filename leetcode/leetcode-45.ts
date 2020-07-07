// 45. 跳跃游戏 II 贪心算法

// 递归
let jump1 = function(nums) {
    let len = nums.length
    if (len <= 1) return 0
    let lastIdx = len - 1
    let prevIdxs = []
    for (let i = lastIdx - 1; i >= 0; i--) {
        if (i + nums[i] >= lastIdx) prevIdxs.push(i)
    }
    if (prevIdxs.length <= 0) throw new Error('no way')
    if (prevIdxs.includes(0)) return 1
    return 1 + Math.min(...prevIdxs.map(i => jump(nums.slice(0, i + 1))))
};

// 迭代 prevIdx数组
let jump2 = function(nums) {
    let len = nums.length
    if (len <= 1) return 0
    let minSteps = 0
    let endIdxs = new Set([len - 1])
    while (true) {
        minSteps++
        let prevIdxs = new Set<number>()
        for (let endIdx of endIdxs) {
            for (let i = endIdx; i >= 0; i--) {
                if (i + nums[i] >= endIdx) prevIdxs.add(i)
            }
            if (prevIdxs.size <= 0) throw new Error('no way')
            if (prevIdxs.has(0)) return minSteps
        }
        endIdxs = prevIdxs
    }
};

// 迭代 发现只需保留prevMin
// 执行结果: 通过
// 执行用时: 344 ms,在所有 JavaScript 提交中击败了 10.84 % 的用户
// 内存消耗: 36.1 MB, 在所有 JavaScript 提交中击败了 100.00 % 的用户
let jump3 = function(nums) {
    let len = nums.length
    if (len <= 1) return 0
    let minSteps = 0
    let endIdx = len - 1
    while (true) {
        minSteps++
        let prevMin
        for (let i = 0; i < endIdx; i++) {
          if (i + nums[i] >= endIdx) {
            prevMin = i
            break
          }
        }
        if (prevMin == null) throw new Error('no way')
        if (prevMin === 0) return minSteps
        endIdx = prevMin
    }
};

// 迭代 补充了对单一步长的处理
// 执行结果: 通过
// 执行用时: 68 ms, 在所有 JavaScript 提交中击败了 85.88% 的用户
// 内存消耗: 36.1 MB, 在所有 JavaScript 提交中击败了 100.00 % 的用户
let jump4 = function(nums) {
    let len = nums.length
    if (len <= 1) return 0
    let minSteps = 0
    let endIdx = len - 1
    let isFirstLoop = true
    while (true) {
        minSteps++
        let prevMin
        let lastVal = nums[0]
        let allEqual = true
        for (let i = 0; i < endIdx; i++) {
          if (i + nums[i] >= endIdx) {
            if (prevMin == null) prevMin = i
            if (!isFirstLoop) break
          }
          if (nums[i] !== lastVal) allEqual = false
        }
        if (isFirstLoop) {
          if (allEqual) {
            if (lastVal > 0) {
              return Math.ceil((len - 1) / lastVal)
            } else {
              throw new Error('no way')
            }
          }
          isFirstLoop = false
        }
        if (prevMin == null) throw new Error('no way')
        if (prevMin === 0) return minSteps
        endIdx = prevMin
    }
};

// 位运算 by廉温
// 执行结果： 通过
// 执行用时 : 76 ms , 在所有 JavaScript 提交中击败了 52.02% 的用户
// 内存消耗 : 36 MB , 在所有 JavaScript 提交中击败了 100.00% 的用户
let jump6 = function(nums) {
    nums[0] = nums[0] << 16;
    let index = 0;
    let canIndex = 1;
    let resultMax = 0;
    for (; index < nums.length; index++) {
        // 本身的数据
        let jumpLength = nums[index] >> 16;
        resultMax = (nums[index] & 0xffff) + 1;
        let maxJump = index + 1 + jumpLength;
        if(maxJump >= nums.length){
            maxJump = nums.length;
        }
        for (; canIndex < maxJump; canIndex++) {
            nums[canIndex] = (nums[canIndex] << 16) + resultMax
        }
    }
    return resultMax - 1;
};


// 作者：optimjie
// 链接：https://leetcode-cn.com/problems/jump-game-ii/solution/dong-tai-gui-hua-tan-xin-yi-dong-by-optimjie/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
// }
let jump7 = function (nums) {
  let n = nums.length;
  let f = new Array(n);
  for (let i = 0, last = 0; i < n; i++) {
    if (i === 0) f[i] = 0;
    else {
      while (last < n && last + nums[last] < i) last++;
      f[i] = f[last] + 1; // 使用第一个能到i的点更新f[i]
    }
  }
  return f[n - 1];
}

// 55. 跳跃游戏

// 执行结果：通过
// 执行用时: 80 ms, 在所有 JavaScript 提交中击败了 36.52% 的用户
// 内存消耗 : 36.3 MB , 在所有 JavaScript 提交中击败了 75.00% 的用户
let canJump = function(nums) {
    let len = nums.length
    if (len <= 1) return true
    let endIdx = len - 1
    let isFirstLoop = true
    while (true) {
        let prevMin
        let lastVal = nums[0]
        let allEqual = true
        for (let i = 0; i < endIdx; i++) {
          if (i + nums[i] >= endIdx) {
            if (prevMin == null) prevMin = i
            if (!isFirstLoop) break
          }
          if (nums[i] !== lastVal) allEqual = false
        }
        if (isFirstLoop) {
          if (allEqual) return lastVal > 0
          isFirstLoop = false
        }
        if (prevMin == null) return false
        if (prevMin === 0) return true
        endIdx = prevMin
    }
};
