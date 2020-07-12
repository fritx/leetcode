// 543. 二叉树的直径 - 简单
// https://leetcode-cn.com/problems/diameter-of-binary-tree/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


// 1. dfs
// 执行用时： 4 ms , 在所有 Go 提交中击败了 93.81% 的用户
// 内存消耗： 4.5 MB , 在所有 Go 提交中击败了 100.00% 的用户
func diameterOfBinaryTree(root *TreeNode) int {
    ans := 0
    dfs(root, &ans)
    return ans
}

func dfs(root *TreeNode, ans *int) int {
    if root == nil {
        return 0
    }
    l := dfs(root.Left, ans)
    r := dfs(root.Right, ans)
    *ans = max(*ans, l + r)
    return 1 + max(l, r)
}

func max(x int, y int) int {
    if (x > y) {
        return x
    }
    return y
}
