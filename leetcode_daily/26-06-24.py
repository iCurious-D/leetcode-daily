""" 3700. 锯齿形数组的总数 II   困难
给你三个整数 n、l 和 r。
长度为 n 的锯齿形数组定义如下：
    每个元素的取值范围为 [l, r]。
    任意 两个 相邻的元素都不相等。
    任意 三个 连续的元素不能构成一个 严格递增 或 严格递减 的序列。
返回满足条件的锯齿形数组的总数。
由于答案可能很大，请将结果对 10^9 + 7 取余数。
序列 被称为 严格递增 需要满足：当且仅当每个元素都严格大于它的前一个元素（如果存在）。
序列 被称为 严格递减 需要满足，当且仅当每个元素都严格小于它的前一个元素（如果存在）。

示例 1：输入：n = 3, l = 4, r = 5;    输出：2
解释：在取值范围 [4, 5] 内，长度为 n = 3 的锯齿形数组只有 2 种：[4, 5, 4]  [5, 4, 5]

示例 2：输入：n = 3, l = 1, r = 3;    输出：10
解释：在取值范围 [1, 3] 内，长度为 n = 3 的锯齿形数组共有 10 种：
[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
所有数组均符合锯齿形条件。

提示：
3 <= n <= 10^9
1 <= l < r <= 75
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-24.md

"""
from typing import List


MOD = 10 ** 9 + 7

def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x*y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n&1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r-l+1
        m = [[0] * (k*2) for _ in range(k*2)]
        for i in range(k):
            for j in range(i):
                m[i][k+j] = 1
            for j in range(i+1, k):
                m[k+i][j] = 1
        f1 = [[1] for _ in range(k*2)]
        fn = pow_mul(m, n-1, f1)
        return sum(row[0] for row in fn) % MOD


if __name__ == '__main__':
    print(Solution().zigZagArrays(n=3, l=4, r=5))
    print(Solution().zigZagArrays(n=3, l=1, r=3))
    print(Solution().zigZagArrays(n=4, l=1, r=3))

