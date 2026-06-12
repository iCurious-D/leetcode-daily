""" 3559. 给边赋权值的方案数 II
给你一棵有 n 个节点的无向树，节点从 1 到 n 编号，树以节点 1 为根。
树由一个长度为 n - 1 的二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间有一条边。
一开始，所有边的权重为 0。你可以将每条边的权重设为 1 或 2。
两个节点 u 和 v 之间路径的 代价 是连接它们路径上所有边的权重之和。
给定一个二维整数数组 queries。对于每个 queries[i] = [ui, vi]，计算从节点 ui 到 vi 的路径中，使得路径代价为 奇数 的权重分配方式数量。
返回一个数组 answer，其中 answer[i] 表示第 i 个查询的合法赋值方式数量。
由于答案可能很大，请对每个 answer[i] 取模 10^9 + 7。
注意： 对于每个查询，仅考虑 ui 到 vi 路径上的边，忽略其他边。

示例 1：输入： edges = [[1,2]], queries = [[1,1],[1,2]];  输出： [0,1]
解释：查询 [1,1]：节点 1 到自身没有边，代价为 0，因此合法赋值方式为 0。
    查询 [1,2]：从节点 1 到节点 2 的路径有一条边（1 → 2）。将权重设为 1 时代价为奇数，设为 2 时为偶数，因此合法赋值方式为 1。

示例 2：输入： edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]; 输出： [2,1,4]
解释：查询 [1,4]：路径为两条边（1 → 3 和 3 → 4），(1,2) 或 (2,1) 的组合会使代价为奇数，共 2 种。
    查询 [3,4]：路径为一条边（3 → 4），仅权重为 1 时代价为奇数，共 1 种。
    查询 [2,5]：路径为三条边（2 → 1 → 3 → 5），组合 (1,2,2)、(2,1,2)、(2,2,1)、(1,1,1) 均为奇数代价，共 4 种。

提示：
2 <= n <= 10^5
edges.length == n - 1
edges[i] == [ui, vi]
1 <= queries.length <= 10^5
queries[i] == [ui, vi]
1 <= ui, vi <= n
edges 表示一棵合法的树。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-12.md

"""
from typing import List


