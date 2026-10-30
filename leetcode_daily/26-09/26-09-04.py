""" 3903. 最小稳定下标 I  简单
给你一个长度为 n 的整数数组 nums 和一个整数 k。
对于每个下标 i，定义它的 不稳定值 为 max(nums[0..i]) - min(nums[i..n - 1])。
换句话说：
max(nums[0..i]) 表示从下标 0 到下标 i 的元素中的 最大值 。
min(nums[i..n - 1]) 表示从下标 i 到下标 n - 1 的元素中的 最小值 。
如果某个下标 i 的不稳定值 小于等于 k，则称该下标为 稳定下标 。
返回 最小 的稳定下标。如果不存在这样的下标，则返回 -1。

示例 1：输入： nums = [5,0,1,4], k = 3;   输出： 3
解释：在下标 0 处：[5] 中的最大值是 5，[5, 0, 1, 4] 中的最小值是 0，因此不稳定值为 5 - 0 = 5。
在下标 1 处：[5, 0] 中的最大值是 5，[0, 1, 4] 中的最小值是 0，因此不稳定值为 5 - 0 = 5。
在下标 2 处：[5, 0, 1] 中的最大值是 5，[1, 4] 中的最小值是 1，因此不稳定值为 5 - 1 = 4。
在下标 3 处：[5, 0, 1, 4] 中的最大值是 5，[4] 中的最小值是 4，因此不稳定值为 5 - 4 = 1。
这是第一个不稳定值小于等于 k = 3 的下标，因此答案是 3。
示例 2：输入： nums = [3,2,1], k = 1;     输出： -1
解释：在下标 0 处，不稳定值为 3 - 1 = 2。在下标 1 处，不稳定值为 3 - 1 = 2。
在下标 2 处，不稳定值为 3 - 1 = 2。这些值都不小于等于 k = 1，因此答案是 -1。
示例 3：输入： nums = [0], k = 0;     输出： 0
解释：在下标 0 处，不稳定值为 0 - 0 = 0，它小于等于 k = 0。因此答案是 0。

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
0 <= k <= 10^9

"""
from itertools import accumulate


def firstStableIndex(nums: list[int], k: int) -> int:
    # 纯模拟，暴力切片，O(n²)
    # n = len(nums)
    # for i in range(n):
    #     if max(nums[:i+1]) - min(nums[i:]) <= k:
    #         return i
    # return -1

    # 前后缀预处理：O(n)
    # # accumulate 版
    # # 反向累积累 min 再翻回来，就是后缀最小值数组
    # suf_min = list(accumulate(reversed(nums), min))[::-1]
    # # 正向累积累 max 就是前缀最大值序列，zip 到一起逐个判定
    # for i, (pm, sm) in enumerate(zip(accumulate(nums, max), suf_min)):
    #     if pm - sm <= k:
    #         return i
    # return -1

    # # 显式双循环版
    # n = len(nums)
    # suf_min = [0] * n
    # suf_min[n - 1] = nums[-1]
    # for i in range(n - 2, -1, -1):
    #     suf_min[i] = min(suf_min[i + 1], nums[i])
    # pre_max = nums[0]
    # for i, x in enumerate(nums):
    #     if x > pre_max:       # 一条比较字节码，比每轮调 builtin max 便宜
    #         pre_max = x
    #     if pre_max - suf_min[i] <= k:
    #         return i
    #
    # return -1

    # 反向 accumulate 把 min 递推整个丢进 C 层跑，省掉一趟 Python 字节码循环
    # [::-1] 翻回正向：花一次 O(n) 拷贝，换后面下标直观
    suf_min = list(accumulate(reversed(nums), min))[::-1]

    # 第二趟刻意保留显式循环，不用 zip(accumulate(nums, max), ...)
    # 原因：留一个能自由改的循环体，题目变体（II）来了不用重写骨架
    pre_max = nums[0]                       # 不依赖「元素非负」的约束
    for i, x in enumerate(nums):
        if x > pre_max:                     # 一条比较字节码，比每轮调 builtin max 便宜
            pre_max = x
        # 不稳定值 = 左侧(含自己)最大值 - 右侧(含自己)最小值
        if pre_max - suf_min[i] <= k:
            return i                        # 正向扫，第一个命中就是最小下标
    return -1


if __name__ == '__main__':
    print(firstStableIndex([5,0,1,4], 3))
    print(firstStableIndex([3,2,1], 1))
    print(firstStableIndex([0], 0))




