// 315. 计算右侧小于当前元素的个数 - 困难
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
// https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/ji-suan-you-ce-xiao-yu-dang-qian-yuan-su-de-ge-s-7/


// 1. 方法一：离散化树状数组
// 执行用时： 312 ms , 在所有 C# 提交中击败了 12.50% 的用户
// 内存消耗： 33.4 MB , 在所有 C# 提交中击败了 100.00% 的用户
public class Solution
{
    private int[] c;

    private int[] a;

    private void Init(int length)
    {
        c = new int[length];
        Array.Fill(c, 0);
    }

    private int LowBit(int x)
    {
        return x & (-x);
    }

    private void Update(int pos)
    {
        while (pos < c.Length)
        {
            c[pos] += 1;
            pos += LowBit(pos);
        }
    }

    private int Query(int pos)
    {
        int ret = 0;
        while (pos > 0)
        {
            ret += c[pos];
            pos -= LowBit(pos);
        }

        return ret;
    }

    private void Discretization(int[] nums)
    {
        a = (int[])nums.Clone();
        var hashSet = new HashSet<int>(a);
        a = hashSet.ToArray();
        Array.Sort(a);
    }

    private int GetId(int x)
    {
        return Array.BinarySearch(a, x) + 1;
    }

    public IList<int> CountSmaller(int[] nums)
    {
        var resultList = new List<int>();

        Discretization(nums);

        Init(nums.Length + 5);

        for (int i = nums.Length - 1; i >= 0; --i)
        {
            var id = GetId(nums[i]);
            resultList.Add(Query(id - 1));
            Update(id);
        }

        resultList.Reverse();

        return resultList;
    }
}
