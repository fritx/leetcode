# 144. 二叉树的前序遍历
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 4. 前序-中序-后序 通用模板
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/mo-fang-di-gui-zhi-bian-yi-xing-by-sonp/
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            p = stack.pop()
            if p is None:
                p = stack.pop()
                result.append(p.val)
            else:
                if p.right:
                    stack.append(p.right)  # 先append的最后访问
                if p.left:
                    stack.append(p.left)
                stack.append(p)
                stack.append(None)
            return result


# 3. 莫里斯遍历 - 出返回值外 空间O(1)
# 作者：LeetCode
# 链接：https: // leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 执行用时: 16 ms , 在所有 Python 提交中击败了 88.80% 的用户
# 内存消耗: 12.6 MB , 在所有 Python 提交中击败了 5.56% 的用户
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left

                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right

        return output


# 2. 迭代
# 执行用时: 28 ms , 在所有 Python 提交中击败了 16.30% 的用户
# 内存消耗: 13 MB , 在所有 Python 提交中击败了 5.56% 的用户
class Solution(object):
    def preorderTraversal(self, root):
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
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return ans


# 1. 递归
# 执行用时: 20 ms , 在所有 Python 提交中击败了 69.51% 的用户
# 内存消耗: 12.7 MB , 在所有 Python 提交中击败了 5.56% 的用户
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def walk(node):
            if not node:
                return
            ans.append(node.val)
            walk(node.left)
            walk(node.right)

        walk(root)
        return ans
