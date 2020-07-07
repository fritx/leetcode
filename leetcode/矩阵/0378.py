# 378. 有序矩阵中第K小的元素
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/


# 3. 归并排序 - 简化
# 执行用时： 1396 ms , 在所有 Python3 提交中击败了 5.07% 的用户
# 内存消耗： 18.9 MB , 在所有 Python3 提交中击败了 50.00% 的用户
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = None
        while k:
            mininfo = [None, float("inf")]
            for i, row in enumerate(matrix):
                if row and row[0] < mininfo[1]:
                    mininfo = [i, row[0]]
            matrix[mininfo[0]] = matrix[mininfo[0]][1:]
            ans = mininfo[1]
            k -= 1
        return ans


# 2. 归并排序 - 维护数组
# 执行用时： 3368 ms , 在所有 Python3 提交中击败了 5.07% 的用户
# 内存消耗： 19.7 MB , 在所有 Python3 提交中击败了 50.00% 的用户
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nrows = len(matrix)
        leftrow = matrix[0]
        for i in range(1, nrows):
            rightrow = matrix[i]
            print(rightrow)
            newrow = []
            L, R = 0, 0
            while L < len(leftrow) and R < len(rightrow):
                if leftrow[L] < rightrow[R]:
                    newrow.append(leftrow[L])
                    L += 1
                else:
                    newrow.append(rightrow[R])
                    R += 1
            leftrow = newrow + leftrow[L:] + rightrow[R:]
        return leftrow[k - 1]


# 1. 暴力法
# 执行用时： 244 ms , 在所有 Python3 提交中击败了 56.52% 的用户
# 内存消耗： 19.7 MB , 在所有 Python3 提交中击败了 50.00% 的用户
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = []
        for row in matrix:
            for n in row:
                flat.append(n)
        flat.sort()
        return flat[k - 1]
