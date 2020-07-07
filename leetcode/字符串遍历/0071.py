# 71. 简化路径
# https://leetcode-cn.com/problems/simplify-path/
# https://leetcode-cn.com/problems/simplify-path/solution/python-4-line-by-qqqun902025048/

# 2. 使用builtin split函数
# 执行用时： 48 ms , 在所有 Python3 提交中击败了 45.50% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 9.09% 的用户
class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)


# 1. 直接遍历法
# 执行用时： 52 ms , 在所有 Python3 提交中击败了 25.93% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 9.09% 的用户
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path[0] != '/':
            raise "path must begin with /"

        arr, curr = [], ""

        def flush() -> None:
            nonlocal arr, curr
            if not curr:
                pass
            elif curr == "..":
                if arr:
                    arr.pop()
            elif curr == '.':
                pass
            else:
                arr.append(curr)
            curr = ""

        for c in path[1:]:
            if c == '/':
                flush()
            else:
                curr += c

        flush()
        return '/' + '/'.join(arr)
