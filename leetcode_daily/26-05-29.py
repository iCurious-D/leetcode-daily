""" 3300. 替换为数位和以后的最小元素
给你一个整数数组 nums 。
请你将 nums 中每一个元素都替换为它的各个数位之 和 。
请你返回替换所有元素以后 nums 中的 最小 元素。

示例 1：输入：nums = [10,12,13,14]   输出：1
解释：nums 替换后变为 [1, 3, 4, 5] ，最小元素为 1 。

示例 2：输入：nums = [1,2,3,4]   输出：1
解释：nums 替换后变为 [1, 2, 3, 4] ，最小元素为 1 。

示例 3：输入：nums = [999,19,199]   输出：10
解释：nums 替换后变为 [27, 10, 19] ，最小元素为 10 。

提示：
1 <= nums.length <= 100
1 <= nums[i] <= 10^4

==================================================

解路径：. / leetcode_daily_stories / 26-05-29.md



"""
from math import inf
from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        # ans = inf
        # for num in nums:
        #     cur = 0
        #     while num:
        #         cur += num % 10
        #         num //= 10
        #     ans = min(ans, cur)
        # return ans

        return min(sum(map(int, str(num))) for num in nums)


if __name__ == '__main__':
    s = Solution()
    print(s.minElement(nums=[10, 12, 13, 14]))
    print(s.minElement(nums=[1, 2, 3, 4]))
    print(s.minElement(nums=[999, 19, 199]))