class LcaBinaryLifting:
    """
    使用二进制提升技术实现最近公共祖先(LCA)查询

    核心思想：
    - 预处理每个节点的2^0, 2^1, 2^2, ...级祖先
    - 利用这些信息可以在O(log n)时间内跳到任意祖先
    - 路径长度 = depth[x] + depth[y] - 2 * depth[LCA(x,y)]
    """
    def __init__(self, edges: List[List[int]]):
        # 根据边数计算节点数：n个节点的树有n-1条边
        n = len(edges) + 1
        # 计算二进制提升需要的层数：log2(n)向上取整
        m = n.bit_length()

        # 构建邻接表表示的无向图
        g = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1  # 节点编号从 0 开始（内部处理更方便）
            y -= 1
            g[x].append(y)
            g[y].append(x)

        # depth[i]: 节点i的深度（根节点深度为0）
        depth = [0] * n
        # pa[i][j]: 节点i的第2^j级祖先（-1表示不存在）
        pa = [[-1] * m for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            """
            深度优先搜索预处理深度和直接父节点

            参数:
                x: 当前节点
                fa: 当前节点的父节点
            """
            pa[x][0] = fa  # 第2^0=1级祖先就是父节点
            for y in g[x]:  # 遍历所有邻居
                if y != fa:  # 避免回溯到父节点
                    depth[y] = depth[x] + 1  # 子节点深度+1
                    dfs(y, x)  # 递归处理子节点

        # 从根节点0开始DFS，根节点的父节点设为-1
        dfs(0, -1)

        # 动态规划计算更高级的祖先
        # 状态转移：pa[x][i+1] = pa[pa[x][i]][i]
        # 即：x的2^(i+1)级祖先 = x的2^i级祖先的2^i级祖先
        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:  # 如果2^i级祖先存在
                    pa[x][i + 1] = pa[p][i]  # 计算2^(i+1)级祖先

        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        """
        获取node节点的第k级祖先

        原理：将k拆分为二进制，例如k=13=1101(二进制)=8+4+1
        则第13级祖先 = 第8级祖先的第4级祖先的第1级祖先

        参数:
            node: 起始节点
            k: 往上跳的步数
        返回:
            第k级祖先节点编号
        """
        for i in range(k.bit_length()):  # 遍历k的每一位二进制位
            if k >> i & 1:  # k 二进制从低到高第 i 位是 1；检查k的二进制表示中第i位是否为1
                node = self.pa[node][i]  # 往上跳2^i步
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        """
        求x和y的最近公共祖先(LCA)

        算法步骤：
        1. 确保x在y上方（depth[x] <= depth[y]）
        2. 将y提升到与x同一深度
        3. 如果此时x==y，说明x就是LCA
        4. 否则，x和y同时从大到小尝试往上跳，直到它们的祖先相同但自己不同
        5. 返回它们的父节点即为LCA

        参数:
            x: 第一个节点
            y: 第二个节点
        返回:
            x和y的最近公共祖先节点编号
        """
        if self.depth[x] > self.depth[y]:
            x, y = y, x  # 确保x的深度不大于y

        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x  # x本身就是y的祖先
        # 从最大的步长开始尝试，逐步缩小
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        # 此时x和y的父节点就是LCA
        return self.pa[x][0]

    # 返回 x 到 y 的距离（最短路长度，即路径上的边数）
    def get_dis(self, x: int, y: int) -> int:
        """
        计算x到y的路径长度（边数）

        公式推导：
        - 设L = LCA(x, y)
        - x到L的路径长度 = depth[x] - depth[L]
        - y到L的路径长度 = depth[y] - depth[L]
        - 总长度 = (depth[x] - depth[L]) + (depth[y] - depth[L])
                = depth[x] + depth[y] - 2 * depth[L]

        参数:
            x: 起始节点
            y: 终止节点
        返回:
            x到y路径上的边数
        """
        return self.depth[x] + self.depth[y] - self.depth[self.get_lca(x, y)] * 2


# 预处理 2 的幂（用于快速计算方案数）
MOD = 1_000_000_007
POW2 = [0] * 10 ** 5  # POW2[i] = 2^i % MOD
POW2[0] = 1  # 2^0 = 1
for i in range(1, len(POW2)):
    POW2[i] = POW2[i - 1] * 2 % MOD   # 递推：2^i = 2^(i-1) * 2

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        主函数：计算每个查询的合法赋值方案数

        解题思路：
        1. 构建LCA数据结构用于快速查询路径长度
        2. 对于每个查询(x, y)：
           - 如果x == y，路径长度为0，方案数为0
           - 否则，设路径长度为k，则方案数为2^(k-1)

        为什么是2^(k-1)？
        - k条边中选奇数条边赋值为1的方案数
        - 根据组合数学：C(k,1) + C(k,3) + C(k,5) + ... = 2^(k-1)
        - 这可以用二项式定理证明：(1+1)^k = (1-1)^k 展开后得到

        参数:
            edges: 树的边列表
            queries: 查询列表，每个查询为[x, y]
        返回:
            每个查询对应的合法赋值方案数列表
        """
        # 倍增法，又称二进制提升法
        g = LcaBinaryLifting(edges)  # 初始化LCA结构
        # 对每个查询计算答案
        return [
            POW2[g.get_dis(x - 1, y - 1) - 1] if x != y else 0
            for x, y in queries
        ]
        # 解释：
        # - x-1, y-1: 将节点编号从1-based转为0-based（与LCA内部一致）
        # - get_dis(...): 获取路径长度k
        # - POW2[k-1]: 获取2^(k-1) % MOD
        # - if x != y else 0: 同一点路径长度为0，无合法方案

        # """暴力法1
        # 暴力解法：对每个查询，通过BFS/DFS找路径，然后计算方案数
        # 时间复杂度：O(q * n)，q是查询数，n是节点数
        # 当q=10^5, n=10^5时，总操作量是10^10，直接TLE
        # """
        # MOD = 1_000_000_007
        # n = len(edges) + 1
        #
        # # 建图
        # g = [[] for _ in range(n + 1)]
        # for x, y in edges:
        #     g[x].append(y)
        #     g[y].append(x)
        #
        # def find_path(start: int, end: int) -> List[int]:
        #     """
        #     BFS找从start到end的路径，返回路径上的节点列表
        #     如果找不到路径，返回空列表
        #     """
        #     from collections import deque
        #
        #     if start == end:
        #         return [start]
        #
        #     # BFS模板
        #     visited = [False] * (n + 1)
        #     parent = [-1] * (n + 1)  # 记录每个节点的父节点，用于回溯路径
        #     queue = deque([start])
        #     visited[start] = True
        #
        #     while queue:
        #         node = queue.popleft()
        #         for neighbor in g[node]:
        #             if not visited[neighbor]:
        #                 visited[neighbor] = True
        #                 parent[neighbor] = node
        #                 if neighbor == end:
        #                     # 找到终点，回溯路径
        #                     path = []
        #                     cur = end
        #                     while cur != -1:
        #                         path.append(cur)
        #                         cur = parent[cur]
        #                     return path[::-1]  # 反转路径
        #                 queue.append(neighbor)
        #
        #     return []  # 没找到路径
        #
        # def count_odd_ways(path_length: int) -> int:
        #     """
        #     计算path_length条边中，有多少种赋值方案使得总和为奇数
        #     根据对称性，答案是2^(path_length - 1)
        #     """
        #     if path_length == 0:
        #         return 0
        #     return pow(2, path_length - 1, MOD)
        #
        # # 处理每个查询
        # answer = []
        # for x, y in queries:
        #     if x == y:
        #         # 同一点，路径长度为0
        #         answer.append(0)
        #     else:
        #         # BFS找路径
        #         path = find_path(x, y)
        #         # 路径长度 = 节点数 - 1
        #         path_length = len(path) - 1
        #         # 计算方案数
        #         answer.append(count_odd_ways(path_length))
        #
        # return answer

        # # 暴力法2
        # """
        # 暴力LCA解法：通过爬树找最近公共祖先
        #
        # 核心思路：
        # 1. 先用DFS预处理每个节点的父节点和深度
        # 2. 对于查询(u, v)，分别从u和v往上爬到根节点，记录路径
        # 3. 从两条路径的开头开始比对，第一个共同节点就是LCA
        # 4. 路径长度 = depth[u] + depth[v] - 2 * depth[LCA]
        #
        # 时间复杂度：每次查询O(n)（最坏情况要爬完整棵树）
        # 空间复杂度：O(n)存储父节点信息
        # """
        # MOD = 1_000_000_007
        # n = len(edges) + 1
        #
        # # 建图：邻接表表示
        # g = [[] for _ in range(n + 1)]
        # for x, y in edges:
        #     g[x].append(y)
        #     g[y].append(x)
        #
        # # DFS预处理：计算每个节点的父节点和深度
        # parent = [0] * (n + 1)  # parent[i]表示节点i的父节点
        # depth = [0] * (n + 1)  # depth[i]表示节点i的深度
        #
        # def dfs(x: int, fa: int) -> None:
        #     """
        #     深度优先搜索，预处理父节点和深度
        #
        #     参数:
        #         x: 当前节点
        #         fa: 当前节点的父节点
        #     """
        #     parent[x] = fa
        #     for y in g[x]:
        #         if y != fa:  # 避免回溯到父节点
        #             depth[y] = depth[x] + 1
        #             dfs(y, x)
        #
        # # 从根节点1开始DFS，根节点的父节点设为0（虚拟节点）
        # dfs(1, 0)
        #
        # def find_path_to_root(node: int) -> list:
        #     """
        #     从节点node一路爬到根节点，记录经过的所有节点
        #
        #     原理：不断访问父节点，直到到达根节点（父节点为0）
        #
        #     参数:
        #         node: 起始节点
        #     返回:
        #         从node到根节点的路径列表（包含node和根节点）
        #     """
        #     path = []
        #     current = node
        #     while current != 0:  # 一直爬到根节点的父节点（虚拟节点0）
        #         path.append(current)
        #         current = parent[current]
        #     return path
        #
        # def find_lca_brute_force(u: int, v: int) -> int:
        #     """
        #     暴力方法找u和v的最近公共祖先(LCA)
        #
        #     算法步骤：
        #     1. 分别从u和v往上爬到根，得到path_u和path_v
        #     2. 从两条路径的开头开始逐个比对
        #     3. 第一个相同的节点就是LCA
        #
        #     为什么第一个相同节点就是LCA？
        #     - path_u和path_v都是从节点往根的方向
        #     - 如果u和v有公共祖先，那么从根往下的第一个分叉点之前的节点都是共同的
        #     - 但从节点往根走，第一个相遇的就是"最近"的公共祖先
        #
        #     参数:
        #         u: 第一个节点
        #         v: 第二个节点
        #     返回:
        #         u和v的最近公共祖先节点编号
        #     """
        #     path_u = find_path_to_root(u)
        #     path_v = find_path_to_root(v)
        #
        #     # 将path_u转为集合，方便快速查找
        #     # 这样可以将查找从O(n)优化到O(1)
        #     path_u_set = set(path_u)
        #
        #     # 从v的路径往上找，第一个在u路径中的节点就是LCA
        #     # 因为是从下往上找，所以第一个遇到的就是"最近"的
        #     for node in path_v:
        #         if node in path_u_set:
        #             return node
        #
        #     # 理论上不会到这里，因为根节点一定是公共祖先
        #     return 1
        #
        # def get_distance(u: int, v: int) -> int:
        #     """
        #     计算u到v的路径长度（边数）
        #
        #     公式：distance = depth[u] + depth[v] - 2 * depth[LCA(u, v)]
        #
        #     推导过程：
        #     - u到LCA的距离 = depth[u] - depth[LCA]
        #     - v到LCA的距离 = depth[v] - depth[LCA]
        #     - 总距离 = (depth[u] - depth[LCA]) + (depth[v] - depth[LCA])
        #              = depth[u] + depth[v] - 2 * depth[LCA]
        #
        #     参数:
        #         u: 起始节点
        #         v: 终止节点
        #     返回:
        #         u到v路径上的边数
        #     """
        #     lca = find_lca_brute_force(u, v)
        #     return depth[u] + depth[v] - 2 * depth[lca]
        #
        # def count_odd_ways(k: int) -> int:
        #     """
        #     计算k条边的赋值方案中，使总和为奇数的方案数
        #
        #     原理：
        #     - 每条边可以赋值为1或2
        #     - 总和为奇数 ⟺ 有奇数条边赋值为1
        #     - 根据组合数学：C(k,1) + C(k,3) + C(k,5) + ... = 2^(k-1)
        #     - 也可以用对称性理解：所有2^k种方案中，一半奇数一半偶数
        #
        #     参数:
        #         k: 路径上的边数
        #     返回:
        #         合法赋值方案数
        #     """
        #     if k == 0:
        #         return 0
        #     return pow(2, k - 1, MOD)
        #
        # # 处理每个查询
        # answer = []
        # for x, y in queries:
        #     if x == y:
        #         # 同一点，路径长度为0，方案数为0
        #         answer.append(0)
        #     else:
        #         # 计算路径长度
        #         path_length = get_distance(x, y)
        #         # 计算方案数
        #         answer.append(count_odd_ways(path_length))
        #
        # return answer


if __name__ == '__main__':
    print(Solution().assignEdgeWeights([[1,2]], [[1,2]]))
    print(Solution().assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]], [[1,5],[1,4],[1,3],[1,2],[2,5],[2,4],[2,3],[3,4]]))
