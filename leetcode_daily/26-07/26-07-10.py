""" 3534. 针对图的路径存在性查询 II    困难
给你一个整数 n，表示图中的节点数量，这些节点按从 0 到 n - 1 编号。
同时给你一个长度为 n 的整数数组 nums，以及一个整数 maxDiff。
如果满足 |nums[i] - nums[j]| <= maxDiff（即 nums[i] 和 nums[j] 的 绝对差 至多为 maxDiff），则节点 i 和节点 j 之间存在一条 无向边 。
此外，给你一个二维整数数组 queries。
对于每个 queries[i] = [ui, vi]，找到节点 ui 和节点 vi 之间的 最短距离 。如果两节点之间不存在路径，则返回 -1。
返回一个数组 answer，其中 answer[i] 是第 i 个查询的结果。
注意：节点之间的边是无权重（unweighted）的。

示例 1：输入: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]];   输出: [1,1]
解释:查询	最短路径	最短距离
[0, 3]	0 → 3	1
[2, 4]	2 → 4	1
因此，输出为 [1, 1]。

示例 2：输入: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]];  输出: [1,2,-1,1]
解释:查询	最短路径	最短距离
[0, 1]	0 → 1	1
[0, 2]	0 → 1 → 2	2
[2, 3]	无	-1
[4, 3]	3 → 4	1
因此，输出为 [1, 2, -1, 1]。

示例 3：输入: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]; 输出: [0,-1,-1]
解释:由于以下原因，任意两个节点之间都不存在边：
节点 0 和节点 1：|nums[0] - nums[1]| = |3 - 6| = 3 > 1
节点 0 和节点 2：|nums[0] - nums[2]| = |3 - 1| = 2 > 1
节点 1 和节点 2：|nums[1] - nums[2]| = |6 - 1| = 5 > 1
因此，不存在任何可以到达其他节点的节点，输出为 [0, -1, -1]。

提示：
1 <= n == nums.length <= 10^5
0 <= nums[i] <= 10^5
0 <= maxDiff <= 10^5
1 <= queries.length <= 10^5
queries[i] == [ui, vi]
0 <= ui, vi < n
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-10.md

"""
from typing import List

