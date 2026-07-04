""" 2492. 两个城市间路径的最小分数  中等
给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。
给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。
城市构成的图不一定是连通的。
两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。
返回城市 1 和城市 n 之间的所有路径的 最小 分数。
注意：
一条路径指的是两个城市之间的道路序列。
一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。
测试数据保证城市 1 和城市n 之间 至少 有一条路径。

示例 1：输入：n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]];   输出：5
解释：城市 1 到城市 4 的路径中，分数最小的一条为：1 -> 2 -> 4 。这条路径的分数是 min(9,5) = 5 。不存在分数更小的路径。

示例 2：输入：n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]];   输出：2
解释：城市 1 到城市 4 分数最小的路径是：1 -> 2 -> 1 -> 3 -> 4 。这条路径的分数是 min(2,2,4,7) = 2 。

提示：
2 <= n <= 10^5
1 <= roads.length <= 10^5
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 10^4
不会有重复的边。
城市 1 和城市 n 之间至少有一条路径。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-04.md

"""
from typing import List
from collections import deque


# ========== 解法一：递归 DFS ==========
class Solution1:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v, cost in roads:
            g[u].append((v, cost))
            g[v].append((u, cost))

        vis = [False] * (n + 1)
        ans = float('inf')

        """
        从城市 1 出发，像走迷宫一样一路走到黑
        每经过一条边，就记录这条边的成本，和当前最小值比较
        访问过的城市打标记，避免重复访问形成死循环
        因为是连通图，最终会遍历完所有能到达的城市和边
        """
        def dfs(u: int):
            nonlocal ans
            vis[u] = True
            for v, cost in g[u]:
                ans = min(ans, cost)
                if not vis[v]:  # 如果下一个城市v还没访问过
                    dfs(v)      # 递归访问城市v（系统会自动把返回地址压入调用栈）

        dfs(1)
        return ans


# ========== 解法二：迭代 DFS（栈）==========
class Solution2:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v, cost in roads:
            g[u].append((v, cost))
            g[v].append((u, cost))

        vis = [False] * (n + 1)
        ans = float('inf')

        """
        和递归版逻辑完全一样，只是把系统调用栈换成了手动维护的列表
        用 list 的 append() 和 pop() 模拟栈的"后进先出"特性 """
        stack = [1]
        vis[1] = True
        while stack:
            u = stack.pop()
            for v, cost in g[u]:
                ans = min(ans, cost)
                if not vis[v]:
                    vis[v] = True
                    stack.append(v)

        return ans


# ========== 解法三：BFS（队列）==========
class Solution3:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v, cost in roads:
            g[u].append((v, cost))
            g[v].append((u, cost))

        vis = [False] * (n + 1)
        ans = float('inf')

        """
        从起点开始，先访问距离为 1 的所有城市，再访问距离为 2 的城市，以此类推
        同样需要记录访问过的城市，避免重复处理"""
        q = deque([1])
        vis[1] = True
        while q:
            u = q.popleft()
            for v, cost in g[u]:
                ans = min(ans, cost)
                if not vis[v]:
                    vis[v] = True
                    q.append(v)

        return ans
"""
DFS 是"一条路走到黑，撞墙再回溯"
BFS 是"水波纹扩散，一圈一圈往外扩"
但对于这道题，两者都要遍历整个连通分量，所以结果一样
"""

# ========== 解法四：并查集 ==========
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))        # parent[i] 表示节点i的父节点
        self.min_cost = [float('inf')] * n  # min_cost[i] 表示节点i所在集合的最小边权

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, cost):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
            self.min_cost[py] = min(self.min_cost[py], self.min_cost[px], cost)
        else:
            self.min_cost[px] = min(self.min_cost[px], cost)


class Solution4:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        for u, v, cost in roads:
            uf.union(u, v, cost)
        return uf.min_cost[uf.find(1)]


# ========== 测试验证 ==========
if __name__ == '__main__':
    test_cases = [
        (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
        (7, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 6, 5], [6, 7, 6]], 1),
        (5, [[1, 2, 10], [2, 3, 5], [3, 5, 8], [1, 4, 3], [4, 5, 12]], 3),
    ]

    solutions = [
        ("递归 DFS", Solution1()),
        ("迭代 DFS", Solution2()),
        ("BFS", Solution3()),
        ("并查集", Solution4()),
    ]

    print("=" * 60)
    print("🧪 开始验证四种解法的正确性")
    print("=" * 60)

    all_passed = True
    for name, sol in solutions:
        print(f"\n{name} 测试结果：")
        passed = True
        for i, (n, roads, expected) in enumerate(test_cases):
            result = sol.minScore(n, roads)
            status = "✅" if result == expected else "❌"
            if result != expected:
                passed = False
                all_passed = False
            print(f"  测试{i + 1}: {status} 期望={expected}, 实际={result}")

        if passed:
            print(f"  🎉 {name} 全部通过！")

    print("\n" + "=" * 60)
    if all_passed:
        print("🏆 恭喜！所有解法都通过了测试！")
    else:
        print("⚠️  有解法存在错误，请检查代码")
    print("=" * 60)
