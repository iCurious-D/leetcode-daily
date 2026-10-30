""" 3414. 不重叠区间的最大得分    困难
给你一个二维整数数组 intervals，其中 intervals[i] = [li, ri, weighti]。
区间 i 的起点为 li，终点为 ri，权重为 weighti。你最多可以选择 4 个互不重叠 的区间。
所选择区间的 得分 定义为这些区间权重的总和。
返回一个至多包含 4 个下标且 字典序最小 的数组，表示从 intervals 中选中的互不重叠且得分最大的区间。
如果两个区间没有任何重叠点，则称二者 互不重叠 。特别地，如果两个区间共享左边界或右边界，也认为二者重叠。

示例 1：输入： intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]; 输出： [2,3]
解释：可以选择下标为 2 和 3 的区间，其权重分别为 5 和 3。
示例 2：输入： intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]; 输出： [1,3,5,6]
解释：可以选择下标为 1、3、5 和 6 的区间，其权重分别为 7、6、3 和 5。

提示：
1 <= intervals.length <= 5 * 10^4
intervals[i].length == 3
intervals[i] = [li, ri, weighti]
1 <= li <= ri <= 10^9
1 <= weighti <= 10^9

"""
from bisect import bisect_left
from typing import List

def maximumWeight(intervals: List[List[int]]) -> List[int]:
    # 解法一
    n = len(intervals)
    # 按右端点排序，同时保存原始下标
    arr = sorted((r, l, w, idx) for idx, (l, r, w) in enumerate(intervals))
    ends = [r for r, l, w, idx in arr]

    # 返回更优的状态：先比较得分，再比较字典序
    def better(a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a[0] != b[0]:
            return a if a[0] > b[0] else b
        return a if a[1] < b[1] else b

    # dp[i][k]：前 i 个区间中恰好选 k 个
    # None 表示无法实现
    dp = [[None] * 5 for _ in range(n + 1)]
    dp[0][0] = (0, ())

    for i, (r, l, w, idx) in enumerate(arr, start=1):
        # 在当前区间之前，右端点严格小于 l 的区间数量
        p = bisect_left(ends, l, 0, i - 1)

        # 不选当前区间
        dp[i] = dp[i - 1].copy()

        for k in range(1, 5):
            prev = dp[p][k - 1]
            if prev is None:
                continue

            # 选当前区间，答案按原始下标升序排列
            indices = tuple(sorted(prev[1] + (idx,)))
            candidate = (prev[0] + w, indices)

            dp[i][k] = better(dp[i][k], candidate)

    ans = None
    for k in range(5):
        ans = better(ans, dp[n][k])

    return list(ans[1])

    # # 解法二
    # arr = sorted((r, l, w, idx) for idx, (l, r, w) in enumerate(intervals))
    # n = len(arr)
    # ends = [item[0] for item in arr]
    #
    # # p[i]：arr[i] 之前，右端点严格小于其左端点的区间数
    # p = [
    #     bisect_left(ends, l, 0, i)
    #     for i, (r, l, w, idx) in enumerate(arr)
    # ]
    #
    # # 存 (-得分, 下标元组)，直接用 min 比较即可：
    # # 得分越大越好；同分时字典序越小越好
    # # 初始为恰好选 0 个，任意前缀都可以实现
    # prev = [(0, ())] * (n + 1)
    # ans = (0, ())
    #
    # for k in range(1, min(4, n) + 1):
    #     cur = [None] * (n + 1)
    #
    #     for i, (r, l, w, idx) in enumerate(arr):
    #         best = cur[i]  # 不选 arr[i]
    #         base = prev[p[i]]
    #
    #         if base is not None:
    #             ids = tuple(sorted(base[1] + (idx,)))
    #             candidate = (base[0] - w, ids)
    #
    #             if best is None or candidate < best:
    #                 best = candidate
    #
    #         cur[i + 1] = best
    #
    #     if cur[n] is None:
    #         # 连 k 个都选不出来，也不可能选更多
    #         break
    #
    #     ans = min(ans, cur[n])
    #     prev = cur
    #
    # return list(ans[1])


if __name__ == '__main__':
    print(maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]))
    print(maximumWeight([[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]))
    print(maximumWeight([[1,5,3],[2,6,2],[4,7,4],[3,4,4],[10,10,1],[5,12,3],[3,5,2]]))



