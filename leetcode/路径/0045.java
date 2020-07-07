// 45. 跳跃游戏 II - 困难
// https://leetcode-cn.com/problems/jump-game-ii/

class Solution {
  public int jump(int[] nums) {
    int len = nums.length;
    if (len <= 1) {
      // 如果长度为小于1，直接到达
      return 0;
    }

    // 每一次起跳的起点
    int index = 0;
    // 每一次起跳的终点
    int max = nums[0];
    // 跳到终点的最小步数，至少有一步
    int step = 1;

    while (max < len - 1) {
      // 循环获取 index->max 区间每个点可以到达的最远位置，其中最大的那个点就可以作为下一次的起点
      int curMax = 0;
      for (int i = index + 1; i <= max; i++) {
        if (i + nums[i] > curMax) {
          // 当前点可以到达的最远距离更长
          curMax = i + nums[i];
          index = i;
        }
      }
      // 从当前起点可以到达的终点位置
      max = index + nums[index];
      // 步数加一
      step++;
    }
    return step;
  }
}
