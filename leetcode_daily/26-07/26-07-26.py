""" 628. 三个数的最大乘积   简单
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：输入：nums = [1,2,3];     输出：6
示例 2：输入：nums = [1,2,3,4];   输出：24
示例 3：输入：nums = [-1,-2,-3];  输出：-6

提示：
3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-26.md

"""
from typing import List


def maximumProduct(nums: List[int]) -> int:
    # nums.sort()
    # return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    for num in nums:
        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num
        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num
    return max(min1 * min2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
    print(maximumProduct([1, 2, 3]))
    print(maximumProduct([1, 2, 3, 4]))
    print(maximumProduct([-1, -2, -3]))
    print(maximumProduct([-1000, -1000, 1, 1000]))