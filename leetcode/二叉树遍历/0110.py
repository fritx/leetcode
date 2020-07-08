# 110. 平衡二叉树 - 简单
# https://leetcode-cn.com/problems/balanced-binary-tree/
# https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [3,9,20,null,null,15,7] - true
# [1,2,2,3,3,null,null,4,4] - false
# [1,null,2,null,3] - false
# [1,2,2,3,null,null,3,4,null,null,4] - false


# 3. 官方解 - 方法二：自底向上的递归
class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


# 2. 递归 - getDepth也改为递归
# 官方解 - 方法一：自顶向下的递归
# 执行用时： 76 ms , 在所有 Python3 提交中击败了 45.45% 的用户
# 内存消耗： 17.5 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 定义：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
        if not root:
            return True
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))


# 1.1 - 暴力递归 - 结合memo weakMap - todo

# 1. 暴力递归
# 执行用时： 112 ms , 在所有 Python3 提交中击败了 5.54% 的用户
# 内存消耗： 18.5 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 定义：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
        if not root:
            return True
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

    def getDepth(self, root: TreeNode) -> int:
        curr_d, max_d = 0, 0

        def recurse(curr: TreeNode) -> None:
            if not curr:
                return
            nonlocal curr_d, max_d
            curr_d += 1
            max_d = max(max_d, curr_d)
            recurse(curr.left)
            recurse(curr.right)
            curr_d -= 1

        recurse(root)
        return max_d
