// 160. 相交链表 - 简单
// https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


// 3. 方法三：双指针法
// https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/60msgo-shi-xian-by-elliotxx/
// 执行用时： 44 ms , 在所有 Go 提交中击败了 89.55% 的用户
// 内存消耗： 6.8 MB , 在所有 Go 提交中击败了 100.00% 的用户
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    pA, pB := headA, headB
    // 如果第一次遍历到链表尾部，就指向另一个链表的头部，继续遍历，这样会抵消长度差。
    // 如果没有相交，因为遍历长度相等，最后会是 nil ==  nil
    for pA != pB {
        if pA == nil {
            pA = headB
        } else {
            pA = pA.Next
        }
        if pB == nil {
            pB = headA
        } else {
            pB = pB.Next
        }
    }
    return pA
}

// 2. 方法二: 哈希表法
// https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/ha-xi-biao-fa-by-dylanhan8/
// 执行用时： 48 ms , 在所有 Go 提交中击败了 70.38% 的用户
// 内存消耗： 6.7 MB , 在所有 Go 提交中击败了 100.00% 的用户
func getIntersectionNode(headA, headB *ListNode) *ListNode {
   mapInterface := make(map[interface{}]interface{})
   for headA != nil {
       mapInterface[headA] = 1
       headA = headA.Next
   }
   for headB != nil {
       if mapInterface[headB] == 1 {
           return headB
        }
        headB = headB.Next
   }
   return nil
}


// 1. 方法一: 暴力法 - 双重比对
// 执行用时： 488 ms , 在所有 Go 提交中击败了 5.32% 的用户
// 内存消耗： 6.2 MB , 在所有 Go 提交中击败了 100.00% 的用户
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    for headA != nil {
        pb := headB
        for pb != nil {
            if pb == headA {
                return pb
            }
            pb = pb.Next
        }
        headA = headA.Next
    }
    return nil
}
