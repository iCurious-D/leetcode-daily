""" 3345. 最小可整除数位乘积 I   简单
给你两个整数 n 和 t 。
请你返回大于等于 n 的 最小 整数，且该整数的 各数位之积 能被 t 整除。

示例 1：输入：n = 10, t = 2;  输出：10
解释：10 的数位乘积为 0 ，可以被 2 整除，所以它是大于等于 10 且满足题目要求的最小整数。
示例 2：输入：n = 15, t = 3;  输出：16
解释：16 的数位乘积为 6 ，可以被 3 整除，所以它是大于等于 15 且满足题目要求的最小整数。

提示：
1 <= n <= 100
1 <= t <= 10
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-06.md

"""
from functools import reduce
from itertools import count
from operator import mul


def smallestNumber(n: int, t: int) -> int:
    num = n
    while True:
        product = 1
        for x in str(num):
            product *= int(x)
            if product % t == 0:
                return num
        num += 1

    # num = n
    # while True:
    #     product = reduce(mul, map(int, str(num)))
    #     if product % t == 0:
    #         return num
    #     num += 1

    # for num in count(n):
    #     product = 1
    #     x = num
    #     while x:
    #         x, d = divmod(x, 10)
    #         product *= d
        #     if product % t == 0:
        #         return num

    # def check(x: int) -> bool:
    #     product = 1
    #     while x:
    #         x, d = divmod(x, 10)
    #         product *= d
    #         if product == 0:
    #             break
    #     return product % t == 0
    #
    # while not check(n):
    #     n += 1
    #
    # return n


if __name__ == '__main__':
    print(smallestNumber(n = 10, t = 2))
    print(smallestNumber(n = 15, t = 3))
    print(smallestNumber(n = 100, t = 1))



