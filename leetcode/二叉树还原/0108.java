// 108. 将有序数组转换为二叉搜索树
// https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */

// 执行用时： 1 ms , 在所有 Java 提交中击败了 8.54% 的用户
// 内存消耗： 40 MB , 在所有 Java 提交中击败了 8.70% 的用户
class Solution {
  public TreeNode sortedArrayToBST(int[] nums) {
    if (nums.length == 0)
      return null;
    int mid = nums.length / 2;
    TreeNode midNode = new TreeNode(nums[mid]);
    midNode.left = mid > 0 ? sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid)) : null;
    midNode.right = nums.length > mid + 1 ? sortedArrayToBST(Arrays.copyOfRange(nums, mid + 1, nums.length)) : null;
    return midNode;
  }
}
