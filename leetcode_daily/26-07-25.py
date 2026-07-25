""" 3536. 两个数字的最大乘积     简单
给定一个正整数 n。
返回 任意两位数字 相乘所得的 最大 乘积。
注意：如果某个数字在 n 中出现多次，你可以多次使用该数字。

示例 1：输入： n = 31;    输出： 3
解释：n 的数字是 [3, 1]。任意两位数字相乘的结果为：3 * 1 = 3。最大乘积为 3。
示例 2：输入： n = 22;    输出： 4
解释：n 的数字是 [2, 2]。任意两位数字相乘的结果为：2 * 2 = 4。最大乘积为 4。
示例 3：输入： n = 124;   输出： 8
解释：n 的数字是 [1, 2, 4]。任意两位数字相乘的结果为：1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8。最大乘积为 8。

提示：
10 <= n <= 10^9
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-25.md

"""
def maxProduct(n: int) -> int:
    first, second = 0, 0
    while n:
        x = n % 10
        if x > first:
            first, second = x, first
        elif x > second:
            second = x
        n //= 10
    return first * second

    # s = sorted(str(n))
    # return int(s[-1]) * int(s[-2])


if __name__ == '__main__':
    print(maxProduct(31))
    print(maxProduct(22))
    print(maxProduct(124))

