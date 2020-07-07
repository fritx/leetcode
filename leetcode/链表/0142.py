# 142. 环形链表 II
# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 2. 哈希表
# 执行用时： 56 ms , 在所有 Python3 提交中击败了 93.48% 的用户
# 内存消耗： 17.1 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        st = set()
        while head:
            if head in st:
                return head
            st.add(head)
            head = head.next
        return None


# 1. 快慢指针 - s1 + a = a + b - Floyd 算法
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 99.41% 的用户
# 内存消耗： 16.8 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        hasCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                hasCycle = True
                break
        if not hasCycle:  # 不存在环形
            return None

        curr = head  # 存在环形
        while slow != curr:
            slow = slow.next
            curr = curr.next
        return curr
