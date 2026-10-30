""" 115. 不同的子序列     困难
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
测试用例保证结果在 32 位有符号整数范围内。

示例 1：输入：s = "rabbbit", t = "rabbit";    输出：3
解释：如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit  /  rabbbit/    rabbbit /   rabbbit
示例 2：输入：s = "babgbag", t = "bag";       输出：5
解释：如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag /   babgbag /   babgbag /   babgbag /   babgbag

提示：
1 <= s.length, t.length <= 1000
s 和 t 由英文字母组成

"""
from functools import cache


def numDistinct(s: str, t: str) -> int:
    @cache
    def dfs(i, j):
        if i < j:
            return 0
        if j < 0:
            return 1
        res = dfs(i - 1, j)
        if s[i] == t[j]:
            res += dfs(i - 1, j - 1)
        return res

    return dfs(len(s) - 1, len(t) - 1)

    # n, m = len(s), len(t)
    # dp = [[0] * (m + 1) for _ in range(n + 1)]
    # for i in range(n + 1):
    #     dp[i][0] = 1
    #
    # for i, x in enumerate(s):
    #     for j in range(max(0, m-n+i), min(m, i+1)):
    #         dp[i+1][j+1] = dp[i][j+1]
    #         if x == t[j]:
    #             dp[i+1][j+1] += dp[i][j]
    #
    # return dp[n][m]


if __name__ == '__main__':
    print(numDistinct("rabbbit", "rabbit"))
    print(numDistinct("babgbag", "bag"))
    print(numDistinct("aaa", "a"))





