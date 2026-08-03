""" 3754. 连接非零数字并乘以其数字和 I   简单
给你一个整数 n。
将 n 中所有的 非零数字 按照它们的原始顺序连接起来，形成一个新的整数 x。如果不存在 非零数字 ，则 x = 0。
sum 为 x 中所有数字的 数字和 。
返回一个整数，表示 x * sum 的值。

示例 1：输入： n = 10203004；  输出： 12340
解释：非零数字是 1、2、3 和 4。因此，x = 1234。数字和为 sum = 1 + 2 + 3 + 4 = 10。因此，答案是 x * sum = 1234 * 10 = 12340。

示例 2：输入： n = 1000；  输出： 1
解释：非零数字是 1，因此 x = 1 且 sum = 1。因此，答案是 x * sum = 1 * 1 = 1。

提示：
0 <= n <= 10^9
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-07.md

"""
def sumAndMultiply(n: int) -> int:
    x, s, pow10 = 0, 0, 1
    while n:
        n, d = divmod(n, 10)
        if d:
            x += pow10 * d
            s += d
            pow10 *= 10
    return x * s


if __name__ == '__main__':
    print(sumAndMultiply(10203004))
    print(sumAndMultiply(1000))
    print(sumAndMultiply(0))
    print(sumAndMultiply(123456789))
