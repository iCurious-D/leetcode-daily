"""  1752. 检查数组是否经排序和轮转得到
给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。
如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。
源数组中可能存在 重复项 。
注意：数组 A 在轮转 x 个位置后得到长度相同的数组 B ，使得对于每一个有效的下标 i，满足 B[i] == A[(i+x) % A.length]。

示例 1：输入：nums = [3,4,5,1,2]    输出：true
解释：[1,2,3,4,5] 为有序的源数组。可以轮转 x = 2 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。

示例 2：输入：nums = [2,1,3,4]    输出：false
解释：源数组无法经轮转得到 nums 。

示例 3：输入：nums = [1,2,3]   输出：true
解释：[1,2,3] 为有序的源数组。可以轮转 x = 0 个位置（即不轮转）得到 nums 。

提示：
1 <= nums.length <= 100
1 <= nums[i] <= 100
=======================================================================================


"""
from typing import List
from itertools import pairwise


class Solution:
    def check(self, nums: List[int]) -> bool:
        # n = len(nums)
        # min_index = 0
        # for i in range(1, n):
        #     if nums[i] < nums[i-1]:
        #         min_index = i
        #         break
        # if min_index == 0:
        #     return True
        # for i in range(min_index+1, n):
        #     if nums[i] < nums[i-1]:
        #         return False
        # return nums[-1] <= nums[0]
        is_sorted = nums[0]>=nums[-1]
        for x, y in pairwise(nums):
            if x > y:
                if not is_sorted:
                    return False
                is_sorted = False
        return True

        # n = len(nums)
        # count = 0  # 断崖计数器
        # for i in range(n):
        #     # 检查当前元素和下一个元素的相邻关系（注意：末尾的下一个是开头，用取模实现）
        #     if nums[i] > nums[(i + 1) % n]:
        #         count += 1
        #     # 断崖超过一处，直接判定为假冒伪劣，退货
        #     if count > 1:
        #         return False
        # return True


if __name__ == '__main__':
    print(Solution().check([3,4,5,1,2]))
    print(Solution().check([2,1,3,4]))
    print(Solution().check([1,2,3]))


