// 717. 1比特与2比特字符 - 简单
// https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/submissions/
// https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/1bi-te-yu-2bi-te-zi-fu-by-leetcode/


// 4. 贪心 + 位运算
// 执行用时： 4 ms , 在所有 Go 提交中击败了 93.75% 的用户
// 内存消耗： 2.7 MB , 在所有 Go 提交中击败了 100.00% 的用户
func isOneBitCharacter(bits []int) bool {
    parity := bits[len(bits)-1]  // 模拟pop
    bits = bits[0:len(bits)-1]
    for {
        if len(bits) > 0 {
            tmp := bits[len(bits)-1]  // 模拟pop
            bits = bits[0:len(bits)-1]
            if tmp == 1 {
                parity ^= 1
                continue
            }
        }
        break
    }
    return parity == 0
}

// 3. 贪心
func isOneBitCharacter(bits []int) bool {
    bits = bits[0:len(bits)-1]  // 给定的字符串总是由0结束
    c := 0
    for len(bits) > 0 {
        num := bits[len(bits)-1]
        bits = bits[0:len(bits)-1]
        if num == 0 {
            break
        }
        c += 1
    }
    return c % 2 == 0
}


// 2. 线性扫描
// 执行用时： 4 ms , 在所有 Go 提交中击败了 93.75% 的用户
// 内存消耗： 2.7 MB , 在所有 Go 提交中击败了 100.00% 的用户
func isOneBitCharacter(bits []int) bool {
    i := 0
    for i < len(bits) - 1 {
        i += bits[i] + 1
    }
    return i == len(bits) - 1
}


// 1. 递归
// 执行用时： 4 ms , 在所有 Go 提交中击败了 93.75% 的用户
// 内存消耗： 2.8 MB , 在所有 Go 提交中击败了 100.00% 的用户
func isOneBitCharacter(bits []int) bool {
    N := len(bits)
    if N == 0 { // 不符题意
        return false
    }
    if N == 1 { // 给定的字符串总是由0结束
        return true
    }
    return isOneBitCharacter(bits[1+bits[0] : N])
}
