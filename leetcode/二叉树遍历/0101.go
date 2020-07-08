// 101. 对称二叉树
// https://leetcode-cn.com/problems/symmetric-tree/
// https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/

// 2. 方法二：迭代
// 执行用时： 4 ms , 在所有 Go 提交中击败了 74.85% 的用户
// 内存消耗： 3.1 MB , 在所有 Go 提交中击败了 28.57% 的用户
func isSymmetric(root *TreeNode) bool {
    u, v := root, root
    q := []*TreeNode{}
    q = append(q, u)
    q = append(q, v)
    for len(q) > 0 {
        u, v = q[0], q[1]
        q = q[2:]
        if u == nil && v == nil {
            continue
        }
        if u == nil || v == nil {
            return false
        }
        if u.Val != v.Val {
            return false
        }
        q = append(q, u.Left)
        q = append(q, v.Right)

        q = append(q, u.Right)
        q = append(q, v.Left)
    }
    return true
}


// 1. 方法一：递归
// 执行用时： 4 ms , 在所有 Go 提交中击败了 74.85% 的用户
// 内存消耗： 2.9 MB , 在所有 Go 提交中击败了 100.00% 的用户
func isSymmetric(root *TreeNode) bool {
    return check(root, root)
}

func check(p, q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    }
    if p == nil || q == nil {
        return false
    }
    return p.Val == q.Val && check(p.Left, q.Right) && check(p.Right, q.Left)
}
