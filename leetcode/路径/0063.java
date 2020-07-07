// 63. 不同路径 II - 中等
// https://leetcode-cn.com/problems/unique-paths-ii/

// 执行用时： 1 ms , 在所有 Java 提交中击败了 49.66% 的用户
// 内存消耗： 39.1 MB , 在所有 Java 提交中击败了 48.15% 的用户
class Solution {
  public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    int nrows = obstacleGrid.length;
    if (nrows == 0)
      return 0;
    int ncols = obstacleGrid[0].length;
    if (ncols == 0)
      return 0;

    int[][] dp = new int[nrows][ncols];
    for (int ir = 0; ir < nrows; ir++) {
      for (int ic = 0; ic < ncols; ic++) {
        if (obstacleGrid[ir][ic] == 1) { // 增设障碍判断 (优先级最高)
          dp[ir][ic] = 0;
        } else if (ir == 0 && ic == 0) {
          dp[ir][ic] = 1;
        } else {
          int prv = ir == 0 ? 0 : dp[ir - 1][ic];
          int pcv = ic == 0 ? 0 : dp[ir][ic - 1];
          dp[ir][ic] = prv + pcv;
        }
      }
    }
    return dp[nrows - 1][ncols - 1];
  }
}
