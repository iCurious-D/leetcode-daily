""" 3702. 按位异或非零的最长子序列  中等
给你一个整数数组 nums。
返回 nums 中 按位异或（XOR）计算结果 非零 的 最长子序列 的长度。
如果不存在这样的 子序列 ，返回 0 。
子序列 是一个 非空 数组，可以通过从原数组中删除一些或不删除任何元素（不改变剩余元素的顺序）派生而来。

示例 1：输入： nums = [1,2,3];    输出： 2
解释：最长子序列之一是 [2, 3]。按位异或计算为 2 XOR 3 = 1，它是非零的。
示例 2：输入： nums = [2,3,4];    输出： 3
解释：最长子序列是 [2, 3, 4]。按位异或计算为 2 XOR 3 XOR 4 = 5，它是非零的。

提示：
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9

"""
from functools import reduce
from operator import xor
from typing import List

def longestSubsequence(nums: List[int]) -> int:
    # # 解法一
    # total_xor = 0
    # all_zero = True
    # for num in nums:
    #     total_xor ^= num
    #     if all_zero==True and num != 0:
    #         all_zero = False
    # if total_xor==0 and all_zero==False:
    #     return len(nums)-1
    # return 0 if all_zero else len(nums)

    # 解法二
    total_xor = 0
    if not any(nums):
        return 0
    for num in nums:
        total_xor ^= num
    return len(nums) - (total_xor == 0)

    # # 解法三
    # if not any(nums):
    #     return 0
    # total_xor = reduce(xor, nums)
    # return len(nums) - (total_xor == 0)


if __name__ == '__main__':
    print(longestSubsequence([1,2,3]))
    print(longestSubsequence([2,3,4]))












