
// 爬楼梯
// https://leetcode-cn.com/problems/climbing-stairs/

// 2. 动态规划 滚动数组 (只保留3个变量)
class Solution {
  public int climbStairs(int n) {
    // ...
  }
}

// 1. 动态规划 一维数组
// 执行用时 : 0 ms , 在所有 Java 提交中击败了 100.00% 的用户
// 内存消耗 : 36.1 MB , 在所有 Java 提交中击败了 5.66% 的用户
class Solution {
  public int climbStairs(int n) {
    int[] dp = new int[n + 1];
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; i++)
      dp[i] = dp[i - 1] + dp[i - 2];
    return dp[n];
  }
}
