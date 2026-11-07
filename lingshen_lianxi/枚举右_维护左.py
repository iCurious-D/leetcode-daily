""" §0.1 枚举右，维护左
对于 双变量问题，例如两数之和 a_i + a_j = t，
可以枚举右边的 a_j ，转化成 单变量问题，也就是在 a_j 左边查找是否有 a_i = t − a_j ，
这可以用哈希表维护。我把这个技巧叫做 枚举右，维护左。
下面这些题目，如果可以，请用一次遍历实现。
"""
from collections import defaultdict
from math import inf
from typing import List

# §0.1.1 基础 =====================================================================

# 1. 两数之和


# 1512. 好数对的数目 1161 相当于两数之差等于 0
def numIdenticalPairs(nums: List[int]) -> int:
    ans = 0
    cnt = defaultdict(int)
    for x in nums:
        ans += cnt[x]
        cnt[x] += 1
    return ans


# 2441. 与对应负数同时存在的最大正整数 1168 相当于两数之和等于 0
def findMaxK(nums: List[int]) -> int:
    ans = -1
    s = set()
    for num in nums:
        if -num in s:
            ans = max(ans, abs(num))
        s.add(num)
    return ans


# 4074. 和为目标值的最大乘积对 1232
def maxProductPair(nums: List[int], target: int) -> List[int]:
    dt = {}
    best_i, best_j = -1, -1
    for i, num in nums:
        if num * 2 == target:
            continue
        j = dt.get(target - num, -1)
        if j >= 0 and (best_i < 0 or num * (target-num) > nums[best_i] * (target - nums[best_i])):
            best_i, best_j = i, j
        dt[num] = i
    if best_i >= 0 and nums[best_i] < nums[best_j]:
        best_i, best_j = best_j, best_i
    return [best_i, best_j]


# 121. 买卖股票的最佳时机
def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# 2016. 增量元素之间的最大差值 1246
def maximumDifference(nums: List[int]) -> int:
    max_diff = 0
    min_num = inf
    for num in nums:
        max_diff = max(max_diff, num - min_num)
        min_num = min(min_num, num)
    return max_diff or -1


# 624. 数组列表中的最大距离
def maxDistance(arrays: List[List[int]]) -> int:
    max_dis = 0
    min_num = inf
    max_num = -inf
    for a in arrays:
        max_dis = max(max_dis, a[-1] - min_num, max_num - a[0])
        min_num = min(min_num, a[0])
        max_num = max(max_num, a[-1])
    return max_dis


# 3880. 两个值之间的最小绝对差值 1257



# 2342. 数位和相等数对的最大和 1309
# 3979. 最大有效数对和 1328
# 1128. 等价多米诺骨牌对的数量 1333
# 1679. K 和数对的最大数目 1346
# 面试题 16.24. 数对和
# 219. 存在重复元素 II
# 2260. 必须拿起的最小连续卡牌数 1365
# 2001. 可互换矩形的组数 1436
# 2815. 数组中的最大数对和 非暴力做法
# 3623. 统计梯形的数目 I 1580
# 2364. 统计坏数对的数目 1622
# 3805. 统计凯撒加密对数目 1624
# 3371. 识别数组中的最大异常值 1644
# 3761. 镜像对之间最小绝对距离 1669
# 1014. 最佳观光组合 1730
# 1814. 统计一个数组中好对子的数目 1738
# 3584. 子序列首尾元素的最大乘积 1763
# 2905. 找出满足差值条件的下标 II 1764 思考题：求下标对的个数
# 3837. 相等元素的延迟计数（会员题）
# 3907. 统计具有相反奇偶性的较小元素（会员题）



