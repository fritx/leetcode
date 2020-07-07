# 124. 二叉树中的最大路径和
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 执行用时： 100 ms , 在所有 Python3 提交中击败了 87.29% 的用户
# 内存消耗： 21.1 MB , 在所有 Python3 提交中击败了 20.00% 的用户
class Solution:
    def __init__(self):
        self.ans = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def walk(node: TreeNode) -> int:
            if not node:
                return 0
            L = max(0, walk(node.left))
            R = max(0, walk(node.right))
            self.ans = max(self.ans, node.val + L + R)
            return max(node.val, node.val + L, node.val + R)

        walk(root)
        return self.ans
