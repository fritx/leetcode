// 爬楼梯
// https://leetcode-cn.com/problems/climbing-stairs/

// 动态规划 一维数组
// 执行用时 : 64 ms , 在所有 JavaScript 提交中击败了 71.20% 的用户
// 内存消耗 : 32.5 MB , 在所有 JavaScript 提交中击败了 100.00% 的用户
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let dp = [1, 1];
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
};
