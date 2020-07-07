# 104. 二叉树的最大深度
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 3. dfs 迭代
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/cde-san-chong-fang-fa-shi-xian-you-zhu-jie-by-zzxh/
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 74.24% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans, d, p, stack = 0, 0, root, []
        while p or stack:
            while p:
                d += 1
                stack.append((p, d))
                p = p.left
            p, d = stack[-1]
            ans = max(ans, d)
            stack.pop()
            p = p.right
        return ans


# 2.1 官方解 - dfs 递归 极简
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 2. 自解 - dfs 递归
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 89.38% 的用户
# 内存消耗： 15.9 MB , 在所有 Python3 提交中击败了 5.55% 的用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans, curr = 0, 0

        def dfs(node: TreeNode) -> None:
            nonlocal ans, curr
            if not node:
                return
            curr += 1
            ans = max(ans, curr)
            dfs(node.right)
            dfs(node.left)
            curr -= 1

        dfs(root)
        return ans


# 1. 自解 - bfs 迭代
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 89.38% 的用户
# 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 5.55% 的用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue, depth = [], 0
        if root:
            queue.append(root)
        while queue:
            depth += 1
            queue_next = []
            for node in queue:
                if node.left:
                    queue_next.append(node.left)
                if node.right:
                    queue_next.append(node.right)
            queue = queue_next
        return depth
