""" 1140. 石子游戏 II   中等
Alice 和 Bob 继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。
游戏以谁手中的石子最多来决出胜负。
Alice 和 Bob 轮流进行，Alice 先开始。最初，M = 1。
在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
游戏一直持续到所有石子都被拿走。
假设 Alice 和 Bob 都发挥出最佳水平，返回 Alice 可以得到的最大数量的石头。

示例 1：输入：piles = [2,7,9,4,4];    输出：10
解释：如果一开始 Alice 取了一堆，Bob 取了两堆，然后 Alice 再取两堆。Alice 可以得到 2 + 4 + 4 = 10 堆。
如果 Alice 一开始拿走了两堆，那么 Bob 可以拿走剩下的三堆。在这种情况下，Alice 得到 2 + 7 = 9 堆。返回 10，因为它更大。
示例 2:输入：piles = [1,2,3,4,5,100];    输出：104

提示：
1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""
from collections import deque
from functools import cache


def stoneGameII(piles: list[int]) -> int:
    # n = len(piles)
    # for i in range(n-2, -1, -1):
    #     piles[i] += piles[i+1]
    #
    # @cache
    # def dfs(i: int, m: int) -> int:
    #     if i + 2 * m >= n:
    #         return piles[i]
    #     return piles[i] - min(dfs(i+j, max(m, j)) for j in range(1, 2*m+1))
    #
    # return dfs(0, 1)

    n = len(piles)
    f = [[0] * (n + 1) for _ in range(n)]
    col_q = [deque() for _ in range(n + 1)]  # 每列的滑动窗口最小值（窗口向上滑动）

    s = 0
    for i in range(n - 1, -1, -1):
        s += piles[i]
        diag_q = deque()  # 斜向的滑动窗口最小值（窗口向右下滑动）
        for m in range(1, i // 2 + 2):
            if i + m * 2 >= n:  # 全拿
                f[i][m] = s
                continue

            # f[i+1][m] 进入列窗口
            q = col_q[m]
            while q and f[q[-1]][m] >= f[i + 1][m]:
                q.pop()
            q.append(i + 1)

            # 队首离开列窗口
            if q[0] > i + m:
                q.popleft()

            # f[i+m*2-1][m*2-1] 和 f[i+m*2][m*2] 进入斜向窗口
            for x in range(m * 2 - 1, m * 2 + 1):
                while diag_q and f[i + diag_q[-1]][diag_q[-1]] >= f[i + x][x]:
                    diag_q.pop()
                diag_q.append(x)

            # 队首离开斜向窗口
            if diag_q[0] <= m:
                diag_q.popleft()

            f[i][m] = s - min(f[q[0]][m], f[i + diag_q[0]][diag_q[0]])

    return f[0][1]


if __name__ == '__main__':
    print(stoneGameII([2,7,9,4,4]))
    print(stoneGameII([1,2,3,4,5,100]))











