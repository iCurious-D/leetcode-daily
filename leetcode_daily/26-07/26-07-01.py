""" 2812. 找出最安全路径   中等
给你一个下标从 0 开始、大小为 n x n 的二维矩阵 grid ，其中 (r, c) 表示：
    如果 grid[r][c] = 1 ，则表示一个存在小偷的单元格
    如果 grid[r][c] = 0 ，则表示一个空单元格
你最开始位于单元格 (0, 0) 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。
矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。
返回所有通向单元格 (n - 1, n - 1) 的路径中的 最大安全系数 。
单元格 (r, c) 的某个 相邻 单元格，是指在矩阵中存在的 (r, c + 1)、(r, c - 1)、(r + 1, c) 和 (r - 1, c) 之一。
两个单元格 (a, b) 和 (x, y) 之间的 曼哈顿距离 等于 | a - x | + | b - y | ，其中 |val| 表示 val 的绝对值。

示例 1：输入：grid = [[1,0,0],[0,0,0],[0,0,1]]；   输出：0
解释：从 (0, 0) 到 (n - 1, n - 1) 的每条路径都经过存在小偷的单元格 (0, 0) 和 (n - 1, n - 1) 。

示例 2：输入：grid = [[0,0,1],[0,0,0],[0,0,0]]；   输出：2
解释：上图所示路径的安全系数为 2：
- 该路径上距离小偷所在单元格（0，2）最近的单元格是（0，0）。它们之间的曼哈顿距离为 | 0 - 0 | + | 0 - 2 | = 2 。
可以证明，不存在安全系数更高的其他路径。

示例 3：输入：grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]；   输出：2
解释：上图所示路径的安全系数为 2：
- 该路径上距离小偷所在单元格（0，3）最近的单元格是（1，2）。它们之间的曼哈顿距离为 | 0 - 1 | + | 3 - 2 | = 2 。
- 该路径上距离小偷所在单元格（3，0）最近的单元格是（3，2）。它们之间的曼哈顿距离为 | 3 - 3 | + | 0 - 2 | = 2 。
可以证明，不存在安全系数更高的其他路径。

提示：
1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] 为 0 或 1
grid 至少存在一个小偷
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-01.md

"""
from typing import List
from collections import deque
import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # # 解法一：BFS + 二分查找
        # 先用多源BFS计算每个点到最近小偷的距离；
        # 二分枚举安全系数，检查是否存在一条路径，路径上所有点的安全系数都≥limit
        # dis = [[-1] * n for _ in range(n)]  # -1表示未访问
        # dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 四个方向
        # # 初始化：所有小偷位置入队
        # q = deque()
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             dis[i][j] = 0
        #             q.append((i, j))
        # # 多源BFS计算每个点到最近小偷的距离
        # while q:
        #     x, y = q.popleft()
        #     for dx, dy in dirs:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
        #             dis[nx][ny] = dis[x][y] + 1
        #             q.append((nx, ny))
        #
        # def check(limit: int) -> bool:
        #     visit = [[False] * n for _ in range(n)]
        #     q = deque()
        #     q.append((0, 0))
        #     visit[0][0] = True
        #     while q:
        #         x, y = q.popleft()
        #         if x == n-1 and y == n-1:
        #             return True
        #         for dx, dy in dirs:
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and dis[nx][ny] >= limit:
        #                 q.append((nx, ny))
        #                 visit[nx][ny] = True
        #     return False
        #
        # res = 0
        # lo, hi = 0, min(dis[0][0], dis[n-1][n-1])
        # while lo <= hi:
        #     mid = (lo + hi) // 2
        #     if check(mid):
        #         res = mid
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
        #
        # return res

        # # 解法二：Dijkstra变种（最大最小值路径）
        # # 经典的"瓶颈路"问题（bottleneck path），找一条路径使得路径上的最小边权最大
        # Dijkstra改造：传统Dijkstra：累加路径权重，找最短路径 => 本题Dijkstra：维护路径上的最小值，找"最大最小值"
        # 贪心策略：每次都选择当前安全系数最高的点，确保路径尽可能安全
        # 在线算法，直接在搜索过程中动态维护最优路径
        # dis = [[-1] * n for _ in range(n)]
        # dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # q = deque()
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]:
        #             q.append((i, j))
        #             dis[i][j] = 0        #
        # while q:
        #     cx, cy = q.popleft()
        #     for dx, dy in dirs:
        #         nx, ny = cx + dx, cy + dy
        #         if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
        #             dis[nx][ny] = dis[cx][cy] + 1
        #             q.append((nx, ny))
        #
        # # Dijkstra算法变种：找"最大最小值"路径
        # 就是在最大化一条路径的瓶颈（路径上最危险的那一步的安全系数）
        # visit = [[False] * n for _ in range(n)]
        # visit[0][0] = True
        # Python 的 heapq 模块实现的是最小堆，为了得到“最大堆”的效果（每次弹出安全系数最高的格子），采用了存负数的技巧
        # pq = [(-dis[0][0], 0, 0)]]  # 优先队列（最大堆用负数模拟），初始化为起点
        # max_safeness = min(dis[0][0], dis[n - 1][n - 1])  # 初始安全系数
        #
        # while pq:
        #     val, cx, cy = heapq.heappop(pq)  # 弹出当前安全系数最高的点
        #     val = -val  # 转回正数
        #     max_safeness = min(max_safeness, val)  # 更新路径的最小安全系数
        #     if cx == n - 1 and cy == n - 1:
        #         break
        #     for dx, dy in dirs:
        #         nx, ny = cx + dx, cy + dy
        #         if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
        #             visit[nx][ny] = True
        #             heapq.heappush(pq, (-dis[nx][ny], nx, ny))  # 负数入堆（实现最大堆）
        #
        # return max_safeness

        # 解法三四：并查集
        # # 解法三：
        # # 第一步：多源BFS计算每个点到最近小偷的距离
        # dis = [[-1] * n for _ in range(n)]
        # dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # q = deque()
        # cells = []  # 存储所有点及其距离，用于后续排序处理
        # # 初始化：所有小偷位置入队
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]:  # 如果是小偷
        #             q.append((i, j))
        #             dis[i][j] = 0  # 小偷到自己的距离为0
        #             cells.append((i, j, 0))  # 记录该点
        #
        # # BFS扩展，计算所有点的距离
        # while q:
        #     cx, cy = q.popleft()
        #     for dx, dy in dirs:
        #         nx, ny = cx + dx, cy + dy
        #         if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
        #             dis[nx][ny] = dis[cx][cy] + 1  # 距离+1
        #             q.append((nx, ny))
        #             cells.append((nx, ny, dis[nx][ny]))  # 记录该点及其距离
        #
        # # 第二步：按距离从大到小依次"激活"点，用并查集维护连通性
        # visit = [[False] * n for _ in range(n)]  # 标记已激活的点
        # uf = UnionFind(n * n)  # 并查集，将二维坐标映射为一维：(i,j) -> i*n+j
        #
        # # 关键：按距离从大到小处理（逆序）
        # for i in range(len(cells) - 1, -1, -1):
        #     cx, cy, dist = cells[i]  # 当前点及其距离
        #     visit[cx][cy] = True  # 激活该点
        #
        #     # 尝试与周围已激活的点合并
        #     for dx, dy in dirs:
        #         nx, ny = cx + dx, cy + dy
        #         if 0 <= nx < n and 0 <= ny < n and visit[nx][ny]:
        #             # 如果邻居已被激活，说明邻居的距离>=当前dist
        #             # 将两个点合并到同一集合
        #             uf.unite(cx * n + cy, nx * n + ny)
        #
        #     # 检查起点和终点是否连通
        #     if uf.connect(0, n * n - 1):
        #         return dist  # 当前距离就是最大安全系数
        #
        # return 0

        # 解法四：
        dis = [[-1] * n for _ in range(n)]
        q = []
        # 初始化：所有小偷位置入队
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    dis[i][j] = 0
                    q.append((i, j))

        groups = [q]  # groups[d]存储所有距离为d的点（分层记录）
        # 多源BFS，按层扩展
        while q:
            tmp = q  # 当前层的所有点
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] < 0:
                        dis[x][y] = len(groups)  # 当前层数就是距离
                        q.append((x, y))
            groups.append(q)  # 将当前层加入groups

        # 并查集模板（内部函数，更简洁）
        fa = list(range(n * n))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])  # 路径压缩
            return fa[x]

        # 从大到小枚举答案（跳过最后一层空列表和第一层小偷）
        for d in range(len(groups) - 2, 0, -1):
            # 激活所有距离为d的点
            for i, j in groups[d]:
                # 尝试与周围距离>=d的点合并
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= d:
                        # 合并：将邻居的根节点指向当前点的根节点
                        fa[find(x * n + y)] = find(i * n + j)
            # 检查起点和终点是否连通
            if find(0) == find(n * n - 1):  # 写这里判断更快些
                return d
        return 0


if __name__ == '__main__':
    print(Solution().maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
    print(Solution().maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))
    print(Solution().maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))
