"""3619. 总价值可以被 K 整除的岛屿数目   中等
给你一个 m x n 的矩阵 grid 和一个正整数 k。一个 岛屿 是由 正 整数（表示陆地）组成的，并且陆地间 四周 连通（水平或垂直）。
一个岛屿的总价值是该岛屿中所有单元格的值之和。
返回总价值可以被 k 整除 的岛屿数量。

示例 1:输入: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
输出: 2
解释:网格中包含四个岛屿。蓝色高亮显示的岛屿的总价值可以被 5 整除，而红色高亮显示的岛屿则不能。
示例 2:输入: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
输出: 6
解释:网格中包含六个岛屿，每个岛屿的总价值都可以被 3 整除。

提示:
m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
0 <= grid[i][j] <= 10^6
1 <= k < = 10^6

"""
from itertools import product
from typing import List


def countIslands(grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(i: int, j: int) -> int:
        res = grid[i][j]
        grid[i][j] = 0
        for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                res += dfs(x, y)
        return res

    ans = 0
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x and dfs(i, j) % k == 0:
                ans += 1

    return ans
    # return sum(v % k == 0 for v in filter(None, (dfs(i, j) for i, j in product(range(m), range(n)) if grid[i][j])))

