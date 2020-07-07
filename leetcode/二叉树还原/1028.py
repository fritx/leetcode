# 1028. 从先序遍历还原二叉树
# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x: int):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# 3. dfs递归 - by dijks
# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/
# 执行用时： 88 ms , 在所有 Python3 提交中击败了 79.28% 的用户
# 内存消耗： 14.3 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        leng, pos, dep = len(S), 0, 0

        def dfs(td):
            nonlocal pos, dep
            while pos < leng and S[pos] == '-':
                dep, pos = dep + 1, pos + 1
            if dep < td:
                return None

            dep, value = 0, 0
            while pos < leng and S[pos] != '-':
                value, pos = value * 10 + (ord(S[pos]) - ord('0')), pos + 1

            node = TreeNode(value)
            node.left = dfs(td + 1)
            node.right = dfs(td + 1)
            return node

        return dfs(0)


# 2. 栈 - 官方解
# https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/
# 执行用时： 100 ms , 在所有 Python3 提交中击败了 51.80% 的用户
# 内存消耗： 14.2 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path, pos = list(), 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]


# 1. 栈 - 自解
# "1-2--3--4-5--6--7"
# [1, 2, 5, 3, 4, 6, 7]
# "1-2--3---4-5--6---7"
# [1,2,5,3,null,6,null,4,null,7]
# "1-401--349---90--88"
# [1, 401, null, 349, 88, 90]
# "10-7--8"
# [1, 401, null, 349, 88, 90]
# 执行用时： 72 ms , 在所有 Python3 提交中击败了 98.20% 的用户
# 内存消耗： 14 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        lastlevel, curlevel, curval, stack = 0, 0, "", []

        for s in (S + "-"):
            if s == '-':
                if curval:
                    if not stack:
                        # print("rootnode={}".format(curval))
                        stack.append(TreeNode(int(curval)))
                    else:
                        if curlevel == lastlevel:
                            stack.pop()
                        if curlevel < lastlevel:
                            for _ in range(lastlevel - curlevel + 1):
                                stack.pop()
                        parentnode = stack[-1]
                        # print("curval={}, curlevel={}, lastlevel={}, parentnode={}".format(
                        #     curval, curlevel, lastlevel, parentnode.val))
                        curnode = TreeNode(int(curval))
                        if parentnode.left:
                            # print("parentnode={} right = {}".format(
                            #     parentnode.val, curnode.val))
                            parentnode.right = curnode
                        else:
                            # print("parentnode={} left = {}".format(
                            #     parentnode.val, curnode.val))
                            parentnode.left = curnode
                        stack.append(curnode)
                        lastlevel, curlevel = curlevel, 0

                curval, curlevel = "", curlevel + 1
            else:
                curval = curval + s

        return stack[0]
