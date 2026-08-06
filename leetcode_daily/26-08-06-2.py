""" 3348. 最小可整除数位乘积 II  困难
给你一个字符串 num ，表示一个 正 整数，同时给你一个整数 t 。
如果一个整数 没有 任何数位是 0 ，那么我们称这个整数是 无零 数字。
请你返回一个字符串，这个字符串对应的整数是大于等于 num 的 最小无零 整数，且 各数位之积 能被 t 整除。
如果不存在这样的数字，请你返回 "-1" 。

示例 1：输入：num = "1234", t = 256;  输出："1488"
解释：大于等于 1234 且能被 256 整除的最小无零整数是 1488 ，它的数位乘积为 256 。

示例 2：输入：num = "12355", t = 50;  输出："12355"
解释：12355 已经是无零且数位乘积能被 50 整除的整数，它的数位乘积为 150 。

示例 3：输入：num = "11111", t = 26;  输出："-1"
解释：不存在大于等于 11111 且数位乘积能被 26 整除的整数。

提示：
2 <= num.length <= 2 * 10^5
num 只包含 ['0', '9'] 之间的数字。
num 不包含前导 0 。
1 <= t <= 10^14

"""
from math import gcd
from functools import cache


def smallestNumber(num: str, t: int) -> str:
    # # 数位只能是1-9，它们的质因子只有 {2, 3, 5, 7}
    # # 解法一：贪心构造
    # # 1. 枚举t的质因子，如果t包含其它质因子，永远无法满足条件 → 返回 "-1"
    # tmp = t
    # for p in 2, 3, 5, 7:
    #     while tmp % p == 0:
    #         tmp //= p
    # if tmp > 1:
    #     return "-1"
    #
    # # 2. 贪心构造
    # n = len(num)
    # left_t = [0] * (n + 1)  # left_t[i]：处理完前 i 位后，还需要被整除的剩余部分
    # left_t[0] = t
    # pos = n - 1  # pos 构造起始位置，有0时就是第一个出现 '0' 的位置; 因为无零数字不能有0，如果遇到0必须从这里开始调整
    #
    # # 2-1 先分析 num 本身是否满足条件，以及定位 num 可能有的 0
    # for i, c in enumerate(num):
    #     if c == '0':
    #         pos = i
    #         break
    #     left_t[i + 1] = left_t[i] // gcd(left_t[i], int(c))
    # if left_t[n] == 1:  # num的数位之积已经是 t 的倍数
    #     return num
    #
    # # 2-2 逐位调整 num，贪心构造
    # # 假设答案和 s 一样长: 从 pos 位置往前枚举要增大的位置：因为要保持数字尽可能小，优先改动低位
    # num_list = list(map(int, num))
    # for i in range(pos, -1, -1):
    #     # 将第 i 位数字逐步增大（当前值+1 → 9）
    #     for num_list[i] in range(num_list[i] + 1, 10):
    #         t_now = left_t[i] // gcd(left_t[i], num_list[i])
    #         # 初始化贪心选择的数字为 9：从最大的数字开始试，因为大数字包含更多质因子k = 9
    #         k = 9
    #         # 从最后一位往前填充 i 后面的所有位置
    #         for j in range(n - 1, i, -1):
    #             while t_now % k:
    #                 k -= 1
    #             t_now //= k
    #             # 贪心策略：每一位都选当前最优（最大合法）数字
    #             num_list[j] = k
    #         # t_now == 1 说明所有需要的质因子都已凑齐
    #         if t_now == 1:
    #             return ''.join(map(str, num_list))
    #
    # # 无法在原长度内满足，答案一定比 s 长
    # ans = []
    # for i in range(9, 1, -1):
    #     while t % i == 0:
    #         ans.append(str(i))
    #         t //= i
    # return ''.join(ans[::-1]).rjust(n + 1, '1')  # 前面补 1
    # # rjust(width, fillchar) 是字符串右对齐方法：如果长度不足 n+1，在左边填充字符 '1'

    # 解法二：dfs + 记忆化搜索
    cnt = 0  # 记录总共需要多少个质因子
    tmp = t
    for p in 2, 3, 5, 7:
        while tmp % p == 0:
            tmp //= p
            cnt += 1
    if tmp > 1:
        return "-1"

    # 补前导零（至少一个）
    cnt = max(cnt - len(num) + 1, 1)
    s = '0' * cnt + num

    n = len(s)
    ans = ['0'] * n

    @cache
    def dfs(i: int, t: int, is_limit: bool) -> bool:
        if i == n:
            return t == 1

        if is_limit and i < cnt and dfs(i + 1, t, True):  # 填 0（跳过）
            return True

        low = int(s[i]) if is_limit else 1
        for d in range(low, 10):
            if dfs(i + 1, t // gcd(t, d), is_limit and d == low):
                ans[i] = str(d)
                return True
        return False

    dfs(0, t, True)
    dfs.cache_clear()  # 防止爆内存
    return ''.join(ans).lstrip('0')  # 去掉前导零








