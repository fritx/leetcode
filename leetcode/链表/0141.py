# 141. 环形链表
# https://leetcode-cn.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2. 快慢指针
# 执行用时： 72 ms , 在所有 Python3 提交中击败了 27.25% 的用户
# 内存消耗： 16.5 MB , 在所有 Python3 提交中击败了 9.52% 的用户
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


# 1. 哈希表 集合
# 执行用时： 76 ms , 在所有 Python3 提交中击败了 21.94% 的用户
# 内存消耗： 17.2 MB , 在所有 Python3 提交中击败了 9.52% 的用户
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        st = set()

        while head:
            if head in st:
                return True
            st.add(head)
            head = head.next

        return False
