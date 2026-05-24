""" 1340. 跳跃游戏 V
给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：
i + x ，其中 i + x < arr.length 且 0 < x <= d 。
i - x ，其中 i - x >= 0 且 0 < x <= d 。
除此以外，你从下标 i 跳到下标 j 需要满足：
arr[i] > arr[j] 且 arr[i] > arr[k] ，
其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。
你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。
请注意，任何时刻你都不能跳到数组的外面。
=========================================================================

题解路径：. / leetcode_daily_stories / 26-05-24.md

"""
from typing import List
from functools import cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # n = len(arr)
        # memo = [-1] * n  # 记忆化数组，-1 表示未计算
        #
        # def dfs(i: int) -> int:
        #     if memo[i] != -1:
        #         return memo[i]  # 如果已经算过，直接返回
        #
        #     max_steps = 1  # 至少能访问自己
        #
        #     # 尝试向右跳
        #     for x in range(1, d + 1):
        #         j = i + x
        #         if j >= n:  # 越界，停止
        #             break
        #         if arr[j] >= arr[i]:  # 遇到比自己高或相等的，被遮挡，停止
        #             break
        #         max_steps = max(max_steps, dfs(j) + 1)  # 递归计算
        #
        #     # 尝试向左跳
        #     for x in range(1, d + 1):
        #         j = i - x
        #         if j < 0:  # 越界，停止
        #             break
        #         if arr[j] >= arr[i]:  # 遇到比自己高或相等的，被遮挡，停止
        #             break
        #         max_steps = max(max_steps, dfs(j) + 1)  # 递归计算
        #
        #     memo[i] = max_steps  # 记录结果
        #     return max_steps
        #
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, dfs(i))  # 枚举所有起点
        #
        # return ans

        n = len(arr)

        @cache  # 缓存装饰器，自动处理记忆化
        def dfs(i: int) -> int:
            res = 1

            # 往左跳
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)

            # 往右跳
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, dfs(j) + 1)

            return res

        # 枚举起点
        return max(dfs(i) for i in range(n))


if __name__ == '__main__':
    print(Solution().maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
    print(Solution().maxJumps([3, 3, 3, 3, 3], 3))
    print(Solution().maxJumps([7, 6, 5, 4, 3, 2, 1], 1))


