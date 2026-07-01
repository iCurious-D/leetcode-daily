""" 1840. 最高建筑高度    困难
在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。
这座城市对这些新建筑有一些规定：每栋建筑的高度必须是一个非负整数。第一栋建筑的高度 必须 是 0 。任意两栋相邻建筑的高度差 不能超过  1 。
除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 restrictions 的形式给出，
其中 restrictions[i] = [idi, maxHeighti] ，表示建筑 idi 的高度 不能超过 maxHeighti 。
题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。
请你返回 最高 建筑能达到的 最高高度 。

示例 1：输入：n = 5, restrictions = [[2,1],[4,1]];  输出：2
解释：上图中的绿色区域为每栋建筑被允许的最高高度。我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。

示例 2：输入：n = 6, restrictions = [];   输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。

示例 3：输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]];  输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。

提示：
2 <= n <= 10^9
0 <= restrictions.length <= min(n - 1, 10^5)
2 <= idi <= n
idi 是 唯一的 。
0 <= maxHeighti <= 10^9
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-20.md

"""
from typing import List
from math import inf


class Solution:
    # def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
    #     heights = [-1] * (n + 1)
    #     heights[1] = 0
    #     for idx, h in restrictions:
    #         heights[idx] = h
    #
    #     # 从前往后推
    #     for i in range(2, n + 1):
    #         if heights[i] == -1 or heights[i] > heights[i - 1] + 1:
    #             heights[i] = heights[i - 1] + 1
    #
    #     # 从后往前推
    #     for i in range(n - 1, 0, -1):
    #         if heights[i] > heights[i + 1] + 1:
    #             heights[i] = heights[i + 1] + 1
    #
    #     return max(heights)

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions += [[1, 0], [n, inf]]
        restrictions.sort(key=lambda a: a[0])  # 按照 id 从小大到大排序

        m = len(restrictions)
        h = [0] * m  # h[i] 表示编号为 id[i] 的建筑的最大高度
        for i in range(1, m):
            h[i] = min(h[i - 1] + restrictions[i][0] - restrictions[i - 1][0], restrictions[i][1])
        for i in range(m - 2, -1, -1):
            h[i] = min(h[i], h[i + 1] + restrictions[i + 1][0] - restrictions[i][0])

        return max(restrictions[i + 1][0] - restrictions[i][0] + h[i] + h[i + 1] for i in range(m - 1)) // 2


if __name__ == '__main__':
    print(Solution().maxBuilding(5, [[2, 1], [4, 1]]))
    print(Solution().maxBuilding(6, []))
    print(Solution().maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
