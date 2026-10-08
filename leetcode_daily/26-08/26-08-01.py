""" 486. 预测赢家   中等
给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。
玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。
每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。
玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。
如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。
你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：输入：nums = [1,5,2];     输出：false
解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。因此，玩家 1 永远不会成为赢家，返回 false 。

示例 2：输入：nums = [1,5,233,7];     输出：true
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-01.md

"""
from functools import cache
from typing import List

def predictTheWinner(nums: List[int]) -> bool:
    # # 暴力模拟：每个状态分裂成两个子状态，时间复杂度：O(2ⁿ)
    # def win(start, end, score_a, score_b, turn):
    #     if start > end:
    #         return score_a >= score_b
    #     if turn:
    #         return (win(start + 1, end, score_a + nums[start], score_b, 0)
    #                 or win(start, end - 1, score_a + nums[end], score_b, 0))
    #     else:
    #         return (win(start + 1, end, score_a, score_b + nums[start], 1)
    #                 and win(start, end - 1, score_a, score_b + nums[end], 1))
    # return win(0, len(nums)-1, 0, 0, 1)

    # 博弈论DP精髓——用相对值代替绝对值，把双人博弈压缩成一维的状态转移
    # 定义 dp(i, j) 为在子数组 nums[i..j] 中，当前玩家相对于对手的净胜分数
    @cache
    def dfs(start: int, end: int) -> int:
        if start == end:
            return nums[start]
        return max(nums[start] - dfs(start + 1, end), nums[end] - dfs(start, end - 1))

    return dfs(0, len(nums) - 1) >= 0

    # n = len(nums)
    # f = [[0] * n for _ in range(n)]
    # for i in range(n-1, -1, -1):
    #     f[i][i] = nums[i]
    #     for j in range(i+1, n):
    #         f[i][j] = max(nums[i] - f[i + 1][j], nums[j] - f[i][j - 1])
    # return f[0][n-1] >= 0

    # # 计算第 i 行时，只用到了第 i+1 行的数据
    # n = len(nums)
    # f = [0] * n
    # for i in range(n-1, -1, -1):
    #     f[i] = nums[i]
    #     for j in range(i+1, n):
    #         f[j] = max(nums[i] - f[j], nums[j] - f[j - 1])
    # return f[n-1] >= 0


if __name__ == '__main__':
    print(predictTheWinner([1, 5, 2]))
    print(predictTheWinner([1, 5, 233, 7]))
    print(predictTheWinner([1, 5, 2, 4, 6]))
    print(predictTheWinner([1, 5, 2, 4, 6, 7]))
    print(predictTheWinner([1, 5, 2, 4, 6, 7, 8]))
    print(predictTheWinner([1, 5, 2, 4, 6, 7, 8, 9]))
    print(predictTheWinner([1, 9, 8, 5, 7, 4, 6, 3, 5]))
    print(predictTheWinner([1, 5, 233, 8, 2, 6, 4, 3]))

