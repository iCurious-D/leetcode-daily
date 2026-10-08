""" 1563. 石子游戏 V    困难
几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
游戏中的每一轮：
Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。
Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。
下一轮从剩下的那一行开始。
只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
返回 Alice 能够获得的最大分数 。

示例 1：输入：stoneValue = [6,2,3,4,5,5];     输出：18
解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。

示例 2：输入：stoneValue = [7,7,7,7,7,7,7];   输出：28
示例 3：输入：stoneValue = [4];               输出：0

提示：
1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-17.md

"""
from bisect import bisect_left
from math import inf
from typing import List
from itertools import accumulate
from functools import cache


def stoneGameV(stoneValue: List[int]) -> int:
    # 解法一：递归
    s = list(accumulate(stoneValue, initial=0))

    # 不剪枝
    # @cache
    # def dfs(i: int, j: int) -> int:
    #     if j - i == 1:
    #         return 0
    #
    #     res = 0
    #     for k in range(i+1, j):
    #         sum_l = s[k] - s[i]
    #         sum_r = s[j] - s[k]
    #         if sum_l < sum_r:
    #             score = sum_l + dfs(i, k)
    #         elif sum_l > sum_r:
    #             score = sum_r + dfs(k, j)
    #         else:
    #             score = sum_l + max(dfs(i, k), dfs(k, j))
    #         res = max(res, score)
    #     return res

    # 剪枝优化
    @cache
    def dfs(i: int, j: int) -> int:
        if j - i == 1:
            return 0

        total = s[j] - s[i]
        res = 0

        # 二分找最平衡的分割点：最后一个使 sum_l < total/2 的 k
        # 即 s[k] - s[i] < total / 2 → s[k] < s[i] + total / 2
        k = bisect_left(s, s[i] + (total + 1) // 2, i + 1, j + 1) - 1
        k = max(i, min(k, j - 1))

        # 向右扫描：从平衡点往右，sum_r 越来越小
        m = k
        while m < j:
            sum_l = s[m + 1] - s[i]
            sum_r = s[j] - s[m + 1]
            if 2 * sum_r <= res:  # sum_r 太小，不可能更优 → 终止
                break
            if sum_l < sum_r:
                cand = sum_l + dfs(i, m + 1)
            elif sum_l > sum_r:
                cand = sum_r + dfs(m + 1, j)
            else:
                cand = sum_l + max(dfs(i, m + 1), dfs(m + 1, j))
            res = max(res, cand)
            m += 1

        # 向左扫描：从平衡点往左，sum_l 越来越小
        m = k - 1
        while m >= i:
            sum_l = s[m + 1] - s[i]
            sum_r = s[j] - s[m + 1]
            if 2 * sum_l <= res:  # sum_l 太小，不可能更优 → 终止
                break
            if sum_l < sum_r:
                cand = sum_l + dfs(i, m + 1)
            elif sum_l > sum_r:
                cand = sum_r + dfs(m + 1, j)
            else:
                cand = sum_l + max(dfs(i, m + 1), dfs(m + 1, j))
            res = max(res, cand)
            m -= 1
        return res

    return dfs(0, len(stoneValue))


    # # 解法二：递推
    # n = len(stoneValue)
    # s = [0] + list(accumulate(stoneValue))
    # f = [[0] * n for _ in range(n)]
    # for i in range(n-2, -1, -1):
    #     for j in range(i+2, n+1):
    #         for k in range(i+1, j):
    #             sum_l = s[k] - s[i]
    #             sum_r = s[j] - s[k]
    #             if sum_l < sum_r:
    #                 score = sum_l + f[i][k]
    #             elif sum_l > sum_r:
    #                 if sum_r * 2 <= f[i][j]:
    #                     break
    #                 score = sum_r + f[k][j]
    #             else:
    #                 score = sum_l + max(f[i][k], f[k][j])
    #             f[i][j] = max(f[i][j], score)
    # return f[0][n]

    # # 解法三
    # n = len(stoneValue)
    # s = list(accumulate(stoneValue, initial=0))
    # f = [[0] * (n + 1) for _ in range(n)]
    # suf_max = [[-inf] * (n + 1) for _ in range(n + 1)]
    #
    # for i in range(n - 1, -1, -1):
    #     suf_max[i][i + 1] = -s[i]  # f[i][i+1] - s[i] = 0 - s[i] = -s[i]
    #     pre_max = 0
    #     k = i + 1
    #     for j in range(i + 2, n + 1):
    #         while s[k] - s[i] <= s[j] - s[k]:
    #             pre_max = max(pre_max, f[i][k] + s[k])
    #             k += 1
    #         # 循环结束后 s[k] - s[i] > s[j] - s[k]
    #         q = k if s[k - 1] - s[i] != s[j] - s[k - 1] else k - 1
    #         f[i][j] = max(pre_max - s[i], suf_max[q][j] + s[j])
    #         suf_max[i][j] = max(suf_max[i + 1][j], f[i][j] - s[i])
    #
    # return f[0][n]

    # # 解法三再优化：
    # n = len(stoneValue)
    # s = list(accumulate(stoneValue, initial=0))  # stoneValue 的前缀和
    # f = [0] * (n + 1)
    # suf_max = [[-inf] * (n + 1) for _ in range(n + 1)]
    #
    # for i in range(n - 1, -1, -1):
    #     suf_max[i][i + 1] = -s[i]  # f[i][i+1] - s[i] = 0 - s[i] = -s[i]
    #     pre_max = 0
    #     k = i + 1
    #     for j in range(i + 2, n + 1):
    #         while s[k] - s[i] <= s[j] - s[k]:
    #             pre_max = max(pre_max, f[k] + s[k])
    #             k += 1
    #         # 循环结束后 s[k] - s[i] > s[j] - s[k]
    #         q = k if s[k - 1] - s[i] != s[j] - s[k - 1] else k - 1
    #         f[j] = max(pre_max - s[i], suf_max[q][j] + s[j])
    #         suf_max[i][j] = max(suf_max[i + 1][j], f[j] - s[i])
    #
    # return f[n]

    # # 解法四
    # n = len(stoneValue)
    # pre = [0] * (n + 1)
    # for i, v in enumerate(stoneValue):
    #     pre[i + 1] = pre[i] + v
    #
    # @lru_cache(None)
    # def dp(l, r):
    #     if l == r:
    #         return 0
    #     total = pre[r + 1] - pre[l]
    #     best = 0
    #
    #     k = bisect_left(pre, pre[l] + (total + 1) // 2, l + 1, r + 2) - 1
    #     k = max(l, min(k, r - 1))
    #
    #     i = k
    #     while i < r:
    #         left = pre[i + 1] - pre[l]
    #         right = total - left
    #         if 2 * right <= best:
    #             break
    #         cand = (left + dp(l, i)) if left < right else \
    #                (right + dp(i + 1, r)) if left > right else \
    #                max(left + dp(l, i), right + dp(i + 1, r))
    #         best = max(best, cand)
    #         i += 1
    #
    #     i = k - 1
    #     while i >= l:
    #         left = pre[i + 1] - pre[l]
    #         right = total - left
    #         if 2 * left <= best:
    #             break
    #         cand = (left + dp(l, i)) if left < right else \
    #                (right + dp(i + 1, r)) if left > right else \
    #                max(left + dp(l, i), right + dp(i + 1, r))
    #         best = max(best, cand)
    #         i -= 1
    #
    #     return best
    #
    # return dp(0, n - 1)


if __name__ == '__main__':
    print(stoneGameV([6,2,3,4,5,5]))
    print(stoneGameV([7,7,7,7,7,7,7]))
    print(stoneGameV([4]))












