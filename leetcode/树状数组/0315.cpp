// 315. 计算右侧小于当前元素的个数 - 困难
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/


// 2. by newhar
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> b(nums.begin(), nums.end());
        sort(b.begin(),b.end());
        b.erase(unique(b.begin(),b.end()),b.end());

        vector<int> res(nums.size()), sz(4*b.size(),0);

        for(int i = (int)nums.size()-1; i >= 0; --i) {
            int l = 0, r = (int)b.size()-1, node = 1;
            while(l < r) {
                sz[node]++;
                int mid = (l+r+1) >> 1;
                if(nums[i] >= b[mid]) {
                    res[i] += sz[node<<1], node = (node<<1)|1, l = mid;
                } else {
                    node <<= 1, r = mid - 1;
                }
            }
            sz[node]++;
        }
        return res;
    }
};


// 1. 方法一：离散化树状数组
// 执行用时： 32 ms , 在所有 C++ 提交中击败了 69.63% 的用户
// 内存消耗： 10.3 MB , 在所有 C++ 提交中击败了 100.00% 的用户
class Solution {
private:
    vector<int> c;
    vector<int> a;

    void Init(int length) {
        c.resize(length, 0);
    }

    int LowBit(int x) {
        return x & (-x);
    }

    void Update(int pos) {
        while (pos < c.size()) {
            c[pos] += 1;
            pos += LowBit(pos);
        }
    }

    int Query(int pos) {
        int ret = 0;

        while (pos > 0) {
            ret += c[pos];
            pos -= LowBit(pos);
        }

        return ret;
    }

    void Discretization(vector<int>& nums) {
        a.assign(nums.begin(), nums.end());
        sort(a.begin(), a.end());
        a.erase(unique(a.begin(), a.end()), a.end());
    }

    int getId(int x) {
        return lower_bound(a.begin(), a.end(), x) - a.begin() + 1;
    }
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> resultList;

        Discretization(nums);

        Init(nums.size() + 5);

        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            int id = getId(nums[i]);
            resultList.push_back(Query(id - 1));
            Update(id);
        }

        reverse(resultList.begin(), resultList.end());

        return resultList;
    }
};
