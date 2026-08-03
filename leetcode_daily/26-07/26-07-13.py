""" 1291. 顺次数   中等
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。

示例 1：输出：low = 100, high = 300;  输出：[123,234]
示例 2：输出：low = 1000, high = 13000;   输出：[1234,2345,3456,4567,5678,6789,12345]

提示：
10 <= low <= high <= 10^9
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-13.md

"""
from typing import List

DIGITS = "123456789"

nums = [12, 23, 34, 45, 56, 67, 78, 89,
        123, 234, 345, 456, 567, 678, 789,
        1234, 2345, 3456, 4567, 5678, 6789,
        12345, 23456, 34567, 45678, 56789,
        123456, 234567, 345678, 456789,
        1234567, 2345678, 3456789,
        12345678, 23456789,
        123456789]

def sequentialDigits(low: int, high: int) -> List[int]:
    # # 解法一：打表
    # l, r = bisect_left(nums, low), bisect_right(nums, high)
    # return nums[l:r]

    # # 解法二：枚举-纯枚举，逐位构造
    # ans = []
    # for i in range(1, 10):
    #     num = i
    #     for j in range(i + 1, 10):
    #         num = num * 10 + j
    #         if low <= num <= high:
    #             ans.append(num)
    # return sorted(ans)

    # # 解法三：枚举-字符串切片，静态截取
    # ans = []
    # low_len = len(str(low))
    # high_len = len(str(high))
    # for length in range(low_len, high_len+1):
    #     for r in range(length, len(DIGITS)+1):
    #         num = int(DIGITS[r-length:r])
    #         if low <= num <= high:
    #             ans.append(num)
    # return ans

    # 解法四：滑动窗口
    ans = []
    low_len = len(str(low))
    high_len = len(str(high))

    for length in range(low_len, high_len + 1):
        # 构造第一个顺次数（长度为 length）
        first_num = 0
        for i in range(1, length + 1):
            first_num = first_num * 10 + i

        # 计算模数（用于去掉最高位）
        mod = 10 ** (length - 1)

        # 滑动窗口：从第一个数开始，依次滑动
        num = first_num
        # 当前窗口的最后一位数字
        last_digit = length

        while num <= high and last_digit <= 9:
            if num >= low:
                ans.append(num)

            # 窗口向右滑动一位
            # 1. 去掉最高位，左移一位，加上新数字
            last_digit += 1
            if last_digit > 9:
                break
            num = (num % mod) * 10 + last_digit

    return ans


if __name__ == '__main__':
    print(sequentialDigits(low=100, high=300))
    print(sequentialDigits(low=1000, high=13000))
    print(sequentialDigits(low=1, high=9))
