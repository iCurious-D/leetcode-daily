""" 3471. 找出最大的几近缺失整数   简单
给你一个整数数组 nums 和一个整数 k 。
如果整数 x 恰好仅出现在 nums 中的一个大小为 k 的子数组中，则认为 x 是 nums 中的几近缺失（almost missing）整数。
返回 nums 中 最大的几近缺失 整数，如果不存在这样的整数，返回 -1 。
子数组 是数组中的一个连续元素序列。

示例 1：输入：nums = [3,9,2,1,7], k = 3;  输出：7
解释：1 出现在两个大小为 3 的子数组中：[9, 2, 1]、[2, 1, 7]; 2 出现在三个大小为 3 的子数组中：[3, 9, 2]、[9, 2, 1]、[2, 1, 7]
3 出现在一个大小为 3 的子数组中：[3, 9, 2]; 7 出现在一个大小为 3 的子数组中：[2, 1, 7]
9 出现在两个大小为 3 的子数组中：[3, 9, 2]、[9, 2, 1]; 返回 7 ，因为它满足题意的所有整数中最大的那个。

示例 2：输入：nums = [3,9,7,2,1,7], k = 4;    输出：3
解释：1 出现在两个大小为 4 的子数组中：[9, 7, 2, 1]、[7, 2, 1, 7]
2 出现在三个大小为 4 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1]、[7, 2, 1, 7]
3 出现在一个大小为 4 的子数组中：[3, 9, 7, 2];    7 出现在三个大小为 4 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1]、[7, 2, 1, 7]
9 出现在两个大小为 4 的子数组中：[3, 9, 7, 2]、[9, 7, 2, 1];   返回 3 ，因为它满足题意的所有整数中最大的那个。

示例 3：输入：nums = [0,0], k = 1;    输出：-1
解释：不存在满足题意的整数。

提示：
1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-18.md

"""
from collections import Counter
from typing import List

def check(nums: List[int], num: int) -> int:
    return -1 if num in nums else num

def largestInteger(nums: List[int], k: int) -> int:
    # 解法一
    # n = len(nums)
    #
    # if k == n:
    #     return max(nums)
    #
    # cnt = Counter(nums)
    # ans = -1
    # if k == 1:
    #     for num, c in cnt.items():
    #         if c == 1:
    #             ans = max(ans, num)
    #     return ans
    #
    # if cnt[nums[0]] == 1:
    #     ans = max(ans, nums[0])
    # if cnt[nums[-1]] == 1:
    #     ans = max(ans, nums[-1])
    # return ans

    # 解法二
    # if k == len(nums):
    #     return max(nums)
    #
    # if k == 1:
    #     ans = -1
    #     for num, c in Counter(nums).items():
    #         if c == 1:
    #             ans = max(ans, num)
    #     return ans
    #
    # return max(check(nums[1:], nums[0]), check(nums[:-1], nums[-1]))

    # 全屏模式：一个窗口盖住全场
    if k == len(nums):
        return max(nums)

    # 每个元素独占一屏，必须知道全局频次
    if k == 1:
        freq = Counter(nums)
        return max((x for x, c in freq.items() if c == 1), default=-1)

    # 1 < k < n：只看两端
    return max(nums[0] if nums.count(nums[0]) == 1 else -1, nums[-1] if nums.count(nums[-1]) == 1 else -1)


if __name__ == '__main__':
    print(largestInteger(nums=[3, 9, 2, 1, 7], k=3))
    print(largestInteger(nums=[3, 9, 7, 2, 1, 7], k=4))
    print(largestInteger(nums=[0, 0], k=1))
