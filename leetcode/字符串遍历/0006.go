// 6. Z 字形变换 - 中等
// https://leetcode-cn.com/problems/zigzag-conversion/
// https://leetcode-cn.com/problems/zigzag-conversion/solution/z-zi-xing-bian-huan-by-leetcode/


// 2.1 自解 - 二重循环 按行访问
// 执行用时： 8 ms , 在所有 Go 提交中击败了 77.32% 的用户
// 内存消耗： 6.5 MB , 在所有 Go 提交中击败了 25.00% 的用户
func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }
    step := (numRows - 1) * 2  // step必是偶数
    halfstep := step / 2
    N, ans := len(s), ""

    for offset := 0; offset <= halfstep; offset++ {
        for start := 0; start < N; start += step {
            ans += string(s[start + offset])
            if start + step - offset < N {
                if offset > 0 && offset < halfstep {
                    ans += string(s[start + step - offset])
                }
            }
        }
    }
    return ans
}

// 2. 官方解 - 方法二：按行访问
// 类似 2.1


// 1. 官方解 - 方法一：按行排序（插入）
// 执行用时： 12 ms , 在所有 Go 提交中击败了 53.25% 的用户
// 内存消耗： 6.3 MB , 在所有 Go 提交中击败了 25.00% 的用户
func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }
    curRow, moveOffset := 0, -1
    rows := make([]string, numRows)

    for i := 0; i < len(s); i++ {
        rows[curRow] += string(s[i])
        if curRow == 0 || curRow == numRows - 1 {
            moveOffset = -moveOffset
        }
        curRow += moveOffset
    }

    ans := ""
    for i := 0; i < numRows; i++ {
        ans += rows[i]
    }
    return ans
}

