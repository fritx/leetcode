// 203. 移除链表元素 - 简单
// https://leetcode-cn.com/problems/remove-linked-list-elements/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


// 2.
// 执行用时： 8 ms , 在所有 Go 提交中击败了 90.66% 的用户
// 内存消耗： 4.7 MB , 在所有 Go 提交中击败了 75.00% 的用户
func removeElements(head *ListNode, val int) *ListNode {
    sentinel := &ListNode{Next: head}
    prev, curr := sentinel, head
    for ; curr != nil; curr = curr.Next {
        // fmt.Println(curr.Next.Val, val)
        if curr.Val == val {
            prev.Next = curr.Next
        } else {
            prev = curr
        }
    }
    return sentinel.Next
}


// 1.
// 执行用时： 8 ms , 在所有 Go 提交中击败了 90.66% 的用户
// 内存消耗： 4.7 MB , 在所有 Go 提交中击败了 75.00% 的用户
func removeElements(head *ListNode, val int) *ListNode {
    pre := &ListNode{Next: head}
    for curr := pre; curr.Next != nil; {
        // fmt.Println(curr.Next.Val, val)
        if curr.Next.Val == val {
            curr.Next = curr.Next.Next
        } else {
            curr = curr.Next
        }
    }
    return pre.Next
}
