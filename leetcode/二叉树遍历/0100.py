# 100. 相同的树
# https://leetcode-cn.com/problems/same-tree/submissions/
# https://leetcode-cn.com/problems/same-tree/solution/xiang-tong-de-shu-by-leetcode/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 2. 方法二：迭代
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 47.94% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 7.14% 的用户
from collections import deque  # leetcode中可省略


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p: TreeNode, q: TreeNode) -> bool:
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True


# 1. 方法一：递归
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 22.65% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 7.14% 的用户
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val \
                and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)

        return not p and not q
