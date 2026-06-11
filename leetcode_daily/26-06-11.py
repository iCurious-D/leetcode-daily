""" 3558. 给边赋权值的方案数 I
给你一棵 n 个节点的无向树，节点从 1 到 n 编号，树以节点 1 为根。树由一个长度为 n - 1 的二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间有一条边。
一开始，所有边的权重为 0。你可以将每条边的权重设为 1 或 2。
两个节点 u 和 v 之间路径的 代价 是连接它们路径上所有边的权重之和。
选择任意一个 深度最大 的节点 x。返回从节点 1 到 x 的路径中，边权重之和为 奇数 的赋值方式数量。
由于答案可能很大，返回它对 109 + 7 取模的结果。
注意： 忽略从节点 1 到节点 x 的路径外的所有边。

示例 1：输入： edges = [[1,2]]; 输出： 1
解释：从节点 1 到节点 2 的路径有一条边（1 → 2）。
将该边赋权为 1 会使代价为奇数，赋权为 2 则为偶数。因此，合法的赋值方式有 1 种。

示例 2：输入： edges = [[1,2],[1,3],[3,4],[3,5]];  输出： 2
解释：最大深度为 2，节点 4 和节点 5 都在该深度，可以选择任意一个。例如，从节点 1 到节点 4 的路径包括两条边（1 → 3 和 3 → 4）。
将两条边赋权为 (1,2) 或 (2,1) 会使代价为奇数，因此合法赋值方式有 2 种。

提示：
2 <= n <= 10^5
edges.length == n - 1
edges[i] == [ui, vi]
1 <= ui, vi <= n
edges 表示一棵合法的树。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-11.md

"""
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            d = 0
            for y in g[x]:
                if y != fa:  # 不递归到父节点
                    d = max(d, dfs(y, x) + 1)
            return d

        k = dfs(1, 0)
        return pow(2, k - 1, MOD)


if __name__ == '__main__':
    print(Solution().assignEdgeWeights([[1,2]]))
    print(Solution().assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]]))
    print(Solution().assignEdgeWeights([[1,2],[2,3],[3,4],[4,5],[5,6]]))




