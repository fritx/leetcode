# 21. 合并两个有序链表 - 简单
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2. 迭代
# 执行用时： 44 ms , 在所有 Python3 提交中击败了 79.81% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 7.14% 的用户
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 else l2

        return head.next


# 1. 递归
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 33.30% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 7.14% 的用户
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
