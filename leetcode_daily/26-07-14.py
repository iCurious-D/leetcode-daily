""" 3336. 最大公约数相等的子序列数量     困难
给你一个整数数组 nums。
请你统计所有满足以下条件的 非空 子序列 对 (seq1, seq2) 的数量：
    子序列 seq1 和 seq2 不相交，意味着 nums 中 不存在 同时出现在两个序列中的下标。
    seq1 元素的 GCD 等于 seq2 元素的 GCD。
返回满足条件的子序列对的总数。由于答案可能非常大，请返回其对 109 + 7 取余 的结果。

示例 1：输入： nums = [1,2,3,4];  输出： 10
示例 2：输入： nums = [10,20,30]; 输出： 2
示例 3：输入： nums = [1,1,1,1];  输出： 50

提示：
1 <= nums.length <= 200
1 <= nums[i] <= 200
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-14.md

"""
from functools import cache
from typing import List
from math import gcd, lcm

MOD = 1_000_000_007
MX = 201

# 1. LCM表（最小公倍数）
lcms = [[lcm(i, j) for j in range(MX)] for i in range(MX)]

# 2. 幂次表
pow2 = [1] * MX
pow3 = [1] * MX
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD  # 2的i次方
    pow3[i] = pow3[i - 1] * 3 % MOD  # 3的i次方

# 3. 莫比乌斯函数 μ(n)
# 莫比乌斯函数 μ(n) 是什么？
#   μ(1) = 1
#   μ(n) = 0 if n有平方因子（如4, 8, 9, 12...）
#   μ(n) = (-1)^k if n是k个不同质数的乘积（如6=2×3, μ(6)=1）
# 它的作用是容斥原理的系数！
mu = [0] * MX
mu[1] = 1
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        mu[j] -= mu[i]


