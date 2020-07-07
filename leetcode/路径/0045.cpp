// 45. 跳跃游戏 II - 困难
// https://leetcode-cn.com/problems/jump-game-ii/

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> f(n);
        for (int i = 0, last = 0; i < n; i++) {
            if (!i) f[i] = 0;
            else {
                while (last < n && last + nums[last] < i) last++; // 找到第一个能跳到i的点last
                f[i] = f[last] + 1; // 使用点last更新f[i]
            }
        }
        return f[n - 1];
    }
};
