// 785. 判断二分图 - 中等
// https://leetcode-cn.com/problems/is-graph-bipartite/
// https://leetcode-cn.com/problems/is-graph-bipartite/solution/pan-duan-er-fen-tu-by-leetcode-solution/

// 算法的流程如下：
// 我们任选一个节点开始，将其染成红色，并从该节点开始对整个无向图进行遍历；
// 在遍历的过程中，如果我们通过节点 u 遍历到了节点 v（即 u 和 v 在图中有一条边直接相连），那么会有两种情况：
// 如果 v 未被染色，那么我们将其染成与 u 不同的颜色，并对 v 直接相连的节点进行遍历；
// 如果 v 被染色，并且颜色与 u 相同，那么说明给定的无向图不是二分图。我们可以直接退出遍历并返回 False 作为答案。
// 当遍历结束时，说明给定的无向图是二分图，返回 True 作为答案。
// 我们可以使用「深度优先搜索」或「广度优先搜索」对无向图进行遍历，下文分别给出了这两种搜索对应的代码。


// 2. 方法二：广度优先搜索
// 执行用时： 28 ms , 在所有 Go 提交中击败了 90.24% 的用户
// 内存消耗： 6.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
var (
    UNCOLORED, RED, GREEN = 0, 1, 2
)

func isBipartite(graph [][]int) bool {
    n := len(graph)
    color := make([]int, n)
    for i := 0; i < n; i++ {
        if color[i] == UNCOLORED {
            queue := []int{}
            queue = append(queue, i)
            color[i] = RED
            for i := 0; i < len(queue); i++ {
                node := queue[i]
                cNei := RED
                if color[node] == RED {
                    cNei = GREEN
                }
                for _, neighbor := range graph[node] {
                    if color[neighbor] == UNCOLORED {
                        queue = append(queue, neighbor)
                        color[neighbor] = cNei
                    } else if color[neighbor] != cNei {
                        return false
                    }
                }
            }
        }
    }
    return true
}


// 1. 方法一：深度优先搜索
// 执行用时： 28 ms , 在所有 Go 提交中击败了 90.24% 的用户
// 内存消耗： 6.1 MB , 在所有 Go 提交中击败了 100.00% 的用户
var (
    UNCOLORED, RED, GREEN = 0, 1, 2
    color []int
    valid bool
)

func isBipartite(graph [][]int) bool {
    n := len(graph)
    valid = true
    color = make([]int, n)
    for i := 0; i < n && valid; i++ {
        if color[i] == UNCOLORED {
            dfs(i, RED, graph)
        }
    }
    return valid
}

func dfs(node int, c int, graph [][]int) {
    color[node] = c
    cNei := RED
    if c == RED {
        cNei = GREEN
    }
    for _, neighbor := range graph[node] {
        if color[neighbor] == UNCOLORED {
            dfs(neighbor, cNei, graph)
            if !valid {
                return
            }
        } else if color[neighbor] != cNei {
            valid = false
            return
        }
    }
}
