""" 3882. 网格图中最小异或路径    中等
给你一个大小为 m * n 的二维整数数组 grid。
你从 左上角 的单元格 (0, 0) 出发，想要到达 右下角 的单元格 (m - 1, n - 1)。
在每一步中，你 可以 向右或向下 移动。
路径的 代价 定义为该路径上所有单元格（包括 起点和终点）的值的 按位异或。
返回从 (0, 0) 到 (m - 1, n - 1) 的所有有效路径中 最小 的可能异或值。

示例 1：输入： grid = [[1,2],[3,4]];  输出： 6
解释：有两条有效路径：(0, 0) → (0, 1) → (1, 1)，异或值为：1 XOR 2 XOR 4 = 7
(0, 0) → (1, 0) → (1, 1)，异或值为：1 XOR 3 XOR 4 = 6;所有有效路径中的最小异或值为 6。
示例 2：输入： grid = [[6,7],[5,8]];  输出： 9
解释：有两条有效路径：(0, 0) → (0, 1) → (1, 1)，异或值为：6 XOR 7 XOR 8 = 9
(0, 0) → (1, 0) → (1, 1)，异或值为：6 XOR 5 XOR 8 = 11;所有有效路径中的最小异或值为 9。
示例 3：输入： grid = [[2,7,5]];  输出： 0
解释：只有一条有效路径：(0, 0) → (0, 1) → (0, 2)，异或值为：2 XOR 7 XOR 5 = 0
这条路径的异或值为 0，这是可能达到的最小值。

 提示：
1 <= m == grid.length <= 1000
1 <= n == grid[i].length <= 1000
m * n <= 1000

"""
from math import inf


def minCost(grid: list[list[int]]) -> int:
    # m, n = len(grid), len(grid[0])
    # dp = [set() for _ in range(n)]
    # for i in range(m):
    #     for j in range(n):
    #         g = grid[i][j]
    #         if i == 0 and j == 0:
    #             dp[j] = {g}
    #         elif i == 0:
    #             dp[j] = {x ^ g for x in dp[j - 1]}
    #         elif j == 0:
    #             dp[j] = {x ^ g for x in dp[j]}
    #         else:
    #             dp[j] = {x ^ g for x in dp[j] | dp[j - 1]}
    # return min(dp[-1])

    vis = set()
    ans = inf

    def dfs(i, j, xor):
        nonlocal ans
        if ans==0 or i<0 or j<0 or (i, j, xor) in vis:
            return
        vis.add((i, j, xor))
        xor ^= grid[i][j]
        if i==0 and j==0:
            ans = min(ans, xor)
            return
        dfs(i-1, j, xor)
        dfs(i, j-1, xor)

    dfs(len(grid)-1, len(grid[0])-1, 0)
    return ans




