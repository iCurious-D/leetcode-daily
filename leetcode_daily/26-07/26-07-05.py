""" 1301. 最大得分的路径数目    困难
给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。
在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。
一条路径的 「得分」 定义为：路径上所有数字的和。
请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
如果没有任何路径可以到达终点，请返回 [0, 0] 。

示例 1：输入：board = ["E23","2X2","12S"];    输出：[7,1]
示例 2：输入：board = ["E12","1X1","21S"];    输出：[4,2]
示例 3：输入：board = ["E11","XXX","11S"];    输出：[0,0]

提示：
2 <= board.length == board[i].length <= 100
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-05.md

"""
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        m, n = len(board), len(board[0])

        # 解法一：动态规划
        # dp[i][j] = [最大得分, 方案数]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(m)]
        # 起点初始化
        dp[m - 1][n - 1] = [0, 1]
        # 从右下角往左上角递推
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                # 如果当前位置是障碍，跳过
                if board[i][j] == 'X':
                    continue
                max_score = -1
                max_count = 0
                for x, y in [[i + 1, j], [i, j + 1], [i + 1, j + 1]]:
                    if 0 <= x < m and 0 <= y < n and dp[x][y][0] != -1:
                        score, count = dp[x][y]
                        if score > max_score:
                            max_score, max_count = score, count
                        elif score == max_score:
                            max_count = (max_count + count) % MOD

                # 如果能到达终点
                if max_score != -1:
                    # 计算当前格子的值
                    if board[i][j] == 'E':
                        current_val = 0
                    else:
                        current_val = int(board[i][j])
                    dp[i][j] = [max_score + current_val, max_count % MOD]

        # 如果起点不可达
        if dp[0][0][0] == -1:
            return [0, 0]

        return dp[0][0]

        # 解法二：
        max_sum = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
        ways = [[0] * (n + 1) for _ in range(m + 1)]
        max_sum[0][0] = 0
        ways[0][0] = 1

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'X':
                    continue
                # 左上、正上、正左
                max_sum[i + 1][j + 1] = s = max(max_sum[i][j], max_sum[i][j + 1], max_sum[i + 1][j])
                # 如果路径和相同，则累加方案数（加法原理）
                if max_sum[i][j] == s:
                    ways[i + 1][j + 1] += ways[i][j]
                if max_sum[i][j + 1] == s:
                    ways[i + 1][j + 1] += ways[i][j + 1]
                if max_sum[i + 1][j] == s:
                    ways[i + 1][j + 1] += ways[i + 1][j]
                ways[i + 1][j + 1] %= MOD
                if ch.isdigit():
                    max_sum[i + 1][j + 1] += int(ch)  # 加上当前格子的值

        return [max_sum[m][n], ways[m][n]] if max_sum[m][n] != -float('inf') else [0, 0]



if __name__ == '__main__':
    board = ["E23","2X2","12S"]
    print(Solution().pathsWithMaxScore(board))
    board = ["E12","1X1","21S"]
    print(Solution().pathsWithMaxScore(board))
    board = ["E11","XXX","11S"]
    print(Solution().pathsWithMaxScore(board))
