""" 3658. 奇数和与偶数和的最大公约数     简单
给你一个整数 n。请你计算以下两个值的 最大公约数（GCD）：
sumOdd：最小的 n 个正奇数的总和。
sumEven：最小的 n 个正偶数的总和。
返回 sumOdd 和 sumEven 的 GCD。

示例 1：输入： n = 4; 输出： 4
解释：前 4 个奇数的总和 sumOdd = 1 + 3 + 5 + 7 = 16
前 4 个偶数的总和 sumEven = 2 + 4 + 6 + 8 = 20
因此，GCD(sumOdd, sumEven) = GCD(16, 20) = 4。

示例 2：输入： n = 5;     输出： 5
解释：前 5 个奇数的总和 sumOdd = 1 + 3 + 5 + 7 + 9 = 25
前 5 个偶数的总和 sumEven = 2 + 4 + 6 + 8 + 10 = 30
因此，GCD(sumOdd, sumEven) = GCD(25, 30) = 5。

提示：
1 <= n <= 1000
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-15.md

"""
from math import gcd

# 1 + 3 + ... + 2*n-1 = n*n
# 2 + 4 + ... + 2*n = n*(n+1)
def my_gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcdOfOddEvenSums(n: int) -> int:
    # return gcd(sum(range(1, 2*n, 2)), sum(range(2, 2*n+1, 2)))
    # return gcd(n*n, n*(n+1))
    return n


if __name__ == '__main__':
    print(gcdOfOddEvenSums(n=4))
    print(gcdOfOddEvenSums(n=5))
    print(gcdOfOddEvenSums(n=1))
