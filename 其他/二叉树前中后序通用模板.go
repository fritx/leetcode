// 二叉树前中后序遍历-通用模板
// 出处 https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/mo-fang-di-gui-zhi-bian-yi-xing-by-sonp/
func universalOrderTraverse(root *TreeNode) []int {
    if root == nil {
        return []
    }
    ans, stack := [], [root]
    for len(stack) > 0 {
        p := stack[len(stack)-1]
        stack = stack[0:len(stack)-1]
        if p == nil {
            p = stack[len(stack)-1]
            stack = stack[0:len(stack)-1]
            ans = append(ans, p.Val)  // 遍历要做的动作在这里
        } else {
            // left,right 先append的后遍历 (stack缘故)
            if p.Right != nil {
                stack = append(stack, p.Right)
            }
            if p.Left != nil {
                stack = append(stack, p.Left)
            }
            // 根据前中后序需要 调节一下两行语句的位置
            // 如放最底为前序 放最顶为后序 放left,right之间为中序
            stack = append(stack, p)
            stack = append(stack, nil)
        }
    }
    return ans
}
