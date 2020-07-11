// 315. 计算右侧小于当前元素的个数 - 困难
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


// 1. 方法一：离散化树状数组
// 执行用时： 32 ms , 在所有 C 提交中击败了 95.01% 的用户
// 内存消耗： 9 MB , 在所有 C 提交中击败了 100.00% 的用户
int LowBit(int x) { return x & (-x); }

void Update(int* c, int n, int pos) {
    while (pos < n) {
        c[pos] += 1;
        pos += LowBit(pos);
    }
}

int Query(int* c, int n, int pos) {
    int ret = 0;

    while (pos > 0) {
        ret += c[pos];
        pos -= LowBit(pos);
    }

    return ret;
}

int lower_bound(int* a, int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (a[mid] < x) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}

int comp(const void* a, const void* b) { return (*(int*)a - *(int*)b); }

int Discretization(int* a, int* nums, int n) {
    memcpy(a, nums, sizeof(int) * n);
    qsort(a, n, sizeof(int), comp);
    int m = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[m]) {
            a[++m] = a[i];
        }
    }
    return m + 1;
}
int* countSmaller(int* nums, int numsSize, int* returnSize) {
    int* a = (int*)malloc(sizeof(int) * numsSize);
    int* c = (int*)malloc(sizeof(int) * (numsSize + 1));
    int* ret = (int*)malloc(sizeof(int) * numsSize);
    memset(a, 0, sizeof(int) * numsSize);
    memset(c, 0, sizeof(int) * (numsSize + 1));
    memset(ret, 0, sizeof(int) * numsSize);

    int m = Discretization(a, nums, numsSize);
    for (int i = numsSize - 1; i >= 0; --i) {
        int id = lower_bound(a, m, nums[i]) + 1;
        ret[i] = Query(c, m + 1, id - 1);
        Update(c, m + 1, id);
    }
    free(a);
    free(c);
    *returnSize = numsSize;
    return ret;
}
