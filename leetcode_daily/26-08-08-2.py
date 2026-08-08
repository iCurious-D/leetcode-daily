""" 2565. 最少得分子序列   困难
给你两个字符串 s 和 t 。
你可以从字符串 t 中删除任意数目的字符。
如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：
令 left 为删除字符中的最小下标。
令 right 为删除字符中的最大下标。
字符串的得分为 right - left + 1 。
请你返回使 t 成为 s 子序列的最小得分。
一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。
（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。

示例 1：输入：s = "abacaba", t = "bzaa";  输出：1
解释：这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。
示例 2：输入：s = "cde", t = "xyz";   输出：3
解释：这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。

提示：
1 <= s.length, t.length <= 10^5
s 和 t 都只包含小写英文字母。

"""

def minimumScore(s: str, t: str) -> int:
    n, m = len(s), len(t)
    suf = [m] * (n + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        if s[i] == t[j]:
            j -= 1
        if j < 0:  # t 是 s 的子序列
            return 0
        suf[i] = j + 1

    ans = suf[0]  # 删除 t[:suf[0]]
    j = 0
    for i, c in enumerate(s):
        if c == t[j]:  # 注意上面判断了 t 是 s 子序列的情况，这里 j 不会越界
            j += 1
            ans = min(ans, suf[i + 1] - j)  # 删除 t[j:suf[i+1]]
    return ans

    # m, n = len(s), len(t)
    #
    # # pre[i]：匹配 t 前 i 个字符，在 s 中的最小结尾下标
    # pre = [-1] * (n + 1)
    # j = 0
    # for i, ch in enumerate(s):
    #     if j < n and ch == t[j]:
    #         j += 1
    #         pre[j] = i
    # for k in range(j + 1, n + 1):
    #     pre[k] = m  # 无法匹配，设为无穷大
    #
    # # suf[j]：匹配 t 后 j 个字符，在 s 中的最大起始下标
    # suf = [-1] * (n + 1)
    # suf[0] = m
    # j = n - 1
    # for i in range(m - 1, -1, -1):
    #     if j >= 0 and s[i] == t[j]:
    #         suf[n - j] = i
    #         j -= 1
    #
    # # 寻找最大保留长度 i + j
    # max_keep = 0
    # j = n
    # for i in range(n + 1):
    #     # j 需要满足 i + j <= n 且 pre[i] < suf[j]
    #     while j >= 0 and (i + j > n or pre[i] >= suf[j]):
    #         j -= 1
    #     if j >= 0:
    #         max_keep = max(max_keep, i + j)
    #
    # return n - max_keep


if __name__ == '__main__':
    print(minimumScore("abacaba", "bzaa"))
    print(minimumScore("cde", "xyz"))
    print(minimumScore("abc", "ac"))










