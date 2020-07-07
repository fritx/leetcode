# 206. 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 3. 官方 方法二：递归
# 执行用时： 60 ms , 在所有 Python3 提交中击败了 12.93% 的用户
# 内存消耗： 18.5 MB , 在所有 Python3 提交中击败了 5.88% 的用户
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# 2. 官方 方法一：迭代
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 89.72% 的用户
# 内存消耗： 14.4 MB , 在所有 Python3 提交中击败了 20.59% 的用户
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev


# 1. 迭代
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 30.59% 的用户
# 内存消耗： 14.7 MB , 在所有 Python3 提交中击败了 17.65% 的用户
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            tmp = head
            head = head.next
            tmp.next = ans
            ans = tmp
        return ans