def pathExistenceQueries(n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    """ 排序 + 倍增  """
    #
    # # ========== 第一步：排序 + 建立排名映射 ==========
    # # 核心思想：把节点按值排序，将图问题转化为一维数组上的跳跃问题
    # idx = sorted(range(n), key=lambda i: nums[i])   # idx[i] = 排序后第i个位置的原始节点编号
    # rank = [0] * n                                  # rank[原始编号] = 排序后的位置（排名）
    # for i, j in enumerate(idx):
    #     rank[j] = i
    #
    # # ========== 第二步：预处理倍增表 ==========
    # m = n.bit_length()                      # m = log2(n) + 1，表示倍增的最大层数；# 例如 n=5 时，m=3，表示最多可以跳 2^2=4 步
    # f = [[0] * m for _ in range(n)]         # f[i][j] = 从排序后的位置i出发，跳2^j步能到达的最左位置
    #                                         # j=0: 跳1步(2^0); j=1: 跳2步(2^1); j=2: 跳4步(2^2) ...以此类推
    # # --- 计算第一层倍增 f[i][0]：跳1步能到哪 ---
    # # 使用滑动窗口维护区间[left, i]，保证区间内最大值-最小值 <= maxDiff
    # left = 0
    # for i in range(n):
    #     while left < i and nums[idx[i]] - nums[idx[left]] > maxDiff:
    #         left += 1                       # 如果当前位置i的值与left位置的值差超过maxDiff，说明left太远了，右移
    #     f[i][0] = left                      # f[i][0] = left 表示从位置i跳1步能到达的最左位置是left
    #
    # # --- 填充更高层倍增表 ---
    # # 状态转移方程：f[i][j] = f[f[i][j-1]][j-1]：从i跳2^j步 = 先从i跳2^(j-1)步到中间点，再从中间点跳2^(j-1)步
    # for j in range(1, m):
    #     for i in range(n):
    #         f[i][j] = f[f[i][j - 1]][j - 1]
    #
    # # ========== 第三步：处理查询 ==========
    # res = []
    # for u, v in queries:
    #     l, r = rank[u], rank[v]             # 将原始节点编号转换为排序后的排名
    #     if l > r:
    #         l, r = r, l                     # 保证 l <= r，因为我们只关心从左到右的距离
    #     if l == r:
    #         res.append(0)                   # 特殊情况：同一个节点，距离为0
    #         continue
    #     # --- 倍增跳跃：从r往l的方向跳 ---
    #     step = 0
    #     # 从大步长到小步长贪心试探（类似二进制分解）
    #     for i in range(m - 1, -1, -1):
    #         # 如果从r跳2^i步后仍然在l的右边，说明需要继续跳
    #         if f[r][i] > l:
    #             r = f[r][i]                 # 执行这次跳跃
    #             step += 1 << i              # 累加实际跳跃步数（2^i步，不是1步！）
    #
    #     # --- 判断是否能到达l ---
    #     # 循环结束后，r再跳1步如果能到达或越过l，说明连通
    #     if f[r][0] <= l:
    #         res.append(step + 1)            # 总步数 = 已跳步数 + 最后1步
    #     else:
    #         res.append(-1)                  # 无法到达，不连通
    #
    # return res


    idx = sorted(range(n), key=lambda i: nums[i])
    values = [nums[node] for node in idx]
    pos = [0] * n
    for i, j in enumerate(idx):
        pos[j] = i

    m = n.bit_length()  # m = log2(n) + 1，表示倍增的最大层数；# 例如 n=5 时，m=3，表示最多可以跳 2^2=4 步
    farthest = [[0] * m for _ in range(n)]

    # k = 0：一步最远射程（双指针滑动窗口）
    right = 0
    for left in range(n):
        right = max(right, left)
        while (right + 1 < n and values[right + 1] - values[left] <= maxDiff):
            right += 1
        farthest[left][0] = right  # f[i][0] = 从 i 跳 1 步能到达的最右位置

    # k >= 1：两段拼接，指数级扩展
    for k in range(1, m):
        for i in range(n):
            farthest[i][k] = farthest[farthest[i][k - 1]][k - 1]
            # 状态转移方程：从i跳2^j步 = 先从i跳2^(j-1)步到中间点，再从中间点跳2^(j-1)步

    # # ========== 第三步：处理查询 ==========
    res = []
    for u, v in queries:
        l, r = pos[u], pos[v]  # 将原始节点编号转换为排序后的排名
        if l > r:
            l, r = r, l  # 保证 l <= r，因为我们只关心从左到右的距离
        if l == r:
            res.append(0)  # 特殊情况：同一个节点，距离为0
            continue
        step = 0
        for i in range(m - 1, -1, -1):
            if farthest[l][i] < r:
                l = farthest[l][i]  # 执行这次跳跃
                step += 1 << i  # 累加实际跳跃步数（2^i步，不是1步！）

        if farthest[l][0] >= r:
            res.append(step + 1)  # 总步数 = 已跳步数 + 最后1步
        else:
            res.append(-1)  # 无法到达，不连通

    return res


if __name__ == '__main__':
    print(pathExistenceQueries(n=5, nums=[1, 8, 3, 4, 2], maxDiff=3, queries=[[0, 3], [2, 4]]))
    print(pathExistenceQueries(n=5, nums=[5, 3, 1, 9, 10], maxDiff=2, queries=[[0, 1], [0, 2], [2, 3], [4, 3]]))
    print(pathExistenceQueries(n=3, nums=[3, 6, 1], maxDiff=1, queries=[[0, 0], [0, 1], [1, 2]]))



