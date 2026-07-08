""" 3756. 连接非零数字并乘以其数字和 II  中等
给你一个长度为 m 的字符串 s，其中仅包含数字。另给你一个二维整数数组 queries，其中 queries[i] = [li, ri]。
对于每个 queries[i]，提取 子串 s[li..ri]，然后执行以下操作：
将子串中所有 非零数字 按照原始顺序连接起来，形成一个新的整数 x。如果没有非零数字，则 x = 0。
令 sum 为 x 中所有数字的 数字和 。答案为 x * sum。
返回一个整数数组 answer，其中 answer[i] 是第 i 个查询的答案。
由于答案可能非常大，请返回其对 109 + 7 取余数的结果。
子串 是字符串中的一个连续、非空 字符序列。

示例 1：输入： s = "10203004", queries = [[0,7],[1,3],[4,6]]; 输出： [12340, 4, 9]
解释：s[0..7] = "10203004";    x = 1234;   sum = 1 + 2 + 3 + 4 = 10    因此，答案是 1234 * 10 = 12340。
s[1..3] = "020" x = 2   sum = 2   因此，答案是 2 * 2 = 4。
s[4..6] = "300" x = 3   sum = 3   因此，答案是 3 * 3 = 9。

示例 2：输入： s = "1000", queries = [[0,3],[1,1]];   输出： [1, 0]
解释：s[0..3] = "1000" x = 1   sum = 1 因此，答案是 1 * 1 = 1。
s[1..1] = "0"   x = 0   sum = 0 因此，答案是 0 * 0 = 0。

示例 3：输入： s = "9876543210", queries = [[0,9]]    输出： [444444137]
解释：s[0..9] = "9876543210"   x = 987654321   sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
因此，答案是 987654321 * 45 = 44444444445。    返回结果为 44444444445 mod (109 + 7) = 444444137。

提示：
1 <= m == s.length <= 10^5
s 仅由数字组成。
1 <= queries.length <= 10^5
queries[i] = [li, ri]
0 <= li <= ri < m
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-08.md

"""
from typing import List


def nonZeroProductQueries(s: str, queries: List[List[int]]) -> List[int]:
    MOD = 10 ** 9 + 7
    n = len(s)

    # 预计算 10 的幂
    pow10 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow10[i] = (pow10[i - 1] * 10) % MOD

    # # 三个前缀数组
    # preVal = [0] * (n + 1)  # 去零拼接值
    # preCnt = [0] * (n + 1)  # 非零数字个数
    # preSum = [0] * (n + 1)  # 非零数字和
    #
    # for i in range(n):
    #     d = int(s[i])
    #     preCnt[i + 1] = preCnt[i]
    #     preSum[i + 1] = preSum[i]
    #     preVal[i + 1] = preVal[i]
    #
    #     if d != 0:
    #         preCnt[i + 1] += 1
    #         preSum[i + 1] += d
    #         preVal[i + 1] = (preVal[i] * 10 + d) % MOD
    #     # 如果 d == 0，三个前缀值都不变：零被直接跳过
    #
    # ans = []
    # for l, r in queries:
    #     cnt = preCnt[r + 1] - preCnt[l]
    #     if cnt == 0:
    #         ans.append(0)
    #         continue
    #     s_sum = preSum[r + 1] - preSum[l]
    #     x = (preVal[r + 1] - preVal[l] * pow10[cnt]) % MOD
    #     ans.append((x * s_sum) % MOD)
    #
    # return ans

    preSum = [0] * (n + 1)  # s 的前缀和
    preVal = [0] * (n + 1)  # s 的前缀对应的数字（模 MOD）
    preCnt = [0] * (n + 1)  # s 的前缀中的非零数字个数
    for i, d in enumerate(map(int, s)):
        preSum[i + 1] = preSum[i] + d
        preVal[i + 1] = (preVal[i] * 10 + d) % MOD if d else preVal[i]
        preCnt[i + 1] = preCnt[i] + (d > 0)

    ans = []
    for l, r in queries:
        r += 1  # 避免下面多次计算 r+1
        length = preCnt[r] - preCnt[l]
        x = preVal[r] - preVal[l] * pow10[length]
        ans.append(x * (preSum[r] - preSum[l]) % MOD)
    return ans


if __name__ == '__main__':
    print(nonZeroProductQueries("10203004", [[0,7],[1,3],[4,6]]))
    print(nonZeroProductQueries("1000", [[0,3],[1,1]]))
    print(nonZeroProductQueries("9876543210", [[0,9]]))

