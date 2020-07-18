// 226. 翻转二叉树 - 简单
// https://leetcode-cn.com/problems/invert-binary-tree/
// https://leetcode-cn.com/problems/invert-binary-tree/solution/go-di-gui-he-die-dai-by-ba-xiang-2/
// https://leetcode-cn.com/problems/invert-binary-tree/solution/golang-er-cha-shu-shi-bu-shi-du-shi-di-gui-by-bloo/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


// 2.1 迭代 - DFS - 双stack - 前序遍历
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 11.11% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    ans := &TreeNode{}
    stack1 := []*TreeNode{root}
    stack2 := []*TreeNode{ans}

    for len(stack1) > 0 {
        p1 := stack1[len(stack1)-1]
        stack1 = stack1[0:len(stack1)-1]
        p2 := stack2[len(stack2)-1]
        stack2 = stack2[0:len(stack2)-1]
        if p1 != nil {
            // 此处前序处理 p1.Val
            p2.Val = p1.Val
            if p1.Left != nil {
                stack1 = append(stack1, p1.Left)
                p2.Right = &TreeNode{}
                stack2 = append(stack2, p2.Right)
            }
            if p1.Right != nil {
                stack1 = append(stack1, p1.Right)
                p2.Left = &TreeNode{}
                stack2 = append(stack2, p2.Left)
            }
        }
    }
    return ans
}


// 2. 迭代 - DFS - 双stack - 中序遍历
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 11.11% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    ans := &TreeNode{}
    p1, p2 := root, ans
    stack1 := make([]*TreeNode, 0)
    stack2 := make([]*TreeNode, 0)

    for p1 != nil || len(stack1) > 0 {
        for p1 != nil {
            stack1 = append(stack1, p1)
            stack2 = append(stack2, p2)
            p1 = p1.Left
            if p1 != nil {
                p2.Right = &TreeNode{}
            }
            p2 = p2.Right  // 处理p2
        }
        p1 = stack1[len(stack1)-1]
        stack1 = stack1[0:len(stack1)-1]  // pop stack
        p2 = stack2[len(stack2)-1]
        stack2 = stack2[0:len(stack2)-1]  // pop stack
        // 此处中序处理 p1.Val
        p2.Val = p1.Val
        p1 = p1.Right
        if p1 != nil {
            p2.Left = &TreeNode{}
        }
        p2 = p2.Left  // 处理p2
    }
    return ans
}


// 2.1 迭代 - BFS - (2)
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 11.11% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return root
    }
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        head := queue[0]
        queue = queue[1:]
        head.Left, head.Right = head.Right, head.Left
        if head.Left != nil {
            queue = append(queue, head.Left)
        }
        if head.Right != nil {
            queue = append(queue, head.Right)
        }
    }
    return root
}


// 2. 迭代 - BFS - (1)
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 11.11% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return root
    }
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            node := queue[i]
            node.Left, node.Right = node.Right, node.Left
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        queue = queue[size:]
    }
    return root
}


// 1.2 递归 - 直接操作root - 前序遍历 (先处理 后递归)
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root==nil {// 递归结束条件
        return nil
    }
    // 当前需要一级需要做的是把 左节点指向右节点 右节点指向已经翻转的左节点
    temp := root.Left
    root.Left = root.Right
    root.Right = temp
    invertTree(root.Left) // 翻转的左节点
    invertTree(root.Right)// 返翻转的右节点
    return root
}


// 1.1 递归 - 直接操作root - 后序遍历 (先递归 后处理)
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root==nil {// 递归结束条件
        return nil
    }
    right:= invertTree(root.Right)// 返回已经翻转的右节点
    left := invertTree(root.Left) // 返回已经翻转的左节点
    // 当前需要一级需要做的是把 左节点指向已经翻转的右节点 右节点指向已经翻转的左节点
    root.Left = right
    root.Right = left
    return root
}


// 1. 递归 - 返回新对象
// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2.1 MB , 在所有 Go 提交中击败了 11.11% 的用户
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    p := TreeNode{}
    p.Val = root.Val
    p.Left = invertTree(root.Right)
    p.Right = invertTree(root.Left)
    return &p
}
