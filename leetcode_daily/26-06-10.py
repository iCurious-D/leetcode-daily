""" 3691. 最大子数组总值 II
给你一个长度为 n 的整数数组 nums 和一个整数 k。
你必须从 nums 中选择 恰好 k 个 不同 的非空子数组 nums[l..r]。
子数组可以重叠，但同一个子数组（相同的 l 和 r）不能 被选择超过一次。

子数组 nums[l..r] 的 值 定义为：max(nums[l..r]) - min(nums[l..r])。
总值 是所有被选子数组的 值 之和。
返回你能实现的 最大 可能总值。子数组 是数组中连续的 非空 元素序列。

示例 1:输入: nums = [1,3,2], k = 2 ; 输出: 4
解释:一种最优的方法是：
选择 nums[0..1] = [1, 3]。最大值为 3，最小值为 1，得到的值为 3 - 1 = 2。
选择 nums[0..2] = [1, 3, 2]。最大值仍为 3，最小值仍为 1，所以值也是 3 - 1 = 2。
将它们相加得到 2 + 2 = 4。

示例 2:输入: nums = [4,2,5,1], k = 3 ; 输出: 12
解释:一种最优的方法是：
选择 nums[0..3] = [4, 2, 5, 1]。最大值为 5，最小值为 1，得到的值为 5 - 1 = 4。
选择 nums[1..3] = [2, 5, 1]。最大值为 5，最小值为 1，所以值也是 4。
选择 nums[2..3] = [5, 1]。最大值为 5，最小值为 1，所以值同样是 4。
将它们相加得到 4 + 4 + 4 = 12。

提示:
1 <= n == nums.length <= 5 * 10^4
0 <= nums[i] <= 10^9
1 <= k <= min(10^5, n * (n + 1) / 2)
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-10.md

"""
from typing import List, Tuple
from heapq import heapreplace_max


# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

def op(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return min(a[0], b[0]), max(a[1], b[1])

class ST:
    def __init__(self, a: List[int]):
        n = len(a)
        w = n.bit_length()
        st = [[None] * n for _ in range(w)]
        st[0] = [(x, x) for x in a]
        for i in range(1, w):
            for j in range(n - (1 << i) + 1):
                st[i][j] = op(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
        self.st = st

    # [l, r) 左闭右开
    def query(self, l: int, r: int) -> int:
        """ 查询方法：接收左端点 l 和右端点 r（注意是左闭右开区间 [l, r)），返回该区间的极差（max - min） """
        k = (r - l).bit_length() - 1
        mn, mx = op(self.st[k][l], self.st[k][r - (1 << k)])
        return mx - mn

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 构建稀疏表 st，用于快速查询任意子数组的极差
        st = ST(nums)

        # 最大堆中保存 (子数组值，左端点，右端点加一)
        # 创建列表 h，作为最大堆使用：对于每个左端点 i（从 0 到 n-1），计算以 i 为起点、右端点为 n-1 的子数组的极差
        h = [(st.query(i, n), i, n) for i in range(n)]
        # 由于 h 是递减的，无需堆化

        ans = 0
        for _ in range(k):
            # 取出堆顶元素（当前极差最大的子数组）：(d, l, r)，d 是极差，l 是左端点，r 是右端点加一（左闭右开表示）
            d, l, r = h[0]
            # 如果 d 等于 0，说明堆中剩余的元素极差都是 0（数组元素都相同），提前退出循环
            if d == 0:
                break
            ans += d
            # 调用 heapreplace_max：将堆顶替换为新元素
            # 新元素的左端点还是 l，右端点缩短一位变成 r - 1
            heapreplace_max(h, (st.query(l, r - 1), l, r - 1))
        return ans

if __name__ == '__main__':
    print(Solution().maxTotalValue(nums = [1,3,2], k = 2))
    print(Solution().maxTotalValue(nums = [4,2,5,1], k = 3))
