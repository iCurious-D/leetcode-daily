""" 2267. 检查是否有合法括号字符串路径    困难
一个括号字符串是一个 非空 且只包含 '(' 和 ')' 的字符串。如果下面 任意 条件为 真 ，那么这个括号字符串就是 合法的 。
字符串是 () 。字符串可以表示为 AB（A 连接 B），A 和 B 都是合法括号序列。字符串可以表示为 (A) ，其中 A 是合法括号序列。
给你一个 m x n 的括号网格图矩阵 grid 。网格图中一个 合法括号路径 是满足以下所有条件的一条路径：
路径开始于左上角格子 (0, 0) 。
路径结束于右下角格子 (m - 1, n - 1) 。
路径每次只会向 下 或者向 右 移动。
路径经过的格子组成的括号字符串是 合法 的。
如果网格图中存在一条 合法括号路径 ，请返回 true ，否则返回 false 。

示例 1：输入：grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]];   输出：true
解释：上图展示了两条路径，它们都是合法括号字符串路径。
第一条路径得到的合法字符串是 "()(())" 。第二条路径得到的合法字符串是 "((()))" 。注意可能有其他的合法括号字符串路径。
示例 2：输入：grid = [[")",")"],["(","("]];       输出：false
解释：两条可行路径分别得到 "))(" 和 ")((" 。由于它们都不是合法括号字符串，我们返回 false 。

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] 要么是 '(' ，要么是 ')' 。

"""
from functools import cache
from typing import List


def hasValidPath(grid: List[List[str]]) -> bool:
    # m, n = len(grid), len(grid[0])
    #
    # # 剪枝：路径共 m+n-1 格，合法括号串长度必须为偶数 → m+n 必须为奇数
    # # 且起点必须是 '('，终点必须是 ')'
    # if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
    #     return False
    #
    # # dp[j] 是一个大整数，当 bitset 用：
    # # 第 k 位为 1 ⇔ 走到 (当前行, j) 后，balance=k 是可达的
    # dp = [0] * n
    #
    # for i in range(m):
    #     for j in range(n):
    #         if i == 0 and j == 0:
    #             bs = 1  # 虚拟起点：进入 (0,0) 前 balance=0（bit 0 置位）
    #         elif i == 0:
    #             bs = dp[j - 1]  # 首行：只能从左边的格子来
    #         elif j == 0:
    #             bs = dp[j]  # 首列：只能从上方的格子来（dp[j] 此刻仍是上一行的值）
    #         else:
    #             bs = dp[j] | dp[j - 1]  # 普通格：上方路径 ∨ 左边路径的可达集合取并集
    #
    #         # 核心转移：
    #         #   '(' → 所有 balance 集体 +1 → bitset 整体左移一位
    #         #   ')' → 所有 balance 集体 -1 → bitset 整体右移一位
    #         #   （右移时 bit 0 溢出 = balance 变负的路径被自动剪掉）
    #         dp[j] = bs << 1 if grid[i][j] == '(' else bs >> 1
    #
    # # 终点：bit 0 为 1 ⇔ balance=0 可达 ⇔ 存在合法括号路径
    # return bool(dp[-1] & 1)

    m, n = len(grid), len(grid[0])
    if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
        return False

    @cache
    def dfs(i: int, j: int, k: int) -> bool:
        if i == m - 1 and j == n - 1:
            return k == 0
        if k < 0:
            return False
        return (i < m - 1 and dfs(i + 1, j, k + 1 if grid[i + 1][j] == '(' else k - 1)) or \
            (j < n - 1 and dfs(i, j + 1, k + 1 if grid[i][j + 1] == '(' else k - 1))

    return dfs(0, 0, 1)

    # m, n = len(grid), len(grid[0])
    # if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
    #     return False
    # @cache
    # def dfs(i: int, j: int, k: int) -> bool:
    #     if i == m - 1 and j == n - 1:
    #         return k == 0
    #     if k < 0:
    #         return False
    #     return (i < m - 1 and dfs(i + 1, j, k + 1 if grid[i + 1][j] == '(' else k - 1)) or \
    #             (j < n - 1 and dfs(i, j + 1, k + 1 if grid[i][j + 1] == '(' else k - 1))
    # return dfs(0, 0, 1)


if __name__ == '__main__':
    print(hasValidPath([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]))
    print(hasValidPath([[")", ")"], ["(", "("]]))
    print(hasValidPath([["(", "(", ")"], ["(", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]))
