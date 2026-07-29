""" 3518. 最小回文排列 II     困难
给你一个 回文 字符串 s 和一个整数 k。
返回 s 的按字典序排列的 第 k 小 回文排列。如果不存在 k 个不同的回文排列，则返回空字符串。
注意： 产生相同回文字符串的不同重排视为相同，仅计为一次。
如果一个字符串从前往后和从后往前读都相同，那么这个字符串是一个 回文 字符串。
排列 是字符串中所有字符的重排。
如果字符串 a 按字典序小于字符串 b，则表示在第一个不同的位置，a 中的字符比 b 中的对应字符在字母表中更靠前。
如果在前 min(a.length, b.length) 个字符中没有区别，则较短的字符串按字典序更小。

示例 1：输入： s = "abba", k = 2;     输出： "baab"
解释："abba" 的两个不同的回文排列是 "abba" 和 "baab"。
按字典序，"abba" 位于 "baab" 之前。由于 k = 2，输出为 "baab"。

示例 2：输入： s = "aa", k = 2;   输出： ""
解释：仅有一个回文排列："aa"。由于 k = 2 超过了可能的排列数，输出为空字符串。

示例 3：输入： s = "bacab", k = 1;    输出： "abcba"
解释："bacab" 的两个不同的回文排列是 "abcba" 和 "bacab"。
按字典序，"abcba" 位于 "bacab" 之前。由于 k = 1，输出为 "abcba"。

提示：
1 <= s.length <= 10^4
s 由小写英文字母组成。
保证 s 是回文字符串。
1 <= k <= 10^6
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-28.md

"""
from collections import Counter
from string import ascii_lowercase


def smallestPalindrome(s: str, k: int) -> str:
    # # 解法一
    # n = len(s)
    # half_len = n // 2
    #
    # # 用数组统计左半部分字符频率（索引 0-25 对应 a-z）
    # cnt = [0] * 26
    # for ch in s[:half_len]:
    #     cnt[ord(ch) - ord('a')] += 1
    # #
    # # 预计算阶乘表：fact[i] = i!，避免重复计算大数阶乘
    # fact = [1] * (half_len + 1)
    # for i in range(1, half_len + 1):
    #     fact[i] = fact[i - 1] * i
    #
    # # 定义内部函数：计算给定字符计数的不同排列数
    # # 公式：排列数 = length! / (cnt1! × cnt2! × ... × cntk!)
    # def calc_perms(length: int, counter: list) -> int:
    #     res = fact[length]
    #     for v in counter:
    #         res //= fact[v]
    #     return res
    #
    # # 计算左半部分的所有可能排列数
    # total_perms = calc_perms(half_len, cnt)
    # # 如果总排列数都不够 k，直接返回空字符串（无解）
    # if k > total_perms:
    #     return ""
    #
    # # 用于存储构造出的左半部分字符列表
    # half = []
    # # 剩余待确定的位置数量（初始为左半部分总长度）
    # remaining_length = half_len
    # # 当前剩余的排列总数（初始为全部排列数）
    # current_perms = total_perms
    #
    # # 逐位确定左半部分的每个字符（从左到右）
    # for i in range(half_len):
    #     # 按字典序尝试每个可能的字符（a-z）
    #     for j in range(26):
    #         if cnt[j] == 0:
    #             continue
    #
    #         # 【核心公式】增量计算：如果这一位放字符 c，剩余位置的排列数
    #         # 数学推导：new_perms = current_perms × cnt[c] / remaining_length
    #         # 原理：在所有排列中，以字符 c 开头的比例是 cnt[c]/remaining_length
    #         new_perms = current_perms * cnt[j] // remaining_length
    #
    #         # 判断第 k 个排列是否在以 c 开头的这一批里
    #         if k <= new_perms:
    #             # 是的！选择字符 c 作为当前位置
    #             half.append(ascii_lowercase[j])
    #             # 更新状态：c 用掉一个，剩余长度减 1，排列数更新
    #             cnt[j] -= 1
    #             remaining_length -= 1
    #             current_perms = new_perms
    #             # 跳出内层循环，继续确定下一位
    #             break
    #
    #         else:
    #             # 不在以 c 开头的这批里，跳过这 entire 批排列
    #             k -= new_perms  # 减去这批排列的数量，继续在后面找
    #
    # left = ''.join(half)
    # mid = s[n//2] if n % 2 else ''
    # return ''.join(left + mid + left[::-1])

    # 解法二
    n = len(s)
    half_len = n // 2

    cnt = [0] * 26
    for ch in s[:half_len]:
        cnt[ord(ch) - ord('a')] += 1

    # 组合数计算：用组合数分步计算 + 截断优化
    def comb(n: int, m: int) -> int:
        m = min(m, n - m)  # 优化：C(n,m) = C(n, n-m)，选小的算得快
        res = 1
        for i in range(1, m + 1):
            res = res * (n + 1 - i) // i
            if res >= k:   # 【关键优化】太大了就截断
                return k
        return res

    # 计算长度为 sz 的字符串的排列个数
    def perm(sz: int) -> int:
        res = 1
        for c in cnt:
            if c == 0:
                continue
            # 先从 sz 个里面选 c 个位置填当前字母
            res *= comb(sz, c)
            if res >= k:  # 太大了
                return k
            # 从剩余位置中选位置填下一个字母
            sz -= c
        return res

    # k 太大
    if perm(half_len) < k:
        return ""

    # 构造回文串的左半部分
    half = [''] * half_len
    for i in range(half_len):
        for j in range(26):
            if cnt[j] == 0:
                continue

            # 正确的做法：先假设选了 j，计算排列数，不对就恢复
            cnt[j] -= 1  # 先减
            p = perm(half_len - i - 1)  # 再算
            if k <= p:
                half[i] = ascii_lowercase[j]
                break
            else:
                k -= p  # k 太大，要填更大的字母（类似搜索树剪掉了一个大小为 p 的子树）
                cnt[j] += 1  # 恢复！

    left = ''.join(half)
    mid = s[n//2] if n % 2 else ''
    return ''.join(left + mid + left[::-1])


if __name__ == '__main__':
    print(smallestPalindrome(s="abba", k=2))
    print(smallestPalindrome(s="aa", k=2))
    print(smallestPalindrome(s="bacab", k=1))
    print(smallestPalindrome(s="babab", k=2))
