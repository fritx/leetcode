// 15. 三数之和 中等
// input [-1, 0, 1, 2, -1, -4]
// output [
//   [-1, 0, 1],
//   [-1, -1, 2]
// ]

// 4.
// 作者：hzj
// 链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-chao-guo-989-yong-hu-by-hzj/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
// 执行用时 : 168 ms , 在所有 JavaScript 提交中击败了 87.04% 的用户
// 内存消耗 : 46.3 MB , 在所有 JavaScript 提交中击败了 100.00% 的用户
var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b);
  let res = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i >= 1 && nums[i] === nums[i - 1]) {
      continue;
    }
    let j = i + 1;
    let k = nums.length - 1;
    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];
      if (sum === 0) {
        res.push([nums[i], nums[j], nums[k]]);
        j++;
        while (nums[j - 1] === nums[j]) {
          j++;
        }
      } else if (sum < 0) {
        j++;
      } else {
        k--;
      }
    }
  }
  return res;
};

// 3. 左右指针
// 作者：royal029
// 链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-jszuo-you-zhi-zhen-by-royal029/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
// 执行用时 : 156 ms , 在所有 JavaScript 提交中击败了 93.87% 的用户
// 内存消耗 : 46.6 MB , 在所有 JavaScript 提交中击败了 100.00% 的用户
var threeSum = function (nums) {
  // 从小到大排序
  nums = nums.sort((a, b) => a - b);
  let result = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break; // 最小数字如果大于0，则后面不会有和为0的组

    if (i > 0 && nums[i] === nums[i - 1]) continue; // 跳过相同的数字
    // 其中，nums[i]是最小的数字，nums[k]是最大的数字
    let j = i + 1;
    let k = nums.length - 1;

    // 第二个数的索引不能超过第三个数的索引
    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];
      if (sum > 0) {
        // 如果结果大于0，那么最大的数字索引减一，寻找更小的数字
        do {
          k--;
        } while (nums[k] === nums[k + 1]); // 跳过相同的数字
      } else {
        // 如果结果等于0，加入数组
        if (!sum) result.push([nums[i], nums[j], nums[k]]);
        // 如果结果不大于0，那么次大的数字索引加一，寻找更大的数字
        do {
          j++;
        } while (nums[j] === nums[j - 1]); // 跳过相同的数字
      }
    }
  }
  return result;
};

// 2. 两两对比
// 执行结果: 通过 JS-228ms
let threeSum = function (nums) {
  let target = 0;
  let ans = [];
  let countHash = {};
  nums.sort(); // 排序整理
  for (let i = 0; i < nums.length; i++) {
    countHash[nums[i]] = (countHash[nums[i]] || 0) + 1; // 每个元素计数
  }
  let last;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === last) continue; // 去重
    last = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      // 两层循环 两两比对
      let left = target - (nums[i] + nums[j]);
      if (left < nums[i] || left < nums[j]) continue; // 去重
      if (left === nums[i]) continue; // 去重
      if (countHash[left] != null) {
        // 如果第三个数存在
        let remaining = countHash[left];
        if (nums[i] === left) remaining--;
        if (nums[j] === left) remaining--;
        if (remaining > 0) {
          ans.push([nums[i], nums[j], left]);
        }
      }
    }
  }
  return ans;
};

// 1. 暴力法
// 执行结果: 超时
let threeSum = function (nums) {
  let ans = [];
  let len = nums.length;
  let sum = 0;
  let exists = {};
  for (let i = 0; i < len; i++) {
    let curr = nums[i];
    if (exists[curr]) continue;
    exists[curr] = 1;
    let leftSum = sum - curr;
    let leftNums = nums.slice(0, i).concat(nums.slice(i + 1));
    let leftAns = twoSum(leftNums, leftSum);
    for (let j = 0; j < leftAns.length; j++) {
      let row = [curr, ...leftAns[j]].sort();
      let duplicated = false;
      for (let k = 0; k < ans.length; k++) {
        if (ans[k].toString() === row.toString()) {
          duplicated = true;
          break;
        }
      }
      if (!duplicated) ans.push(row);
    }
  }
  return ans.sort();
};

let twoSum = function (nums, sum) {
  let ans = [];
  let len = nums.length;
  let hash = {};
  for (let i = 0; i < len; i++) {
    let curr = nums[i];
    let left = hash[curr];
    if (left == null) {
      left = sum - curr;
      hash[left] = curr;
    } else {
      ans.push([left, curr]);
    }
  }
  return ans;
};
