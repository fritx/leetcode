# 面试题 16.11. 跳水板
# https://leetcode-cn.com/problems/diving-board-lcci/
# https://leetcode-cn.com/problems/diving-board-lcci/solution/tiao-shui-ban-by-leetcode-solution/
# https://leetcode-cn.com/problems/diving-board-lcci/solution/li-yong-zui-da-zui-xiao-chang-du-an-zhao-gu-ding-b/

# 2. 利用list(range)
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        ret = []
        if k == 0:
            return ret
        if shorter == longer:
            ret.append(k*shorter)
            return ret
        else:
            length_min = shorter*k
            length_max = longer*k
            dist = longer-shorter
            return list(range(length_min, length_max+1, dist))


# 1. 暴力法 - 数学
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [k * shorter]
        arr = []
        for a in range(k + 1):
            v = a * longer + (k - a) * shorter
            arr.append(v)
        return arr
