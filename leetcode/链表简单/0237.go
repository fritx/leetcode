// 237. 删除链表中的节点 - 简单
// https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


// 执行用时： 4 ms , 在所有 Go 提交中击败了 71.81% 的用户
// 内存消耗： 2.9 MB , 在所有 Go 提交中击败了 33.33% 的用户
func deleteNode(node *ListNode) {
    node.Val = node.Next.Val
    node.Next = node.Next.Next
}
