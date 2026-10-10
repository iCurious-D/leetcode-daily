""" 128. 最长连续序列     中等
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：输入：nums = [100,4,200,1,3,2];   输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：输入：nums = [0,3,7,2,5,8,4,6,0,1];   输出：9
示例 3：输入：nums = [1,0,1,2];   输出：3

提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""
from collections import Counter


def longestConsecutive(self, nums: list[int]) -> int:
    st = set(nums)
    m = len(st)
    ans = 0
    for x in st:
        if x - 1 in st:
            continue
        y = x + 1
        while y in st:
            y += 1
        ans = max(ans, y - x)
        if ans * 2 >= m:
            break
    return ans


if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(longestConsecutive([1,0,1,2]))