def subsequenceCount(nums: List[int]) -> int:

    # ======================================================================================
    # 解法一：递归（记忆化搜索）
    # 状态定义：dfs(i, j, k) 表示在考虑了前 i 个元素（下标 0..i）的取舍之后，
    #           当前 seq1 的 GCD 为 j，seq2 的 GCD 为 k，继续考虑剩余元素后能达到最终两个 GCD 相等的方案数。
    @cache
    def dfs(i, j, k):
        # 边界 i < 0：无剩余元素，当前状态就是最终状态。
        # 若 j == k 则合法，计 1；否则 0。这里 j = k = 0 也被计为合法，对应两个空序列。
        if i < 0:
            return 1 if j == k else 0  # GCD相等才算合法方案

        # 转移：对于元素 nums[i]，三种选择——
        #      都不放：状态不变，dfs(i-1, j, k)
        #      放 seq1：新 GCD = gcd(j, nums[i])，dfs(i-1, gcd(j, nums[i]), k)
        #      放 seq2：新 GCD = gcd(k, nums[i])，dfs(i-1, j, gcd(k, nums[i]))
        return (dfs(i - 1, j, k) + dfs(i - 1, gcd(j, nums[i]), k) + dfs(i - 1, j, gcd(k, nums[i]))) % MOD

    # 最终答案：初始 dfs(n-1, 0, 0) 包含了“两个序列全空”的 1 种方案，题目要求非空，所以减 1。
    return (dfs(len(nums) - 1, 0, 0) - 1) % MOD
    # 这里有一个很巧妙的地方：整个递归过程中 0 一直表示还没放任何元素；gcd(0,x)=x 天然就是第一次加入元素, 所以不用特判。

    # ======================================================================================
    # # 解法二：三维DP（“未来期望”DP）
    # 未来期望 DP 从“如果我现在是 (j,k)，再塞进 num 后状态变成 (gcd(j,num),k)，然后查剩余方案”。计算时先知道加入后的状态，再往回拉，所以一行赋值即可。
    # n = len(nums)
    # m = max(nums)

    # 状态定义（与递归一致）dp[i][j][k]：已经处理完前 i 个元素，
    #       此时 seq1 GCD = j, seq2 GCD = k。在这个状态下，继续处理剩余 n-i 个元素，最终能使两个 GCD 相等（且按要求非空）的方案数。
    # dp = [[[0] * (m+1) for _ in range(m+1)] for _ in range(n+1)]

    # 边界（i = 0）：没有元素可处理，当前 (j, k) 就是最终状态。
    #       为了直接得到非空子序列对的答案，这里把“合法最终状态”定义为 j == k 且 j >= 1，即最终 GCD 相等且不为零（两个序列都非空）。
    #       因此 dp[0][j][j] = 1 (j >= 1)，而 dp[0][0][0] 保持 0（排除了全空方案）。
    # for j in range(1, m+1):
    #     dp[0][j][j] = 1

    # 状态转移：
    # 递归关系为：dfs(i, j, k) = dfs(i - 1, j, k) + dfs(i - 1, gcd(j, nums[i]), k) + dfs(i - 1, j, gcd(k, nums[i]))
    # 对应到数组：dp[i] 对应 dfs(i-1, ·, ·)，dp[i+1] 对应 dfs(i, ·, ·)
    # 于是递推：dp[i+1][j][k] = dp[i][j][k] + dp[i][gcd(j, num)][k] + dp[i][j][gcd(k, num)]
    #           这里的求和是“拉取（pull）”模式：
    #           计算 dp[i+1][j][k] 时，直接看处理 num 之后可能到达的三种未来状态，
    #           这些未来状态的值已经存在 dp[i] 中（因为 dp[i] 表示的是“再往后走的结果”）。
    #           因此一次赋值就能完成，不需要 += 累加多个来源——在每一轮 i 中，dp[i+1] 的每个元素恰好由这三个来源唯一确定。
    # for i, num in enumerate(nums):
    #     for j in range(m+1):
    #         for k in range(m+1):
    #             dp[i+1][j][k] = (dp[i][j][k] + dp[i][gcd(j, num)][k] + dp[i][j][gcd(k, num)]) % MOD
    #             # 转移：
    #

    # 最终答案 dp[n][0][0]：初始时空序列（GCD=0,0），经过所有 n 个元素的选择后，能达成“最终 GCD 相等且非空”的方案数。无需再减 1。
    # return dp[n][0][0]

    # =======================================================================================
    # # 解法二：三维DP（“历史累积”DP）
    # # 历史累积 DP 从“我现在已经是 (j,k)，塞进 num 就去更新新状态”。一个目标被多个起点更新，所以必须分别累加。
    # n = len(nums)
    # m = max(nums)
    # # 状态定义（与上面相反）dp[i][j][k]：仅考虑前 i 个元素，已经完成选择，目前 seq1 GCD = j, seq2 GCD = k 的方案总数。
    # dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    # # 边界（i = 0）：0 个元素时，唯一可能的状态是两个序列都空：dp[0][0][0] = 1。
    # dp[0][0][0] = 1
    # # 状态转移：为什么必须“分开更新”？
    # # 这是“推送（push）”模式：对每个已知状态 dp[i][j][k]，把当前元素 num 加入后形成的新状态累加到下一层。
    # #   不选 → dp[i+1][j][k] += dp[i][j][k]
    # #   选入 seq1 → dp[i+1][gcd(j,num)][k] += dp[i][j][k]
    # #   选入 seq2 → dp[i+1][j][gcd(k,num)] += dp[i][j][k]
    # # 一个目标状态 dp[i+1][a][b] 可能被多个不同的前驱 (j,k) 贡献（例如 gcd(2,6)=2，gcd(4,6)=2 等），
    # # 所以必须用 += 把这些来源逐个累加起来。不能像未来期望 DP 那样用一次赋值写出，因为这里没有简单的“未来状态值之和”的逆关系。
    # for i, num in enumerate(nums):
    #     for j in range(m + 1):
    #         for k in range(m + 1):
    #             if dp[i][j][k] == 0:
    #                 continue
    #             # 选择1：第i+1个元素不放任何序列
    #             dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % MOD
    #             # 选择2：第i+1个元素放入seq1
    #             dp[i + 1][gcd(j, num)][k] = (dp[i + 1][gcd(j, num)][k] + dp[i][j][k]) % MOD
    #             # 选择3：第i+1个元素放入seq2
    #             dp[i + 1][j][gcd(k, num)] = (dp[i + 1][j][gcd(k, num)] + dp[i][j][k]) % MOD
    #
    # # 最终答案：处理完所有元素后，合法的非空子序列对是那些两个 GCD 相等且 g >= 1 的状态：sum_{g=1..m} dp[n][g][g]。
    # # 全空状态 dp[n][0][0] 被自然地排除。
    # ans = 0
    # for g in range(1, m + 1):
    #     ans = (ans + dp[n][g][g]) % MOD
    #
    # return ans

    # # 解法三：多维dp优化—滚动数组
    # m = max(nums)
    # # dp[j][k] 表示当前处理到某个位置时，seq1的GCD为j，seq2的GCD为k的方案数
    # dp = [[0] * (m + 1) for _ in range(m + 1)]
    # # 初始化：还没选任何元素时，GCD都为0的情况有1种（但题目要求非空，最后要减去）
    # dp[0][0] = 1
    #
    # for num in nums:
    #     # 需要从后往前更新，避免重复使用当前元素
    #     new_dp = [row[:] for row in dp]  # 创建新的状态数组，基于上一轮的状态转移
    #
    #     for j in range(m + 1):
    #         for k in range(m + 1):
    #             if dp[j][k] == 0:
    #                 continue
    #             # 选择1：把num加入seq1
    #             new_dp[gcd(j, num)][k] = (new_dp[gcd(j, num)][k] + dp[j][k]) % MOD
    #             # 选择2：把num加入seq2
    #             new_dp[j][gcd(k, num)] = (new_dp[j][gcd(k, num)] + dp[j][k]) % MOD
    #
    #     dp = new_dp
    #
    # # dp[0][0] 包含了都不选的情况，需要排除
    # # 答案是所有 gcd(j,k) 相等且不为0的情况
    # ans = 0
    # for g in range(1, m + 1):
    #     ans = (ans + dp[g][g]) % MOD
    #
    # return ans

    # # # 解法四：倍数容斥
    # m = max(nums)
    # # cnt[i] 表示 nums 中的 i 的倍数的个数
    # cnt = [0] * (m + 1)
    # # 统计每个数出现的次数。
    # for x in nums:
    #     cnt[x] += 1
    # # 关键！ 它在累加所有i的倍数的数量。
    # for i in range(1, m + 1):
    #     for j in range(i * 2, m + 1, i):
    #         cnt[i] += cnt[j]  # 统计 i 的倍数的个数
    #         # 最终 cnt[i] = nums中能被 i 整除的元素个数。
    #
    # # f[g1][g2] 的含义:
    # # 从nums中选出两个不相交子序列(seq1, seq2)，满足：
    # # seq1的所有元素都能被 g1 整除,seq2的所有元素都能被 g2 整除 且seq1和seq2都非空 的方案数。
    # f = [[0] * (m + 1) for _ in range(m + 1)]
    # for g1 in range(1, m + 1):
    #     for g2 in range(1, m + 1):
    #         l = lcms[g1][g2]
    #         # 为什么要算 lcm(g1, g2)？
    #         # 因为seq1和seq2要不相交（不能有共同元素）。
    #         # 如果一个数同时能被g1和g2整除，那它就是 lcm(g1, g2) 的倍数。
    #         c = cnt[l] if l <= m else 0
    #         c1, c2 = cnt[g1], cnt[g2]
    #         # c1 = cnt[g1]：能被g1整除的元素个数
    #         # c2 = cnt[g2]：能被g2整除的元素个数
    #         # c = cnt[lcm(g1,g2)]：能同时被g1和g2整除的元素个数（冲突元素）
    #         f[g1][g2] = (pow3[c] * pow2[c1 + c2 - c * 2] - pow2[c1] - pow2[c2] + 1) % MOD
    #         # 核心思想：把元素分成三类
    #         #   A类：只能被g1整除（不能被g2整除）→ 有 (c1 - c) 个
    #         #   B类：只能被g2整除（不能被g1整除）→ 有 (c2 - c) 个
    #         #   C类：既能被g1整除又能被g2整除   → 有 c 个
    #         # 对于每个元素的三种选择：
    #         #   A类元素：放入seq1、都不放（2种选择）
    #         #   B类元素：放入seq2、都不放（2种选择）
    #         #   C类元素：放入seq1、放入seq2、都不放（3种选择）
    #         # 所以总方案数  = 2^(c1-c) × 2^(c2-c) × 3^c
    #         #        = 2^(c1+c2-2c) × 3^c
    #         #        = pow2[c1 + c2 - c*2] * pow3[c]
    #         # 但要减去不合法的情况：
    #         # seq1为空：2^c2 种（每个B类和C类元素可以放seq2或不放）
    #         # seq2为空：2^c1 种
    #         # 但"都为空"被减了两次，要加回1
    #         # f[g1][g2] = pow3[c] * pow2[c1 + c2 - c*2] - pow2[c1] - pow2[c2] + 1
    #
    # # 倍数容斥
    # return sum(mu[j] * mu[k] * f[j * i][k * i]
    #            for i in range(1, m + 1)
    #            for j in range(1, m // i + 1)
    #            for k in range(1, m // i + 1)) % MOD
    # # 为什么要用莫比乌斯函数？
    # # 我们想要的是：GCD恰好等于g 的子序列对数量。
    # # 但 f[g][g] 统计的是：GCD是g的倍数 的子序列对数量。
    # # 莫比乌斯反演公式
    # # 如果：F(n) = sum(f(d)) for all d|n  （F是f的前缀和）
    # # 那么：f(n) = sum(μ(d) * F(n/d)) for all d|n
    # # 答案 = sum(μ(j) * μ(k) * f[j*i][k*i])

    # # 原地爆炸
    # n = len(nums)
    # ans = 0
    # # 每个元素三种状态：0=不选, 1=放seq1, 2=放seq2
    # for mask in range(3**n):
    #     seq1, seq2 = [], []
    #     tmp = mask
    #     for i in range(n):
    #         choice = tmp % 3
    #         tmp //= 3
    #         if choice == 1:
    #             seq1.append(nums[i])
    #         elif choice == 2:
    #             seq2.append(nums[i])
    #     if seq1 and seq2:
    #         g1 = seq1[0]
    #         for x in seq1[1:]: g1 = gcd(g1, x)
    #         g2 = seq2[0]
    #         for x in seq2[1:]: g2 = gcd(g2, x)
    #         if g1 == g2:
    #             ans += 1
    # return ans % 1000000007


# def findGCD(self, nums: List[int]) -> int:
#     # return math.gcd(max(nums), min(nums))
#
#     def gcd(a, b):
#         if b == 0:
#             return a
#         else:
#             return gcd(b, a % b)
#
#     return gcd(max(nums), min(nums))


if __name__ == '__main__':
    print(subsequenceCount(nums=[1, 2, 3, 4]))
    print(subsequenceCount(nums=[10, 20, 30]))
    print(subsequenceCount(nums=[1, 1, 1, 1]))
    print(gcd(0, 6))  # 6: gcd(0, x)==x
