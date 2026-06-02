"""  3043. 最长公共前缀的长度
给你两个 正整数 数组 arr1 和 arr2 。
正整数的 前缀 是其 最左边 的一位或多位数字组成的整数。例如，123 是整数 12345 的前缀，而 234 不是 。
设若整数 c 是整数 a 和 b 的 公共前缀 ，那么 c 需要同时是 a 和 b 的前缀。
例如，5655359 和 56554 有公共前缀 565 和 5655，而 1223 和 43456 没有 公共前缀。

你需要找出属于 arr1 的整数 x 和属于 arr2 的整数 y 组成的所有数对 (x, y) 之中最长的公共前缀的长度。
返回所有数对之中最长公共前缀的长度。如果它们之间不存在公共前缀，则返回 0 。


示例 1：输入：arr1 = [1,10,100], arr2 = [1000]   输出：3
解释：存在 3 个数对 (arr1[i], arr2[j]) ：
- (1, 1000) 的最长公共前缀是 1 。
- (10, 1000) 的最长公共前缀是 10 。
- (100, 1000) 的最长公共前缀是 100 。
最长的公共前缀是 100 ，长度为 3 。

示例 2：输入：arr1 = [1,2,3], arr2 = [4,4,4]   输出：0
解释：任何数对 (arr1[i], arr2[j]) 之中都不存在公共前缀，因此返回 0 。
请注意，同一个数组内元素之间的公共前缀不在考虑范围内。

提示：
1 <= arr1.length, arr2.length <= 5 * 104
1 <= arr1[i], arr2[i] <= 10^8
========================================================================

题解路径：. / leetcode_daily_stories / 26-05-21.md

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # prefix_set = set()
        # for num in arr1:
        #     s = str(num)
        #     for i in range(1, len(s)+1):
        #         prefix_set.add(s[:i])
        # max_len = 0
        # for num in arr2:
        #     s = str(num)
        #     for i in range(len(s), 0, -1):
        #         if s[:i] in prefix_set:
        #             max_len = max(max_len, i)
        #             break
        # return max_len
        ancestors = set()
        for num in arr1:
            while num:
                ancestors.add(num)
                num //= 10
        max_prefix = 0
        for num in arr2:
            while num:
                if num in ancestors:
                    max_prefix = max(max_prefix, num)
                    break
                num //= 10
        return len(str(max_prefix)) if max_prefix else 0


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([1,10,100], [1000]))
    print(Solution().longestCommonPrefix([1,2,3], [4,4,4]))
    print(Solution().longestCommonPrefix([1,2,3], [1,2,3]))
