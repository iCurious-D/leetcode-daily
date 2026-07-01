""" 3699. 锯齿形数组的总数 I    困难
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
3 <= n <= 2000
1 <= l < r <= 2000
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-23.md

"""
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        k = r - l + 1

        f0 = [1] * k  # 后两个数递增
        f1 = [1] * k  # 后两个数递减

        # for _ in range(n - 1):
        #     new_f0 = [0] * k
        #     new_f1 = [0] * k
        #     for j in range(k):  # 枚举当前元素的值
        #         for p in range(j):  # 枚举前一个元素的值（p < j，递增）
        #             new_f0[j] += f1[p]  # 从递减状态转移过来
        #         for p in range(j + 1, k):  # 枚举前一个元素的值（p > j，递减）
        #             new_f1[j] += f0[p]  # 从递增状态转移过来
        #     f0, f1 = new_f0, new_f1

        for _ in range(n - 1):
            s0 = list(accumulate(f0, initial=0))
            s1 = list(accumulate(f1, initial=0))
            for j in range(k):
                f0[j] = s1[j] % MOD
                f1[j] = (s0[k] - s0[j + 1]) % MOD

        return (sum(f0) + sum(f1)) % MOD


if __name__ == '__main__':
    print(Solution().zigZagArrays(n=3, l=4, r=5))
    print(Solution().zigZagArrays(n=3, l=1, r=3))
    print(Solution().zigZagArrays(n=4, l=1, r=3))