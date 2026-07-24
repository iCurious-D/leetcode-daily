""" 3514. 不同 XOR 三元组的数目 II  中等
给你一个整数数组 nums 。
XOR 三元组 定义为三个元素的异或值 nums[i] XOR nums[j] XOR nums[k]，其中 i <= j <= k。
返回所有可能三元组 (i, j, k) 中 不同 的 XOR 值的数量。

示例 1：输入： nums = [1,3];  输出： 2
解释：所有可能的 XOR 三元组值为：
(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
不同的 XOR 值为 {1, 3} 。因此输出为 2 。

示例 2：输入： nums = [6,7,8,9];  输出： 4
解释：不同的 XOR 值为 {6, 7, 8, 9} 。因此输出为 4 。

提示：
1 <= nums.length <= 1500
1 <= nums[i] <= 1500
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-23.md

"""
from itertools import combinations
from typing import List

def uniqueXorTriplets(nums: List[int]) -> int:
    # 解法一
    # nums = set(nums)
    # two = {a ^ b for a, b in combinations(nums, 2)} | {0}
    # three = {t ^ c for t in two for c in nums}
    # return len(three)

    # # 解法二：用布尔数组代替 Python Set（常数优化）
    uniq = list(set(nums))
    M = 1 << max(uniq).bit_length()  # 动态值域

    # 两数异或集合
    two = [False] * M
    two[0] = True  # 对应 i == j 的情况

    n = len(uniq)
    for i in range(n):
        a = uniq[i]
        for j in range(i + 1, n):
            two[a ^ uniq[j]] = True

    # 三数异或集合
    three = [False] * M
    for t in range(M):
        if two[t]:
            for c in uniq:
                three[t ^ c] = True

    return sum(three)


if __name__ == '__main__':
    print(uniqueXorTriplets([1,3]))
    print(uniqueXorTriplets([6,7,8,9]))
    print(uniqueXorTriplets([1,2,3,4,5,6,7,8,9,10]))
