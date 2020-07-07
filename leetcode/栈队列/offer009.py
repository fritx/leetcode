# 剑指 Offer 09. 用两个栈实现队列
# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

# [1, 2, 3, 4, 5]
# st1 [1, 2, 3]
# st2 [3, 2, 1]

# 2. 直接使用builtin list数据结构
# 执行用时： 608 ms , 在所有 Python3 提交中击败了 47.81% 的用户
# 内存消耗： 16.9 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class CQueue:
    def __init__(self):
        self.st1, self.st2 = [], []

    def appendTail(self, value: int) -> None:
        self.st1.append(value)

    def deleteHead(self) -> int:
        if not self.st2:
            while self.st1:
                elem = self.st1.pop()
                self.st2.append(elem)
        return self.st2.pop() if self.st2 else -1


# 1. 自实现Stack类
# 执行用时： 836 ms , 在所有 Python3 提交中击败了 23.87% 的用户
# 内存消耗： 17.2 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Stack:
    def __init__(self):
        self.lst = []

    def push(self, value: int) -> None:
        self.lst.append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise "out of range"
        return self.lst.pop()

    def is_empty(self) -> bool:
        return not self.lst


class CQueue:
    def __init__(self):
        self.st1, self.st2 = Stack(), Stack()

    def appendTail(self, value: int) -> None:
        self.st1.push(value)

    def deleteHead(self) -> int:
        if self.st2.is_empty():
            while not self.st1.is_empty():
                elem = self.st1.pop()
                self.st2.push(elem)
        return -1 if self.st2.is_empty() else self.st2.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
