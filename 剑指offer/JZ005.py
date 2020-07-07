# -*- coding:utf-8 -*-

# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6


class Stack:
    def __init__(self):
        self.lst = []

    def push(self, node):
        self.lst.append(node)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class Solution:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, node):
        # write code here
        self.stack_in.push(node)

    def pop(self):
        # return xx
        if not self.size():
            raise IndexError("list index out of range")
        if self.stack_out.size():
            return self.stack_out.pop()
        else:
            while self.stack_in.size():
                self.stack_out.push(self.stack_in.pop())
            return self.stack_out.pop()

    def size(self):
        return self.stack_in.size() + self.stack_out.size()
