""" 3751. 范围内总波动值 I
给你两个整数 num1 和 num2，表示一个 闭 区间 [num1, num2]。
一个数字的 波动值 定义为该数字中 峰 和 谷 的总数：
    如果一个数位 严格大于 其两个相邻数位，则该数位为 峰。
    如果一个数位 严格小于 其两个相邻数位，则该数位为 谷。
    数字的第一个和最后一个数位 不能 是峰或谷。
    任何少于 3 位的数字，其波动值均为 0。
返回范围 [num1, num2] 内所有数字的波动值之和。

示例 1：输入： num1 = 120, num2 = 130  输出： 3
解释：在范围 [120, 130] 内：
120：中间数位 2 是峰，波动值 = 1。
121：中间数位 2 是峰，波动值 = 1。
130：中间数位 3 是峰，波动值 = 1。
范围内所有其他数字的波动值均为 0。因此，总波动值为 1 + 1 + 1 = 3。

示例 2：输入： num1 = 198, num2 = 202  输出： 3
解释：在范围 [198, 202] 内：
198：中间数位 9 是峰，波动值 = 1。
201：中间数位 0 是谷，波动值 = 1。
202：中间数位 0 是谷，波动值 = 1。
范围内所有其他数字的波动值均为 0。因此，总波动值为 1 + 1 + 1 = 3。

示例 3：输入： num1 = 4848, num2 = 4848  输出： 2
解释：数字 4848：第二个数位 8 是峰，第三个数位 4 是谷，波动值为 2。

提示：
1 <= num1 <= num2 <= 10^5
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-04.md

"""
from typing import Tuple


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 解法一
        # res = 0
        # for i in range(num1, num2 + 1):
        #     s = str(i)
        #     for a, b, c in zip(s, s[1:], s[2:]):
        #         if a > b < c:
        #             res += 1
        #         elif a < b > c:
        #             res += 1
        # return res

        # #  计算 [0, num] 内所有数字的波动值之和
        # def solve(num: int) -> int:
        #     # 如果少于 3 的数字波动值 0
        #     if num < 100:
        #         return 0
        #     s = str(num)
        #     n = len(s)
        #
        #     # 记忆化搜索使用两个独立的数组
        #     # memo_cnt[pos][x][y]：当前位为 pos 位，且前两位为 x, y 的合法填充方案数
        #     memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]
        #     # memo_sum[pos][x][y]：当前位为 pos 位，且左边两位为 x, y 的波动值
        #     memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]
        #
        #     from functools import lru_cache
        #
        #     @lru_cache(None)
        #     def dfs(pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool):
        #         # 结束位置
        #         if pos == n:
        #             return 1, 0
        #
        #         # 计算当前条件下的填充方案数和波动值
        #         cnt = 0
        #         waviness = 0
        #         up = int(s[pos]) if isLimit else 9
        #         for digit in range(up + 1):
        #             newLeading = isLeading and (digit == 0)
        #             # 前一个数字更新为 curr
        #             newPrev = curr
        #             # 当前数字更新为 digit
        #             newCurr = -1 if newLeading else digit
        #             subCnt, subSum = dfs(pos + 1, newPrev, newCurr,
        #                                  isLimit and (digit == up), newLeading)
        #             # 不包含前导零时才计算波动值
        #             if not newLeading and prev >= 0 and curr >= 0:
        #                 # 数位为峰或为谷时，更新当前的波动值
        #                 if (prev < curr and curr > digit) or (prev > curr and curr < digit):
        #                     waviness += subCnt
        #
        #             cnt += subCnt
        #             waviness += subSum
        #
        #         return cnt, waviness
        #
        #     _, totalSum = dfs(0, -1, -1, True, True)
        #     return totalSum
        #
        # return solve(num2) - solve(num1 - 1)


        # # 解法二
        # low_s = list(map(int, str(num1)))  # 避免在 dfs 中频繁调用 int()
        # high_s = list(map(int, str(num2)))
        # n = len(high_s)
        # diff_lh = n - len(low_s)
        #
        # @cache
        # def dfs(i: int, waviness: int, last_cmp: int, last_digit: int, limit_low: bool, limit_high: bool) -> int:
        #     if i == n:
        #         return waviness
        #
        #     lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
        #     hi = high_s[i] if limit_high else 9
        #
        #     res = 0
        #     is_num = not limit_low or i > diff_lh  # 前面是否填过数字
        #     for d in range(lo, hi + 1):
        #         # 当前填的数不是最高位，c 才有意义
        #         c = (d > last_digit) - (d < last_digit) if is_num else 0
        #         w = waviness
        #         if c * last_cmp < 0:  # 形成了一个峰或谷
        #             w += 1
        #         res += dfs(i + 1, w, c, d, limit_low and d == lo, limit_high and d == hi)
        #     return res
        #
        # return dfs(0, 0, 0, 0, True, True)

        # 解法三
        low_s = list(map(int, str(num1)))  # 避免在 dfs 中频繁调用 int()
        high_s = list(map(int, str(num2)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        from functools import cache
        # dfs 返回两个数：子树波动值总和，子树合法数字个数
        @cache
        def dfs(i: int, last_cmp: int, last_digit: int, limit_low: bool, limit_high: bool) -> Tuple[int, int]:
            if i == n:
                return 0, 1  # 本题无特殊约束，能递归到终点的都是合法数字

            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9

            waviness_sum = num_cnt = 0
            is_num = not limit_low or i > diff_lh  # 前面是否填过数字
            for d in range(lo, hi + 1):
                # 当前填的数不是最高位，c 才有意义
                c = (d > last_digit) - (d < last_digit) if is_num else 0
                sub_waviness_sum, sub_num_cnt = dfs(i + 1, c, d, limit_low and d == lo, limit_high and d == hi)
                waviness_sum += sub_waviness_sum  # 累加子树的波动值
                num_cnt += sub_num_cnt  # 累加子树的合法数字个数
                if c * last_cmp < 0:  # 形成了一个峰或谷
                    waviness_sum += sub_num_cnt  # 这个峰谷会出现在 sub_num_cnt 个数字中
            return waviness_sum, num_cnt

        return dfs(0, 0, 0, True, True)[0]


if __name__ == '__main__':
    print(Solution().totalWaviness(num1 = 120, num2 = 130))
    print(Solution().totalWaviness(num1 = 198, num2 = 202))
    print(Solution().totalWaviness(num1 = 4848, num2 = 4848))