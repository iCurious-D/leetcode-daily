from functools import cache
from typing import List


def predictTheWinnerWithTrace(nums: List[int]) -> bool:
    @cache
    def dfs(start: int, end: int) -> int:
        if start == end:
            return nums[start]
        return max(nums[start] - dfs(start + 1, end), nums[end] - dfs(start, end - 1))

    # 追踪每一步的选择
    def trace(start: int, end: int, turn: int = 1, score_a: int = 0, score_b: int = 0):
        if start > end:
            print(
                f"游戏结束! 玩家1得分: {score_a}, 玩家2得分: {score_b}, 结果: {'玩家1赢' if score_a >= score_b else '玩家2赢'}")
            return

        left_val = nums[start]
        right_val = nums[end]
        left_net = left_val - dfs(start + 1, end)
        right_net = right_val - dfs(start, end - 1)

        if left_net >= right_net:
            choice = left_val
            next_start, next_end = start + 1, end
            side = "左"
        else:
            choice = right_val
            next_start, next_end = start, end - 1
            side = "右"

        if turn == 1:
            new_score_a = score_a + choice
            print(f"回合{turn}: 玩家1选[{side}]的{choice}, 当前得分: 玩家1={new_score_a}, 玩家2={score_b}")
            trace(next_start, next_end, 2, new_score_a, score_b)
        else:
            new_score_b = score_b + choice
            print(f"回合{turn}: 玩家2选[{side}]的{choice}, 当前得分: 玩家1={score_a}, 玩家2={new_score_b}")
            trace(next_start, next_end, 1, score_a, new_score_b)

    net_win = dfs(0, len(nums) - 1)
    print(f"数组: {nums}")
    print(f"净胜分: {net_win}")
    print(f"先手能否赢: {net_win >= 0}\n")
    print("=== 博弈过程 ===")
    trace(0, len(nums) - 1, 1, 0, 0)
    print()

    return net_win >= 0


# 测试你的案例
predictTheWinnerWithTrace(  [1, 10, 1, 10, 1, 10, 1, 10, 100])