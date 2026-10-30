""" 2472. 不重叠回文子字符串的最大数目    困难
给你一个字符串 s 和一个 正 整数 k 。
从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：
每个子字符串的长度 至少 为 k 。每个子字符串是一个 回文串 。
返回最优方案中能选择的子字符串的 最大 数目。
子字符串 是字符串中一个连续的字符序列。

示例 1 ：输入：s = "abaccdbbd", k = 3;    输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
示例 2 ：输入：s = "adbcda", k = 2;       输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。

提示：
1 <= k <= s.length <= 2000
s 仅由小写英文字母组成

"""
from functools import cache


def maxPalindromes(s: str, k: int) -> int:

    # @cache
    # def dfs(i: int) -> int:
    #     if i < k:
    #         return 0
    #     res = dfs(i - 1)
    #     if s[i - k: i] == s[i - k: i][::-1]:
    #         res = max(res, dfs(i - k) + 1)
    #     if i > k and s[i - k - 1: i] == s[i - k - 1: i][::-1]:
    #         res = max(res, dfs(i - k - 1) + 1)
    #     return res
    #
    # return dfs(len(s))

    n = len(s)
    f = [0] * (n+1)
    for i in range(k, n+1):
        f[i] = f[i-1]
        if s[i-k:i] == s[i-k:i][::-1]:
            f[i] = max(f[i], f[i-k] + 1)
        if i > k and s[i-k-1:i] == s[i-k-1:i][::-1]:
            f[i] = max(f[i], f[i-k-1] + 1)
    return f[n]


if __name__ == '__main__':
    print(maxPalindromes("abaccdbbd", 3))
    print(maxPalindromes("adbcda", 2))
    print(maxPalindromes("aaaaa", 1))







