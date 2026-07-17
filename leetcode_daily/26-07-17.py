""" 3312. 查询排序后的最大公约数   困难
给你一个长度为 n 的整数数组 nums 和一个整数数组 queries 。
gcdPairs 表示数组 nums 中所有满足 0 <= i < j < n 的数对 (nums[i], nums[j]) 的 最大公约数 升序 排列构成的数组。
对于每个查询 queries[i] ，你需要找到 gcdPairs 中下标为 queries[i] 的元素。
请你返回一个整数数组 answer ，其中 answer[i] 是 gcdPairs[queries[i]] 的值。
gcd(a, b) 表示 a 和 b 的 最大公约数 。

示例 1：输入：nums = [2,3,4], queries = [0,2,2]   输出：[1,2,2]
解释：gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].
升序排序后得到 gcdPairs = [1, 1, 2] 。
所以答案为 [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2] 。

示例 2：输入：nums = [4,4,2,1], queries = [5,3,1,0]   输出：[4,2,1,1]
解释：gcdPairs 升序排序后得到 [1, 1, 1, 2, 2, 4] 。

示例 3：输入：nums = [2,2], queries = [0,0]   输出：[2,2]
解释：gcdPairs = [2] 。

提示：
2 <= n == nums.length <= 10^5
1 <= nums[i] <= 5 * 10^4
1 <= queries.length <= 10^5
0 <= queries[i] < n * (n - 1) / 2
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-17.md

"""
from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List


def gcdValues(nums: List[int], queries: List[int]) -> List[int]:
    # m = max(nums)
    # # gcd_cnt[i] 最终表示：数组中有多少对数的gcd恰好等于i
    # gcd_cnt = [0] * (m + 1)

    # # 第一招：统计每个数在nums中出现的频次
    # # 比如 nums=[4,4,2,1]，则 gcd_cnt[1]=1, gcd_cnt[2]=1, gcd_cnt[4]=2
    # for num in nums:
    #     gcd_cnt[num] += 1
    #
    # # 第二招：计算"至少能被i整除的数有多少个"（包含i的倍数）
    # # 从后往前累加：如果某数是i的倍数，那它也能被i整除
    # # 比如 i=1时，会把gcd_cnt[2],gcd_cnt[3],...都加到gcd_cnt[1]上
    # for i in range(1, m + 1):
    #     for j in range(i * 2, m + 1, i):
    #         gcd_cnt[i] += gcd_cnt[j]
    #
    # # 第三招：从"能被i整除的数的个数"计算"有多少对的gcd至少是i"
    # # C(n,2) = n*(n-1)/2，从n个数中任选2个组成一对
    # # 此时gcd_cnt[i]表示：有多少对数，它们的gcd是i的倍数（>=i）
    # for i in range(1, m + 1):
    #     gcd_cnt[i] = gcd_cnt[i] * (gcd_cnt[i] - 1) // 2
    #
    # # 第四招：容斥原理！从"gcd是i的倍数"反推"gcd恰好等于i"
    # # 从大到小遍历，减去那些gcd是i的倍数但>i的情况
    # # 比如 gcd_cnt[1] 要减去 gcd_cnt[2],gcd_cnt[3],...（因为它们也贡献给了gcd_cnt[1]）
    # for i in range(m, 0, -1):
    #     for j in range(i * 2, m + 1, i):
    #         gcd_cnt[i] -= gcd_cnt[j]
    #
    # # 第五招：前缀和！让gcd_cnt[i]表示"gcd <= i 的数对有多少个"
    # # 这样就能用二分查找快速定位第k小的gcd值
    # # 比如 gcd_cnt=[0,3,5,5,6] 表示：gcd<=1的有3对，gcd<=2的有5对，...
    # for i in range(1, m + 1):
    #     gcd_cnt[i] += gcd_cnt[i - 1]
    #
    # ans = []
    # # 第六招：对每个查询，用二分查找找到第q+1小的gcd值
    # # q+1是因为queries是从0开始的排名，而前缀和是从1开始计数
    # for q in queries:
    #     q += 1
    #     pos = bisect_left(gcd_cnt, q)
    #     ans.append(pos)
    # return ans

    # # 解法一
    # m = max(nums)
    # cnt = [0] * (m + 1)
    # for num in nums:
    #     cnt[num] += 1
    # for i in range(1, m + 1):
    #     for j in range(i * 2, m + 1, i):
    #         cnt[i] += cnt[j]
    # for i in range(1, m + 1):
    #     cnt[i] = cnt[i] * (cnt[i] - 1) // 2
    # for i in range(m, 0, -1):
    #     for j in range(i * 2, m + 1, i):
    #         cnt[i] -= cnt[j]
    #
    # s = list(accumulate(cnt))
    # return [bisect_right(cnt, q) for q in queries]


    解法二
    mx = max(nums)
    cnt_x = [0] * (mx + 1)
    for x in nums:
        cnt_x[x] += 1

    cnt_gcd = [0] * (mx + 1)
    for i in range(mx, 0, -1):
        c = 0
        for j in range(i, mx + 1, i):
            c += cnt_x[j]
            cnt_gcd[i] -= cnt_gcd[j]  # gcd 是 2i,3i,4i,... 的数对不能统计进来
        cnt_gcd[i] += c * (c - 1) // 2  # c 个数选 2 个，组成 c*(c-1)/2 个数对

    s = list(accumulate(cnt_gcd))  # 前缀和
    return [bisect_right(s, q) for q in queries]

    # # 解法三
    # m = max(nums)
    # cnt = [0] * (m + 1)
    #
    # # 第一招：统计每个数在 nums 中出现的频次
    # for num in nums:
    #     cnt[num] += 1
    #
    # for i in range(1, m + 1):
    #     for j in range(i * 2, m + 1, i):
    #         cnt[i] += cnt[j]
    #
    # for i in range(1, m + 1):
    #     cnt[i] = cnt[i] * (cnt[i] - 1) // 2
    #
    # # 预处理莫比乌斯函数 μ
    # mu = [0] * (m + 1)
    # mu[1] = 1
    # for i in range(1, m + 1):
    #     for j in range(i * 2, m + 1, i):
    #         mu[j] -= mu[i]
    #
    # g = [0] * (m + 1)
    # for i in range(1, m + 1):
    #     for k in range(1, m // i + 1):
    #         g[i] += mu[k] * cnt[i * k]
    #
    # s = list(accumulate(g))  # 前缀和
    # return [bisect_right(s, q) for q in queries]


if __name__ == '__main__':
    print(gcdValues(nums=[2, 3, 4], queries=[0, 2, 2]))
    print(gcdValues(nums=[4, 4, 2, 1], queries=[5, 3, 1, 0]))
    print(gcdValues(nums=[2, 2], queries=[0, 0]))
