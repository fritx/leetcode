// 1290. 二进制链表转整数
// https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


// 执行用时： 0 ms , 在所有 Go 提交中击败了 100.00% 的用户
// 内存消耗： 2 MB , 在所有 Go 提交中击败了 100.00% 的用户
func getDecimalValue(head *ListNode) int {
    ans := 0
    for {
        ans = ans * 2 + head.Val
        head = head.Next
        if head == nil {
            break
        }
    }
    return ans
}
