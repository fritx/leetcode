# 349. 两个数组的交集 - 简单
# https://leetcode-cn.com/problems/intersection-of-two-arrays/
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode-solution/


# 3. 利用collections.Counter
# 执行用时： 60 ms , 在所有 Python3 提交中击败了 80.51% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 12.50% 的用户
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (count: = m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection


# 2. 方法二：内置函数
# 执行用时： 64 ms , 在所有 Python3 提交中击败了 54.96% 的用户
# 内存消耗： 13.5 MB , 在所有 Python3 提交中击败了 20.00% 的用户
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


# 1. 方法一：两个set
# 执行用时： 60 ms , 在所有 Python3 提交中击败了 72.72% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 20.00% 的用户
# from typing import Set
class Solution:
    def set_intersection(self, set1: Set[int], set2: Set[int]):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
