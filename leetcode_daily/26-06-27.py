""" 3020. 子集中元素的最大数量    中等
给你一个 正整数 数组 nums 。你需要从数组中选出一个满足下述条件的子集：
你可以将选中的元素放置在一个下标从 0 开始的数组中，并使其遵循以下模式：
[x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] （注意，k 可以是任何 非负 的 2 的幂）。
例如，[2, 4, 16, 4, 2] 和 [3, 9, 3] 都符合这一模式，而 [2, 4, 8, 4, 2] 则不符合。
返回满足这些条件的子集中，元素数量的 最大值 。

示例 1：输入：nums = [5,4,1,2,2];     输出：3
解释：选择子集 {4,2,2} ，将其放在数组 [2,4,2] 中，它遵循该模式，且 22 == 4 。因此答案是 3 。

示例 2：输入：nums = [1,3,2,4]    输出：1
解释：选择子集 {1}，将其放在数组 [1] 中，它遵循该模式。因此答案是 1 。注意我们也可以选择子集 {2} 、{4} 或 {3} ，可能存在多个子集都能得到相同的答案。

提示：
2 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-27.md

"""
from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = (cnt[1] - 1) | 1
        del cnt[1]

        for num in nums:
            res = 0
            while cnt.get(num, 0) >= 2:
                res += 2
                num *= num
            ans = max(ans, res+(1 if num in cnt else -1))

        return ans


if __name__ == '__main__':
    print(Solution().maximumLength(nums=[5,4,1,2,2]))
    print(Solution().maximumLength(nums=[1,3,2,4]))
    print(Solution().maximumLength(nums=[1,2,3,4,5]))

