# 145. 二叉树的后序遍历
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2. 迭代
# 执行用时: 16 ms , 在所有 Python 提交中击败了 88.59% 的用户
# 内存消耗: 12.8 MB , 在所有 Python 提交中击败了 16.67% 的用户
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return ans[::-1]  # 逆序


# 1. 递归
# 执行用时: 24 ms , 在所有 Python 提交中击败了 45.22% 的用户
# 内存消耗: 12.8 MB , 在所有 Python 提交中击败了 16.67% 的用户
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def walk(node):
            if not node:
                return
            walk(node.left)
            walk(node.right)
            ans.append(node.val)
        walk(root)
        return ans
