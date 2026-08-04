""" 3731. 找出缺失的元素   简单
给你一个整数数组 nums ，数组由若干 互不相同 的整数组成。
数组 nums 原本包含了某个范围内的 所有整数 。但现在，其中可能 缺失 部分整数。
该范围内的 最小 整数和 最大 整数仍然存在于 nums 中。
返回一个 有序 列表，包含该范围内缺失的所有整数，并 按从小到大排序。如果没有缺失的整数，返回一个 空 列表。

示例 1：输入： nums = [1,4,2,5];  输出： [3]
解释：最小整数为 1，最大整数为 5，因此完整的范围应为 [1,2,3,4,5]。其中只有 3 缺失。
示例 2：输入： nums = [7,8,6,9];  输出： []
解释：最小整数为 6，最大整数为 9，因此完整的范围为 [6,7,8,9]。所有整数均已存在，因此没有缺失的整数。
示例 3：输入： nums = [5,1];  输出： [2,3,4]
解释：最小整数为 1，最大整数为 5，因此完整的范围应为 [1,2,3,4,5]。缺失的整数为 2、3 和 4。

提示：
2 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

def findMissingElements(nums: List[int]) -> List[int]:
    # # 不用set
    # return [i for i in range(min(nums), max(nums) + 1) if i not in nums]
    # # i not in nums：每次查找需要遍历整个列表 → O(n)
    # # 总时间复杂度：O(n × m)，其中 n 是范围大小，m 是数组长度
    # # 最坏情况：如果范围很大，每次都要线性扫描整个数组

    # 使用set
    st = set(nums)
    return [i for i in range(min(st), max(st) + 1) if i not in st]
    # i not in st：set 底层是哈希表，查找只需要 O(1) 平均时间复杂度
    # 总时间复杂度：O(n + m)，创建 set 需要 O(m)，遍历范围需要 O(n)
    # 快得多！尤其是数据量大时

    # # list没有减法
    # return list(range(min(nums), max(nums) + 1)) - nums

    # # set是无序的，所以用set有错误案例
    # return list(set(range(min(nums), max(nums) + 1)) - set(nums))


if __name__ == '__main__':
    print(findMissingElements([1,4,2,5]))
    print(findMissingElements([7,8,6,9]))
    print(findMissingElements([5,1]))








