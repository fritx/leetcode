# 112. 路径总和 - 简单
# https://leetcode-cn.com/problems/path-sum/
# https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] - 1 - true
# [] - 0 - false
# [1, 2, null, 3, null, 4, null, 5] - 6 - false

# 3. 官方解 - 方法二：广度优先搜索
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False


# 2. 官方解 - 方法一：纯递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# 1. 暴力递归 + 异常终端
# 执行用时： 56 ms , 在所有 Python3 提交中击败了 63.74% 的用户
# 内存消耗： 15.5 MB , 在所有 Python3 提交中击败了 6.67% 的用户
class Solution:
    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        ans, stack = False, []

        def recurse(curr: TreeNode) -> None:
            nonlocal ans
            if not curr:
                return
            stack.append(curr.val)
            if not curr.left and not curr.right:
                if sum(stack) == summ:
                    ans = True
                    raise "finish"
            recurse(curr.left)
            recurse(curr.right)
            stack.pop()

        try:
            recurse(root)
        except:
            pass

        return ans
