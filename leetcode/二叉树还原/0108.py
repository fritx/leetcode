# 108. 将有序数组转换为二叉搜索树
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 3. wip 迭代
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        leftarr = nums[0:mid]
        rightarr = nums[mid + 1:]

        midnode = TreeNode(nums[mid])
        midnode.left = self.sortedArrayToBST(leftarr)
        midnode.right = self.sortedArrayToBST(rightarr)

        return midnode


# 2. 官方解 递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


# 1. 递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        leftarr = nums[0:mid]
        rightarr = nums[mid + 1:]

        midnode = TreeNode(nums[mid])
        midnode.left = self.sortedArrayToBST(leftarr)
        midnode.right = self.sortedArrayToBST(rightarr)

        return midnode
