"""  3161. 物块放置查询
有一条无限长的数轴，原点在 0 处，沿着 x 轴 正 方向无限延伸。
给你一个二维数组 queries ，它包含两种操作：
操作类型 1 ：queries[i] = [1, x] 。在距离原点 x 处建一个障碍物。数据保证当操作执行的时候，位置 x 处 没有 任何障碍物。
操作类型 2 ：queries[i] = [2, x, sz] 。判断在数轴范围 [0, x] 内是否可以放置一个长度为 sz 的物块，这个物块需要 完全 放置在范围 [0, x] 内。
如果物块与任何障碍物有重合，那么这个物块 不能 被放置，但物块可以与障碍物刚好接触。
注意，你只是进行查询，并 不是 真的放置这个物块。每个查询都是相互独立的。
请你返回一个 boolean 数组results ，如果第 i 个操作类型 2 的操作你可以放置物块，那么 results[i] 为 true ，否则为 false 。

示例 1：输入：queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
输出：[false,true,true]
解释：查询 0 ，在 x = 2 处放置一个障碍物。在 x = 3 之前任何大小不超过 2 的物块都可以被放置。

示例 2：输入：queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
输出：[true,true,false]
解释：查询 0 在 x = 7 处放置一个障碍物。在 x = 7 之前任何大小不超过 7 的物块都可以被放置。
查询 2 在 x = 2 处放置一个障碍物。现在，在 x = 7 之前任何大小不超过 5 的物块可以被放置，x = 2 之前任何大小不超过 2 的物块可以被放置。

提示：
1 <= queries.length <= 15 * 104
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 104, 3 * queries.length)
输入保证操作 1 中，x 处不会有障碍物。
输入保证至少有一个操作类型 2 。
====================================================================

题解路径：. / leetcode_daily_stories / 26-05-30.md


"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    # 1. 暴力法：超时
    # def getResults(self, queries: List[List[int]]) -> List[bool]:
    #     obstacles = []
    #     ans = []
    #     for q in queries:
    #         if q[0] == 1:
    #             obstacles.append(q[1])
    #             obstacles.sort()
    #         else:
    #             x, sz = q[1], q[2]
    #             obs = [0] + [p for p in obstacles if p <= x] + [x]
    #             max_gap = 0
    #             for i in range(len(obs) - 1):
    #                 max_gap = max(max_gap, obs[i + 1] - obs[i])
    #             ans.append(max_gap >= sz)
    #     return ans

    # 2. 线段树解法1
    # def getResults(self, queries: List[List[int]]) -> List[bool]:
    #     mx = max(q[1] for q in queries) + 1
    #     obstacles = SortedList([0, mx])
    #     seg = [0] * (2 << mx.bit_length())
    #
    #     def update(o, l, r, i, val):
    #         if l == r:
    #             seg[o] = val
    #             return
    #         m = (l + r) >> 1
    #         if i <= m:
    #             update(o * 2, l, m, i, val)
    #         else:
    #             update(o * 2 + 1, m + 1, r, i, val)
    #         seg[o] = max(seg[o * 2], seg[o * 2 + 1])
    #
    #     def query(o, l, r, L, R):
    #         if L <= l and r <= R:
    #             return seg[o]
    #         mid = (l + r) >> 1
    #         res = 0
    #         if L <= mid:
    #             res = max(res, query(o * 2, l, mid, L, R))
    #         if R > mid:
    #             res = max(res, query(o * 2 + 1, mid + 1, r, L, R))
    #         return res
    #
    #     ans = []
    #     for q in queries:
    #         x = q[1]
    #         idx = min(len(obstacles) - 1, obstacles.bisect_right(x))
    #         if q[0] == 1:
    #             r = obstacles[idx]
    #             l = obstacles[idx - 1] if idx > 0 else obstacles[0]
    #             update(1, 0, mx, x, x - l)
    #             update(1, 0, mx, r, r - x)
    #             obstacles.add(x)
    #         else:
    #             sz = q[2]
    #             pre = obstacles[0] if idx == 0 else obstacles[idx - 1]
    #             max_space = max(x - pre, query(1, 0, mx, 0, pre))
    #             ans.append(max_space >= sz)
    #     return ans

    # 3. 线段树解法2
    # def getResults(self, queries: List[List[int]]) -> List[bool]:
    #     mx = max(q[1] for q in queries) + 1
    #     seg = [0] * (2 << mx.bit_length())
    #
    #     # 把 i 处的值改成 val
    #     def update(o: int, l: int, r: int, i: int, val: int) -> None:
    #         if l == r:
    #             seg[o] = val
    #             return
    #         m = (l + r) // 2
    #         if i <= m:
    #             update(o * 2, l, m, i, val)
    #         else:
    #             update(o * 2 + 1, m + 1, r, i, val)
    #         seg[o] = max(seg[o * 2], seg[o * 2 + 1])
    #
    #     # 查询 [0,R] 中的最大值
    #     def query(o: int, l: int, r: int, R: int) -> int:
    #         if r <= R:
    #             return seg[o]
    #         m = (l + r) // 2
    #         if R <= m:
    #             return query(o * 2, l, m, R)
    #         return max(seg[o * 2], query(o * 2 + 1, m + 1, r, R))
    #
    #     obstacles = SortedList([0, mx])  # 哨兵
    #     ans = []
    #     for q in queries:
    #         x = q[1]
    #         i = obstacles.bisect_left(x)
    #         pre = obstacles[i - 1]  # x 左侧最近障碍物的位置
    #         if q[0] == 1:
    #             nxt = obstacles[i]  # x 右侧最近障碍物的位置
    #             obstacles.add(x)
    #             update(1, 0, mx, x, x - pre)  # 更新 d[x] = x - pre
    #             update(1, 0, mx, nxt, nxt - x)  # 更新 d[nxt] = nxt - x
    #         else:
    #             # 最大长度要么是 [0,pre] 中的最大 d，要么是 [pre,x] 这一段的长度
    #             max_gap = max(query(1, 0, mx, pre), x - pre)
    #             ans.append(max_gap >= q[2])
    #     return ans

    # 4. 树状数组解法
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = 50000
        st = SortedList([0, mx])
        for q in queries:
            if q[0] == 1:
                st.add(q[1])

        bt = [0] * (mx + 1)

        def update(x: int, v: int) -> None:
            while x < len(bt):
                if v > bt[x]:
                    bt[x] = v
                x += x & -x

        def query(x: int) -> int:
            res = 0
            while x > 0:
                if bt[x] > res:
                    res = bt[x]
                x -= x & -x
            return res

        pre = 0
        for x in st:
            if x == 0:
                continue
            update(x, x - pre)
            pre = x

        ans = []
        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]
                idx = st.bisect_left(x)
                if idx < len(st) and st[idx] == x:
                    pre_val = x
                else:
                    pre_val = st[idx - 1]
                max_space = query(pre_val)
                max_space = max(max_space, x - pre_val)
                ans.append(max_space >= sz)
            else:
                x = q[1]
                idx = st.bisect_left(x)
                pre_val = st[idx - 1]
                nxt = st[idx + 1]
                update(nxt, nxt - pre_val)
                st.discard(x)

        return ans[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.getResults([[1,2],[2,3,3],[2,3,1],[2,2,2]]))
    print(s.getResults([[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]))
