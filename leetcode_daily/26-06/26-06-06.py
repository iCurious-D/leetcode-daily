""" 2574. 左右元素和的差值
给你一个下标从 0 开始的长度为 n 的整数数组 nums。
定义两个数组 leftSum 和 rightSum，其中：
leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。
rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。
返回长度为 n 数组 answer，其中 answer[i] = |leftSum[i] - rightSum[i]|。

示例 1：输入：nums = [10,4,8,3]  输出：[15,1,11,22]
解释：数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。

示例 2：输入：nums = [1]  输出：[0]
解释：数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。

提示：
1 <= nums.length <= 1000
1 <= nums[i] <= 10^5
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-06.md

"""
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = [0] * n
        #
        # left_sum = 0
        # for i in range(n):
        #     ans[i] = left_sum
        #     left_sum += nums[i]
        # right_sum = 0
        # for i in range(n-1, -1, -1):
        #     ans[i] = abs(ans[i] - right_sum)
        #     right_sum += nums[i]
        #
        # return ans

        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            nums[i] = abs(left_sum*2 + num - total)
            left_sum += num
        return nums


if __name__ == '__main__':
    print(Solution().leftRightDifference(nums = [10,4,8,3]))
    print(Solution().leftRightDifference(nums = [1]))
    print(Solution().leftRightDifference(nums = [1,2,3]))
