""" 1254. 统计封闭岛屿的数目     中等
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，
封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
请返回 封闭岛屿 的数目。

示例 1：输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：输入：grid = [[1,1,1,1,1,1,1], [1,0,0,0,0,0,1], [1,0,1,1,1,0,1],
                    [1,0,1,0,1,0,1], [1,0,1,1,1,0,1], [1,0,0,0,0,0,1], [1,1,1,1,1,1,1]]
输出：2

提示：
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

"""
from typing import List

def closedIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m < 3 or n < 3:
        return 0

    def dfs(x: int, y: int) -> None:
        grid[x][y] = 1
        for i, j in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                dfs(i, j)

    for i in range(m):
        step = 1 if i == 0 or i == m - 1 else n - 1
        for j in range(0, n, step):
            if grid[i][j] == 0:
                dfs(i, j)

    ans = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            if grid[i][j] == 0:
                ans += 1
                dfs(i, j)

    return ans





