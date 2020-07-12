// 174. 地下城游戏 - 困难
// https://leetcode-cn.com/problems/dungeon-game/
// https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/

// 1. 方法一：动态规划
// 执行用时： 3 ms , 在所有 Java 提交中击败了 41.26% 的用户
// 内存消耗： 39.1 MB , 在所有 Java 提交中击败了 100.00% 的用户
class Solution {
  public int calculateMinimumHP(int[][] dungeon) {
    int n = dungeon.length, m = dungeon[0].length;
    int[][] dp = new int[n + 1][m + 1];
    for (int i = 0; i <= n; ++i) {
      Arrays.fill(dp[i], Integer.MAX_VALUE);
    }
    dp[n][m - 1] = dp[n - 1][m] = 1;
    for (int i = n - 1; i >= 0; --i) {
      for (int j = m - 1; j >= 0; --j) {
        int minn = Math.min(dp[i + 1][j], dp[i][j + 1]);
        dp[i][j] = Math.max(minn - dungeon[i][j], 1);
      }
    }
    return dp[0][0];
  }
}
