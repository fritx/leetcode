# 234. 回文链表
# https://leetcode-cn.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 3. 快慢指针 + 翻转后半段
# 执行用时： 92 ms , 在所有 Python3 提交中击败了 39.24% 的用户
# 内存消耗： 23.9 MB , 在所有 Python3 提交中击败了 25.00% 的用户
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        first_half_end = self.end_of_first_start(head)
        second_half_start = self.reverseList(first_half_end)

        while second_half_start is not None:
            if head.val != second_half_start.val:
                return False
            second_half_start = second_half_start.next
            head = head.next

        return True

    def end_of_first_start(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            tmp = head
            head = head.next
            tmp.next = ans
            ans = tmp
        return ans


# 2. 递归
# 执行用时： 100 ms , 在所有 Python3 提交中击败了 25.63% 的用户
# 内存消耗： 76 MB , 在所有 Python3 提交中击败了 5.00% 的用户
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        front = head

        def recurse(curr: ListNode) -> bool:
            nonlocal front
            if not curr:
                return True
            if not recurse(curr.next):
                return False
            if curr.val != front.val:
                return False
            front = front.next
            return True

        return recurse(head)


# 1. 维护数组
# 执行用时： 100 ms , 在所有 Python3 提交中击败了 25.63% 的用户
# 内存消耗： 23.8 MB , 在所有 Python3 提交中击败了 25.00% 的用户
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i, j = 0, len(arr) - 1

        # opt 1.
        # while i < j:
        #     if arr[i] != arr[j]:
        #         return False
        #     i, j = i + 1, j - 1
        # return True

        # opt 2.
        return arr == arr[::-1]
