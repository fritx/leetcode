# 202. 快乐数 - 简单
# https://leetcode-cn.com/problems/happy-number/
# https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/


# 4. 官方解 - 方法三：数学
def isHappy(self, n: int) -> bool:

    cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    while n != 1 and n not in cycle_members:
        n = get_next(n)

    return n == 1


# 3. 官方解 - 方法二：快慢指针
def isHappy(self, n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1


# 2. 官方解 - 方法一：用 HashSet 检测循环
def isHappy(self, n: int) -> bool:
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


# 1. 递归 + HashSet检测
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 89.46% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 9.09% 的用户
class Solution:
    def __init__(self):
        self.st = set()

    def isHappy(self, n: int) -> bool:
        if n in self.st:
            return False
        self.st.add(n)
        arr = []
        while n:
            arr.append(n % 10)
            n //= 10
        nxt = 0
        for a in arr:
            nxt += pow(a, 2)
        if nxt is 1:
            return True
        return self.isHappy(nxt)
