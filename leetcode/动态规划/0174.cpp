// 174. 地下城游戏 - 困难
// https://leetcode-cn.com/problems/dungeon-game/
// https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/

// 1. 方法一：动态规划
// 执行用时： 20 ms , 在所有 C++ 提交中击败了 13.59% 的用户
// 内存消耗： 9 MB , 在所有 C++ 提交中击败了 100.00% 的用户
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int n = dungeon.size(), m = dungeon[0].size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MAX));
        dp[n][m - 1] = dp[n - 1][m] = 1;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                int minn = min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = max(minn - dungeon[i][j], 1);
            }
        }
        return dp[0][0];
    }
};
