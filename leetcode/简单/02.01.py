# 面试题 02.01. 移除重复节点
# https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
# https://leetcode-cn.com/problems/remove-duplicate-node-lcci/solution/yi-chu-zhong-fu-jie-dian-by-leetcode-solution/

# 示例1:
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]

# 示例2:
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]

# 提示：
# 链表长度在[0, 20000]范围内。
# 链表元素在[0, 20000]范围内。

# 进阶：
# 如果不得使用临时缓冲区，该怎么解决？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2. 官方解 - 方法二：两重循环
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        ob = head
        while ob:
            oc = ob
            while oc.next:
                if oc.next.val == ob.val:
                    oc.next = oc.next.next
                else:
                    oc = oc.next
            ob = ob.next
        return head


# 2. 官方解 - 方法一：哈希表 (集合Set)
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head
