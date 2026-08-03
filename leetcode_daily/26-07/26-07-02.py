""" 3286. 穿越网格图的安全路径    中等
给你一个 m x n 的二进制矩形 grid 和一个整数 health 表示你的健康值。
你开始于矩形的左上角 (0, 0) ，你的目标是矩形的右下角 (m - 1, n - 1) 。
你可以在矩形中往上下左右相邻格子移动，但前提是你的健康值始终是 正数 。
对于格子 (i, j) ，如果 grid[i][j] = 1 ，那么这个格子视为 不安全 的，会使你的健康值减少 1 。
如果你可以到达最终的格子，请你返回 true ，否则返回 false 。
注意 ，当你在最终格子的时候，你的健康值也必须为 正数 。

示例 1：输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1;   输出：true
解释：沿着下图中灰色格子走，可以安全到达最终的格子。

示例 2：输入：grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3;   输出：false
解释：健康值最少为 4 才能安全到达最后的格子。

示例 3：输入：grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5;   输出：true
解释：沿着下图中灰色格子走，可以安全到达最终的格子。任何不经过格子 (1, 1) 的路径都是不安全的，因为你的健康值到达最终格子时，都会小于等于 0 。

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 50
2 <= m * n
1 <= health <= m + n
grid[i][j] 要么是 0 ，要么是 1 。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-02.md

"""
import heapq
from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # # 解法一 dijkstra      时间复杂度：(O(mn \log(mn)))，因为堆操作有 log 开销
        # dis = [[-1] * n for _ in range(m)]  # dis[i][j] 记录从起点到 (i,j) 的最小代价
        # q = [(grid[0][0], 0, 0)]  # 最小堆初始化，放入起点 (累计代价, 行, 列)
        # while q:
        #     val, i, j = heapq.heappop(q)  # 每次从堆里弹出累计代价最小的格子
        #     if dis[i][j] >= 0:    # 如果这个格子已经访问过了（距离不是 -1），直接跳过        #
        #         continue          # Dijkstra 的经典去重操作——因为堆里可能有同一个格子的多条旧路径，只有第一次弹出的是最优的。
        #     dis[i][j] = val       # 标记为已访问，记录最优距离。
        #     for dx, dy in dirs:
        #         nx, ny = i + dx, j + dy
        #         # 遍历上下左右四个方向。如果邻居在网格范围内且还没访问过，就把 (当前代价 + 邻居格子的代价) 压入堆中
        #         if 0 <= nx < m and 0 <= ny < n and dis[nx][ny] < 0:
        #             heapq.heappush(q, (val + grid[nx][ny], nx, ny))
        #
        # return dis[-1][-1] < health

        # # 解法二 01BFS
        # # 由于边权只有 0 和 1，可以用 01-BFS 替代 Dijkstra——代价为 0 的邻居放队头（优先处理），代价为 1 的放队尾。
        # # 这样用双端队列就实现了和 Dijkstra 一样的效果，但不需要堆，时间复杂度更优
        # dis = [[float('inf')] * n for _ in range(m)]
        # dis[0][0] = grid[0][0]
        # q = deque()
        # q.appendleft((0, 0))
        #
        # # 2-1：不做任何中途剪枝，老老实实跑完全部可达格子，最后统一判断
        # while q:
        #     i, j = q.popleft()
        #     for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
        #         if 0 <= x < m and 0 <= y < n:
        #             cost = grid[x][y]
        #             if dis[i][j] + cost < dis[x][y]:
        #                 dis[x][y] = dis[i][j] + cost
        #                 if cost == 0:
        #                     q.appendleft((x, y))
        #                 else:
        #                     q.append((x, y))
        # return dis[-1][-1] < health

        # 2-2：入队时剪枝 + 到达终点提前返回
        # 不合法的格子永远不会进入队列，也就不会从它继续扩展，相当于把搜索树提前修剪掉了
        # while q:
        #     x, y = q.popleft()
        #     if x == m - 1 and y == n - 1:
        #         return True
        #     for dx, dy in dirs:
        #         nx, ny = x + dx, y + dy
        #         if nx < 0 or nx >= m or ny < 0 or ny >= n:
        #             continue
        #         cost = dis[x][y] + grid[nx][ny]
        #         # 入队前剪枝 cost >= health → 直接 continue，这个邻居根本不进队列，不合法的路径直接掐断
        #         if cost >= health:
        #              continue
        #         if dis[nx][ny] > cost:
        #             dis[nx][ny] = cost
        #             if grid[nx][ny] == 0:
        #                 q.appendleft((nx, ny))
        #             else:
        #                 q.append((nx, ny))
        # return False

        # 2-3：不在入队时拦截，而是等格子弹出时再检查是否合法 + 到达终点提前返回
        # 不合法的格子还是会入队并占据队列空间，只是不会从它继续扩展（因为直接 return 了）
        # q = deque([(0, 0)])
        # while q:
        #     i, j = q.popleft()
        #     # 弹出后：dis[i][j] >= health → 返回 False
        #     if dis[i][j] >= health:
        #         return False
        #     # 不合法的格子会入队，但弹出时一旦发现代价超标，由于 01-BFS 的单调性（后面弹出的只会 ≥ 当前值），直接断言后续都不可能合法，返回 False
        #     if i == m - 1 and j == n - 1:
        #         return True
        #     for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
        #         if 0 <= x < m and 0 <= y < n:
        #             cost = grid[x][y]
        #             if dis[i][j] + cost < dis[x][y]:
        #                 dis[x][y] = dis[i][j] + cost
        #                 if cost == 0:
        #                     q.appendleft((x, y))
        #                 else:
        #                     q.append((x, y))
        # return dis[-1][-1] < health


if __name__ == '__main__':
    print(Solution().findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1))
    print(Solution().findSafeWalk([[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3))
    print(Solution().findSafeWalk([[1,1,1],[1,0,1],[1,1,1]], 5))
