""" 1477. 找两个和为目标值且不重叠的子数组  中等
给你一个整数数组 arr 和一个整数值 target 。
请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。
可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

示例 1：输入：arr = [3,2,2,4,3], target = 3;   输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
示例 2：输入：arr = [7,3,4,7], target = 7;    输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
示例 3：输入：arr = [4,3,2,6,2,3,4], target = 6;  输出：-1
解释：我们只有一个和为 6 的子数组。
示例 4：输入：arr = [5,5,4,4,5], target = 3;  输出：-1
解释：我们无法找到和为 3 的子数组。
示例 5：输入：arr = [3,1,1,1,5,1,2,1], target = 3;    输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。

提示：
1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8

"""
from math import inf
from typing import List

def minSumOfLengths(arr: List[int], target: int) -> int:
    # n = len(arr)
    # suf_min_len = [0] * n
    # min_len = inf
    # tmp = 0
    # r = n - 1
    # for l in range(n-1, -1, -1):
    #     tmp += arr[l]
    #     while tmp > target:
    #         tmp -= arr[r]
    #         r -= 1
    #     if tmp == target:
    #         min_len = min(min_len, r-l+1)
    #     suf_min_len[l] = min_len
    #
    # ans = inf
    # l = 0
    # tmp = 0
    # for r in range(n-1):
    #     tmp += arr[r]
    #     while tmp > target:
    #         tmp -= arr[l]
    #         l += 1
    #     if tmp == target:
    #         ans = min(ans, r-l+1 + suf_min_len[r+1])
    #
    # return -1 if ans == inf else ans

    # n = len(arr)
    # end_len = [inf] * n  # end_len[r] 表示以 r 结尾的满足条件的子数组长度
    # ans = best_left = inf
    # tmp = l = 0
    #
    # for r in range(n):
    #     tmp += arr[r]
    #     while tmp > target:
    #         if end_len[l] != inf:
    #             best_left = min(best_left, end_len[l])
    #         tmp -= arr[l]
    #         l += 1
    #
    #     if tmp == target:
    #         length = r - l + 1
    #         ans = min(ans, best_left + length)
    #         end_len[r] = length
    #
    # return -1 if ans == inf else ans

    # n = len(arr)
    # pre_min_len = [inf] * (n+1)
    # ans = min_len = inf
    # tmp = l = 0
    # for r in range(n):
    #     tmp += arr[r]
    #     while tmp > target:
    #         tmp -= arr[l]
    #         l += 1
    #     if tmp == target:
    #         ans = min(ans, pre_min_len[l] + r-l+1)
    #         min_len = min(min_len, r-l+1)
    #     pre_min_len[r+1] = min_len
    # return -1 if ans == inf else ans

    # 如果有负数，滑动窗口失效
    # 用哈希表优化：前缀和 + 哈希表
    n = len(arr)
    # pos 记录每个前缀和最近一次出现的索引
    # prefix[0] = 0 对应索引 -1（空前缀）
    pos = {0: -1}
    prefix = 0
    best = [inf] * n   # best[i] 表示 arr[0..i] 中和为 target 的最短子数组长度
    ans = inf

    for i in range(n):
        prefix += arr[i]

        # 如果存在 prefix - target，说明有一个子数组和为 target
        if prefix - target in pos:
            l = pos[prefix - target] + 1   # 子数组左端点
            length = i - l + 1             # 当前子数组长度

            # 尝试与之前的最优子数组组合（必须不重叠）
            if l > 0 and best[l - 1] != inf:
                ans = min(ans, best[l - 1] + length)

            # 更新 best[i]
            if i > 0:
                best[i] = min(best[i - 1], length)
            else:
                best[i] = length
        else:
            if i > 0:
                best[i] = best[i - 1]

        # 更新当前前缀和的最新位置（覆盖旧位置，保证下次取到的是最短子数组）
        pos[prefix] = i

    return -1 if ans == inf else ans


if __name__ == '__main__':
    print(minSumOfLengths([3,2,2,4,3], 3))
    print(minSumOfLengths([7,3,4,7], 7))
    print(minSumOfLengths([4,3,2,6,2,3,4], 6))




