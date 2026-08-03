""" 2685. 统计完全连通分量的数量   中等
给你一个整数 n 。现有一个包含 n 个顶点的 无向 图，顶点按从 0 到 n - 1 编号。
给你一个二维整数数组 edges 其中 edges[i] = [ai, bi] 表示顶点 ai 和 bi 之间存在一条 无向 边。
返回图中 完全连通分量 的数量。
如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 连通分量 。
如果连通分量中每对节点之间都存在一条边，则称其为 完全连通分量 。

示例 1：输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]    输出：3
解释：如上图所示，可以看到此图所有分量都是完全连通分量。

示例 2：输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]  输出：1
解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
因此，在图中完全连接分量的数量是 1 。

提示：
1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
不存在重复的边
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-11.md

"""
from typing import List


def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    """ 并查集 """
    # 初始化并查集
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    # 合并所有相连的节点
    for u, v in edges:
        union(u, v)

    # 统计每个连通分量的节点数
    block_nodes = {}
    for i in range(n):
        root = find(i)
        block_nodes[root] = block_nodes.get(root, 0) + 1

    # 统计每个连通分量的边数
    block_edges = {}
    for u, v in edges:
        root = find(u)
        block_edges[root] = block_edges.get(root, 0) + 1

    # 检查每个连通分量是否是完全连通的
    ans = 0
    for root in block_nodes:
        v = block_nodes[root]
        e = block_edges.get(root, 0)
        # 完全连通图应该有 v*(v-1)/2 条边
        if e == v * (v - 1) // 2:
            ans += 1

    return ans

    # """ BFS + 统计 """
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    visited = [False] * n

    ans = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            q = [i]
            V = 0
            E = 0
            while q:
                u = q.pop()
                V += 1
                E += len(g[u])
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            if E == V * (V - 1):
                ans += 1
    return ans
    #
    # # def dfs(u):
    # #     nonlocal V, E
    # #     V += 1
    # #     E += len(g[u])
    # #     visited[u] = True
    # #     for v in g[u]:
    # #         if not visited[v]:
    # #             dfs(v)
    # #
    # # ans = 0
    # # for i, b in enumerate(visited):
    # #     if not b:
    # #         V = E = 0
    # #         dfs(i)
    # #         ans += E == V * (V - 1)
    # # return ans



if __name__ == '__main__':
    print(countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
    print(countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
    print(countCompleteComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
