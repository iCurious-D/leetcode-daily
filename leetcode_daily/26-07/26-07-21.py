""" 3499. 操作后最大活跃区段数 I  中等
给你一个长度为 n 的二进制字符串 s，其中：
'1' 表示一个 活跃 区段。'0' 表示一个 非活跃 区段。
你可以执行 最多一次操作 来最大化 s 中的活跃区段数量。在一次操作中，你可以：
将一个被 '0' 包围的连续 '1' 区块转换为全 '0'。然后，将一个被 '1' 包围的连续 '0' 区块转换为全 '1'。
返回在执行最优操作后，s 中的 最大 活跃区段数。
注意：处理时需要在 s 的两侧加上 '1' ，即 t = '1' + s + '1'。这些加上的 '1' 不会影响最终的计数。

示例 1：输入： s = "01";  输出： 1
解释：因为没有被 '0' 包围的 '1' 区块，因此无法进行有效操作。最大活跃区段数为 1。

示例 2：输入： s = "0100";    输出： 4
解释：字符串 "0100" → 两端加上 '1' 后得到 "101001" 。
选择 "0100"，"101001" → "100001" → "111111" 。
最终的字符串去掉两端的 '1' 后为 "1111" 。最大活跃区段数为 4。

示例 3：输入： s = "1000100"; 输出： 7
解释：字符串 "1000100" → 两端加上 '1' 后得到 "110001001" 。
选择 "000100"，"110001001" → "110000001" → "111111111"。
最终的字符串去掉两端的 '1' 后为 "1111111"。最大活跃区段数为 7。

示例 4：输入： s = "01010";   输出： 4
解释：字符串 "01010" → 两端加上 '1' 后得到 "1010101"。
选择 "010"，"1010101" → "1000101" → "1111101"。
最终的字符串去掉两端的 '1' 后为 "11110"。最大活跃区段数为 4。

提示：
1 <= n == s.length <= 10^5
s[i] 仅包含 '0' 或 '1'
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-21.md

"""
from math import inf
from itertools import groupby


def maxActiveSectionsAfterTrade(s: str) -> int:
    # n = len(s)
    # cnt1 = s.count('1')
    # zero_blocks = []
    # i = 0
    # while i < n:
    #     start = i
    #     while i < n and s[i] == s[start]:
    #         i += 1
    #     if s[start] == '0':
    #         zero_blocks.append(i - start)
    # m = len(zero_blocks)
    # if m < 2:
    #     return cnt1
    # best_gain = 0
    # for i in range(m - 1):
    #     best_gain = max(best_gain, zero_blocks[i] + zero_blocks[i + 1])
    # return cnt1 + best_gain

    # cnt1 = s.count('1')
    # n = len(s)
    # i = 0
    # best_gain = 0
    # pre0 = -inf
    # while i < n:
    #     start = i
    #     while i < n and s[i] == s[start]:
    #         i += 1
    #     if s[start] == '0':
    #         cur = i - start
    #         best_gain = max(best_gain, cur + pre0)
    #         pre0 = cur
    # return cnt1 + best_gain

    # total1 = mx = cnt = 0
    # # pre0 = 0
    # pre0 = -inf
    # for i, b in enumerate(s):
    #     cnt += 1
    #     if i == len(s) - 1 or b != s[i + 1]:
    #         if b == '1':
    #             total1 += cnt
    #         else:
    #             mx = max(mx, pre0 + cnt)
    #             pre0 = cnt
    #         cnt = 0
    # return total1 + mx

    total1 = 0
    mx = 0
    pre0 = -inf
    for char, group in groupby(s):
        length = sum(1 for _ in group)
        if char == '1':
            total1 += length
        else:
            mx = max(mx, pre0 + length)
            pre0 = length
    return total1 + mx


if __name__ == '__main__':
    # print(max(0, -inf + 1))  # 0
    print(maxActiveSectionsAfterTrade(s="01"))
    print(maxActiveSectionsAfterTrade(s="0100"))
    print(maxActiveSectionsAfterTrade(s="1000100"))
    print(maxActiveSectionsAfterTrade(s="01010"))
