# 1486. 数组异或操作 - 简单
# https://leetcode-cn.com/problems/xor-operation-in-an-array/
# https://leetcode-cn.com/problems/xor-operation-in-an-array/solution/o1-wei-yun-suan-by-bruceyuj/

# XOR 有很多有用的特性：
# - x ⊕ x = 0
# - 0 ⊕ x = x
# - 2x ⊕ (2x+1) = 1


# 3. 位运算（利用 XOR 的特性）
# 那么 start/2 ⊕ start/2+1 ⊕ start/2+2 ... ⊕ start/2+n−1 该怎么计算呢？
# 我们可以按照特性 3 来补全：
# 1. 如果 start/2 是偶数，我们只需要看 nn 是否是偶数即可：
#   - 如果 nn 是偶数，该公式结果就是 n/2 个 1 进行异或。也就是(n/2) & 1
#   - 如果 nn 是奇数，该公式结果就是 ((n/2) & 1) ⊕ (start/2+n−1)
# 2. 如果 start/2 是奇数，那么我们可以在前面补充 (start/2−1) ⊕ (start/2−1)，就回到了情况 1.
# 执行用时： 36 ms , 在所有 Python3 提交中击败了 89.66% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        def xor(n: int, start: int) -> int:  # 将公式转换成情况1
            if start & 1:
                return (start-1) ^ helper(n+1, start-1)
            return helper(n, start)

        def helper(n: int, start: int) -> int:  # 情况1
            if n % 2 == 0:
                return (n // 2) & 1
            return (n // 2) & 1 ^ (start + n-1)

        ans = 2 * xor(n, start // 2)

        # 处理最后一位
        if n & start & 1:
            ans += 1

        return ans


# 2. 暴力法 - 只维护ans
# 执行用时： 32 ms , 在所有 Python3 提交中击败了 96.91% 的用户
# 内存消耗： 13.7 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            num = start + 2 * i
            ans ^= num
        return ans


# 1. 暴力法 - 维护数组
# 执行用时： 40 ms , 在所有 Python3 提交中击败了 72.30% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        print(nums)
        ans = nums[0]
        for i in range(1, n):
            ans ^= nums[i]
        return ans
