""" 3116. 单面值组合的第 K 小金额     困难
给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。
你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。
返回使用这些硬币能制造的 第 kth 小 金额。

示例 1：输入： coins = [3,6,9], k = 3;    输出： 9
解释：给定的硬币可以制造以下金额：3元硬币产生3的倍数：3, 6, 9, 12, 15等。
6元硬币产生6的倍数：6, 12, 18, 24等。9元硬币产生9的倍数：9, 18, 27, 36等。
所有硬币合起来可以产生：3, 6, 9, 12, 15等。

示例 2：输入：coins = [5,2], k = 7;       输出：12
解释：给定的硬币可以制造以下金额：
5元硬币产生5的倍数：5, 10, 15, 20等。2元硬币产生2的倍数：2, 4, 6, 8, 10, 12等。
所有硬币合起来可以产生：2, 4, 5, 6, 8, 10, 12, 14, 15等。

提示：
1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 10^9
coins 包含两两不同的整数。

"""
from bisect import bisect_left
from typing import List
from math import gcd


# def findKthSmallest(coins: List[int], k: int) -> int:
#     pass

def findKthSmallest(coins: List[int], k: int) -> int:
    # # 最后加个去冗余
    # tmp = []
    # coins.sort()
    # while coins:
    #     c = coins.pop()
    #     if all(c % i for i in coins):
    #         tmp.append(c)
    # if len(tmp) == 1:
    #     return tmp.pop() * k
    #
    # coins = tmp

    n = len(coins)
    subsets = []  # 存储 (lcm, 符号)
    # 枚举所有非空子集
    for mask in range(1, 1 << n):  # mask 从 1 到 2^n - 1
        l = 1  # 当前子集的 lcm
        bits = 0  # 子集中有几种硬币

        # 检查哪些硬币在这个子集中
        for i in range(n):
            if mask & (1 << i):  # 第 i 位是 1，说明 coins[i] 在子集里
                c = coins[i]
                l = l // gcd(l, c) * c  # 更新 lcm
                bits += 1

        # 奇数个集合 -> 加；偶数个集合 -> 减
        sign = 1 if bits % 2 == 1 else -1
        subsets.append((l, sign))

    # 计算 <= x 的能生成金额个数
    def count_le(x: int) -> int:
        total = 0
        for l, sign in subsets:
            if l <= x:  # 如果 lcm 已经大于 x，没有贡献
                total += sign * (x // l)
        return total

    # 二分查找
    return bisect_left(range(min(coins)*k), k, k, key=count_le)
    # lo = 1
    # hi = min(coins) * k  # 二分上界：最小面额硬币的第 k 个倍数
    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if count_le(mid) >= k:
    #         hi = mid
    #     else:
    #         lo = mid + 1
    # return lo


if __name__ == '__main__':
    print(findKthSmallest(coins=[3,6,9], k=3))
    print(findKthSmallest(coins=[5,2], k=7))













