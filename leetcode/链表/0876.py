# 876. 链表的中间结点 - 简单
# https://leetcode-cn.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢指针
# 执行用时： 32 ms , 在所有 Python3 提交中击败了 93.03% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 14.29% 的用户
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


# 单指针法
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 60.31% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 14.29% 的用户
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p, n = head, 0
        while p:
            p, n = p.next, n + 1
        p, n = head, n // 2
        while n:
            p = p.next
            n = n - 1
        return p
