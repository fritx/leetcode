# 剑指 Offer 22. 链表中倒数第k个节点
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 3. 递归+错误抛出
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/po-su-xiang-fa-shuang-zhi-zhen-di-gui-by-huang-da-/
# 执行用时： 32 ms , 在所有 Python3 提交中击败了 98.24% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ans = None

        def recurse(head: ListNode) -> None:
            nonlocal count, ans
            if not head:
                return
            recurse(head.next)
            count += 1
            if count == k:
                ans = head
                raise "terminate"

        try:
            recurse(head)
        except:
            pass

        return ans


# 2. 双指针 快慢指针 固定窗口
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 92.61% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


# 1. 笨方法 - list记录所有节点
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 79.47% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        lst = [head]
        while head.next:
            head = head.next
            lst.append(head)
        return lst[-k] if k <= len(lst) else None
