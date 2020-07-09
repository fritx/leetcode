# 23. 合并K个排序链表 - 困难
# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 3. 分治合并
# 执行用时： 152 ms , 在所有 Python3 提交中击败了 27.04% 的用户
# 内存消耗： 16.5 MB , 在所有 Python3 提交中击败了 25.00% 的用户
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[ListNode], L: int, R: int) -> ListNode:
        if L == R:
            return lists[L]
        mid = (L + R) // 2
        return self.mergeTwoLists(self.merge(lists, L, mid), self.merge(lists, mid + 1, R))

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


# 2. 顺序合并
# 执行用时： 4984 ms , 在所有 Python3 提交中击败了 8.08% 的用户
# 内存消耗： 16.6 MB , 在所有 Python3 提交中击败了 10.71% 的用户
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = lists[0] if lists else None
        for i in range(1, len(lists)):
            ans = self.mergeTwoLists(ans, lists[i])
        return ans

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


# 归并 - 超时
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans, curr, last = None, None, None
        while True:
            mininfo = [None, None]
            for i, node in enumerate(lists):
                if node and (not mininfo[1] or node.val < mininfo[1].val):
                    mininfo = [i, node]
            if mininfo[0] is None:
                break
            else:
                lists[mininfo[0]] = lists[mininfo[0]].next
                if not lists[mininfo[0]]:
                    lists = lists[0:mininfo[0]] + lists[mininfo[0] + 1:]
                curr = mininfo[1]
                if ans:
                    last.next = curr
                else:
                    ans = curr
                last = curr
        return ans
