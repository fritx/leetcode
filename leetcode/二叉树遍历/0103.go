// 103. 二叉树的锯齿形层次遍历 - 中等
// https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

// 模拟数组的unshift等操作 - [译]Go Slice 秘籍
// https://colobu.com/2017/03/22/Slice-Tricks/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// [3,9,20,null,null,15,7] - [[3],[20,9],[15,7]]
// [1,2,3,4,null,null,5] - [[1],[3,2],[4,5]]


// 2. 方法二：DFS （深度优先遍历）
// 时间复杂度：O(N)，其中 N 是树中节点的数量。
// 空间复杂度：O(H)=O(logN)，其中 H 是树的高度。


// 1. 方法一：BFS（广度优先遍历）
// 时间复杂度：O(N)，其中 N 是树中节点的数量。
// 空间复杂度：O(N)，其中 N 是树中节点的数量。
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.7 MB , 在所有 Go 提交中击败了 33.33% 的用户
func zigzagLevelOrder(root *TreeNode) [][]int {
    ans, queue, step := [][]int{}, []*TreeNode{}, 1
    if root != nil {
        queue = append(queue, root)
    }
    for len(queue) > 0 {
        next_queue := []*TreeNode{}
        row := []int{}
        for i := 0; i < len(queue); i++ {
            node := queue[i]
            if step == 1 {
                row = append(row, node.Val)
            } else {
                row = append([]int{node.Val}, row...)
            }
            if node.Left != nil {
                next_queue = append(next_queue, node.Left)
            }
            if node.Right != nil {
                next_queue = append(next_queue, node.Right)
            }
        }
        ans = append(ans, row)
        queue = next_queue  // 替换下一层queue
        step = -step  // 访问方向反转
    }
    return ans
}
