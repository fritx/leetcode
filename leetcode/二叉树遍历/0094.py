# 94. 二叉树的中序遍历
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2. 迭代
# 执行用时: 12 ms , 在所有 Python 提交中击败了 98.00% 的用户
# 内存消耗: 12.6 MB , 在所有 Python 提交中击败了 7.14% 的用户
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack, curr = [], [], root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans


# 1. 递归
# 执行用时: 16 ms , 在所有 Python 提交中击败了 90.75% 的用户
# 内存消耗: 12.6 MB , 在所有 Python 提交中击败了 7.14% 的用户
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def walk(node):
            if not node:
                return
            walk(node.left)
            ans.append(node.val)
            walk(node.right)

        walk(root)
        return ans
