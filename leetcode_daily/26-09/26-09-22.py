""" 3525. 求出数组的 X 值 II  困难
给你一个由 正整数 组成的数组 nums 和一个 正整数 k。
同时给你一个二维数组 queries，其中 queries[i] = [indexi, valuei, starti, xi]。
你可以对 nums 执行 一次 操作，移除 nums 的任意 后缀 ，使得 nums 仍然非空。
给定一个 x，nums 的 x值 定义为执行以上操作后剩余元素的 乘积 除以 k 的 余数 为 x 的方案数。
对于 queries 中的每个查询，你需要执行以下操作，然后确定 xi 对应的 nums 的 x值：
将 nums[indexi] 更新为 valuei。仅这个更改在接下来的所有查询中保留。
移除 前缀 nums[0..(starti - 1)]（nums[0..(-1)] 表示 空前缀 ）。
返回一个长度为 queries.length 的数组 result，其中 result[i] 是第 i 个查询的答案。
数组的一个 前缀 是从数组开始位置到任意位置的子数组。
数组的一个 后缀 是从数组中任意位置开始直到结束的子数组。
子数组 是数组中一段连续的元素序列。
注意：操作中所选的前缀或后缀可以是 空的 。
注意：x值在本题中与问题 I 有不同的定义。

示例 1：输入： nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]];  输出： [2,2,2]
解释：对于查询 0，nums 变为 [1, 2, 2, 4, 5] 。移除空前缀后，可选操作包括：
移除后缀 [2, 4, 5] ，nums 变为 [1, 2]。不移除任何后缀。nums 保持为 [1, 2, 2, 4, 5]，乘积为 80，对 3 取余为 2。
对于查询 1，nums 变为 [1, 2, 2, 3, 5] 。移除前缀 [1, 2, 2] 后，可选操作包括：
不移除任何后缀，nums 为 [3, 5]。移除后缀 [5] ，nums 为 [3]。
对于查询 2，nums 保持为 [1, 2, 2, 3, 5] 。移除空前缀后。可选操作包括：
移除后缀 [2, 2, 3, 5]。nums 为 [1]。移除后缀 [3, 5]。nums 为 [1, 2, 2]。
示例 2：输入： nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]];    输出： [1,0]
解释：对于查询 0，nums 变为 [2, 2, 4, 8, 16, 32]。唯一可行的操作是：移除后缀 [2, 4, 8, 16, 32]。
对于查询 1，nums 仍为 [2, 2, 4, 8, 16, 32]。没有任何操作能使余数为 1。
示例 3：输入： nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]];  输出： [5]

提示：
1 <= nums[i] <= 10^9
1 <= nums.length <= 10^5
1 <= k <= 5
1 <= queries.length <= 2 * 10^4
queries[i] == [indexi, valuei, starti, xi]
0 <= indexi <= nums.length - 1
1 <= valuei <= 10^9
0 <= starti <= nums.length - 1
0 <= xi <= k - 1

"""
from typing import List, Tuple

# 线段树有两个下标，一个是线段树节点的下标，另一个是线段树维护的区间的下标
# 节点的下标：从 1 开始，如果你想改成从 0 开始，需要把左右儿子下标分别改成 node*2+1 和 node*2+2
# 区间的下标：从 0 开始
class SegmentTree:
    def __init__(self, a: List[int], k: int):
        self._n = n = len(a)
        self._k = k
        self._tree = [None] * (2 << (n - 1).bit_length())
        self._build(a, 1, 0, n - 1)

    # 合并信息
    def _merge_data(self, a: Tuple[int, List[int]], b: Tuple[int, List[int]]) -> Tuple[int, List[int]]:
        cnt = a[1].copy()
        left_mul = a[0]
        for rx, c in enumerate(b[1]):
            cnt[left_mul * rx % self._k] += c
        return left_mul * b[0] % self._k, cnt

    def _new_data(self, val: int) -> Tuple[int, List[int]]:
        mul = val % self._k
        cnt = [0] * self._k
        cnt[mul] = 1
        return mul, cnt

    # 合并左右儿子的信息到当前节点
    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_data(self._tree[node * 2], self._tree[node * 2 + 1])

    # 用 a 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:  # 叶子
            self._tree[node] = self._new_data(a[l])  # 初始化叶节点的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子树
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:  # 叶子（到达目标）
            self._tree[node] = self._new_data(val)
            return
        m = (l + r) // 2
        if i <= m:  # i 在左子树
            self._update(node * 2, l, m, i, val)
        else:  # i 在右子树
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> Tuple[int, List[int]]:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_data(l_res, r_res)

    # 更新 a[i] 为 _new_data(val)
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    # 返回用 _merge_data 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> Tuple[int, List[int]]:
        return self._query(1, 0, self._n - 1, ql, qr)

def resultArray(nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        t = SegmentTree(nums, k)
        n = len(nums)
        ans = []
        for index, value, start, x in queries:
            t.update(index, value)
            _, cnt = t.query(start, n - 1)
            ans.append(cnt[x])
        return ans



