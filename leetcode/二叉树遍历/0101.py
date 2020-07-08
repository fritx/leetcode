# 101. 对称二叉树
# https://leetcode-cn.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1,2,2,3,4,4,3] - true
# [1,2,2,null,3,null,3] - false

# 1. bfs
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 89.67% 的用户
# 内存消耗： 13.9 MB , 在所有 Python3 提交中击败了 6.06% 的用户
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        curr_level = [root]

        while True:
            next_level = []

            for node in curr_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)

            if next_level:
                lst = list(map(lambda x: x.val if x else None, next_level))
                if lst != lst[::-1]:
                    return False
            else:
                break

            curr_level = next_level

        return True
