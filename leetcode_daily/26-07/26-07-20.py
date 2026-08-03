""" 1260. 二维网格迁移    简单
给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
每次「迁移」操作将会引发下述活动：
位于 grid[i][j]（j < n - 1）的元素将会移动到 grid[i][j + 1]。
位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
请你返回 k 次迁移操作后最终得到的 二维网格。

示例 1：输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[9,1,2],[3,4,5],[6,7,8]]
示例 2：输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
示例 3：输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
输出：[[1,2,3],[4,5,6],[7,8,9]]

提示：
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-20.md

"""
from typing import List
import numpy as np

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    # 解法一
    # arr = np.array(grid)
    # m, n = arr.shape
    # k = k % (m * n)  # 去除整圈
    #
    # # 1. 整行下移 row_shift 行（切片拼接，不展平）
    # row_shift = k // n
    # if row_shift > 0:
    #     arr = np.concatenate([arr[-row_shift:], arr[:-row_shift]], axis=0)
    #
    # # 2. 处理剩余的列偏移
    # col_shift = k % n
    # if col_shift > 0:
    #     # 每行最后 col_shift 列（形状 m × col_shift）
    #     left_part = arr[:, -col_shift:]
    #     # 向下循环移动一行：最后一行移到开头（纯切片）
    #     left_shifted = np.concatenate([left_part[-1:], left_part[:-1]], axis=0)
    #     # 每行剩余部分（形状 m × (n - col_shift)）
    #     right_part = arr[:, :-col_shift]
    #     # 左右拼接得到最终结果
    #     arr = np.concatenate([left_shifted, right_part], axis=1)
    #
    # return arr.tolist()  # 如需返回 list

    # 解法二
    # return

    # 解法三
    m, n = len(grid), len(grid[0])
    size = m * n
    k %= size
    if k == 0:
        return grid

    def reverse(l: int, r: int) -> None:
        while l < r:
            x1, y1 = divmod(l, n)
            x2, y2 = divmod(r, n)
            grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]
            l += 1
            r -= 1

    # 轮转数组
    reverse(0, size - 1)
    reverse(0, k - 1)
    reverse(k, size - 1)
    return grid


if __name__ == '__main__':
    print(shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
    print(shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
    print(shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))













