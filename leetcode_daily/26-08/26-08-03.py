""" 1406. 石子游戏 III     困难
Alice 和 Bob 继续他们的石子游戏。几堆石子 排成一行 ，每堆石子都对应一个得分，由数组 stoneValue 给出。
Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。
比赛一直持续到所有石头都被拿走。
每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。
比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。
假设 Alice 和 Bob 都采取 最优策略 。
如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，分数相同返回 "Tie" 。

示例 1：输入：values = [1,2,3,7];     输出："Bob"
解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
示例 2：输入：values = [1,2,3,-9];    输出："Alice"
解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
示例 3：输入：values = [1,2,3,6];     输出："Tie"
解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。

提示：
1 <= stoneValue.length <= 5 * 10^4
-1000 <= stoneValue[i] <= 1000
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-03.md

"""
from functools import cache
from typing import List


def stoneGameIII(stoneValue: List[int]) -> str:
    # n = len(stoneValue)
    #
    # @cache
    # def dfs(i):
    #     if i == n:
    #         return 0
    #
    #     res = float('-inf')
    #     total = 0
    #     for j in range(i, min(i + 3, n)):
    #         total += stoneValue[j]
    #         res = max(res, total - dfs(j + 1))
    #
    #     return res
    #
    # return "Tie" if dfs(0) == 0 else "Alice" if dfs(0) > 0 else "Bob"

    # n = len(stoneValue)
    # i1 = i2 = i3 = 0  # 分别存 dp[i+1], dp[i+2], dp[i+3]
    # for i in range(n - 1, -1, -1):
    #     take = 0
    #     best = float('-inf')
    #     for j in range(1, 4):
    #         if i + j <= n:
    #             take += stoneValue[i + j - 1]
    #             if j == 1:
    #                 opponent = i1
    #             elif j == 2:
    #                 opponent = i2
    #             else:
    #                 opponent = i3
    #             best = max(best, take - opponent)
    #     i1, i2, i3 = best, i1, i2
    #
    # return "Tie" if i1 == 0 else "Alice" if i1 > 0 else "Bob"

    # n = len(stoneValue)
    # f = [-float('inf')] * n + [0]
    # for i in range(n-1, -1, -1):
    #     total = 0
    #     for j in range(i, min(i + 3, n)):
    #         total += stoneValue[j]
    #         f[i] = max(f[i], total - f[j + 1])
    #
    # return "Tie" if f[0] == 0 else "Alice" if f[0] > 0 else "Bob"

    # n = len(stoneValue)
    # f = [0] * (n + 3)
    # suf_sum = 0
    # for i in range(n-1, -1, -1):
    #     suf_sum += stoneValue[i]
    #     f[i] = suf_sum - min(f[i + 1], f[i + 2], f[i + 3])
    #
    # diff = f[0] - (suf_sum - f[0])
    # return "Tie" if diff == 0 else "Alice" if diff > 0 else "Bob"

    n = len(stoneValue)
    suf_sum = f1 = f2 = f3 = 0
    for i in range(n-1, -1, -1):
        suf_sum += stoneValue[i]
        f1, f2, f3 = suf_sum - min(f1, f2, f3), f1, f2

    diff = f1 - (suf_sum - f1)
    return "Tie" if diff == 0 else "Alice" if diff > 0 else "Bob"


if __name__ == '__main__':
    print(stoneGameIII([1, 2, 3, 7]))
    print(stoneGameIII([1, 2, 3, -9]))
    print(stoneGameIII([1, 2, 3, 6]))
    print(stoneGameIII([1, 2, 3, 6, 7, 8, 9]))
    print(stoneGameIII([1, 3, 2, 50, 9, 90, 30, 90, 2, 8, 4]))


    def analyze_alice_first_move(stoneValue):
        """分析Alice第一手的最优选择"""
        n = len(stoneValue)

        # 计算DP数组
        f = [-float('inf')] * (n + 1)
        f[n] = 0

        for i in range(n - 1, -1, -1):
            total = 0
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                f[i] = max(f[i], total - f[j + 1])

        print(f"牌面: {stoneValue}")
        print(f"总和: {sum(stoneValue)}")
        print(f"\nAlice在位置0的三种选择:")

        # 分析Alice在位置0的三种选择
        choices = []
        for take_count in range(1, 4):  # 拿1堆、2堆或3堆
            if take_count <= n:
                taken = stoneValue[:take_count]
                score = sum(taken)
                remaining_diff = f[take_count]  # 剩余局面的差值（从Bob视角）

                # Alice的最终净胜分 = 当前得分 - 对手在剩余局面的净胜分
                alice_diff = score - f[take_count]

                choices.append({
                    'take': take_count,
                    'taken': taken,
                    'score': score,
                    'remaining_f': f[take_count],
                    'alice_diff': alice_diff
                })

                print(f"  拿{take_count}堆: {taken}, 得{score}分")
                print(f"    剩余局面f[{take_count}]={f[take_count]}, Alice净胜分={alice_diff}")

        # 找出最优选择
        best_choice = max(choices, key=lambda x: x['alice_diff'])
        print(f"\n✅ Alice最优选择: 拿{best_choice['take']}堆 {best_choice['taken']}")
        print(f"   得分: {best_choice['score']}, 最终净胜分: {best_choice['alice_diff']}")

        # 整体结果
        print(f"\n📊 整体结果:")
        print(f"  Alice最优得分: {(sum(stoneValue) + f[0]) / 2}")
        print(f"  Bob最优得分: {(sum(stoneValue) - f[0]) / 2}")
        print(f"  赢家: {'Tie' if f[0] == 0 else 'Alice' if f[0] > 0 else 'Bob'}")


    # 测试
    analyze_alice_first_move([1, -3, 2, -5, 9, 90, 30, 300, 50, 90, -2, 8, -4])
