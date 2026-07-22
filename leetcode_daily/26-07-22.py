""" 3501. 操作后最大活跃区段数 II     困难
给你一个长度为 n 的二进制字符串 s ，其中：
'1' 表示一个 活跃 区段。'0' 表示一个 非活跃 区段。
你最多可以进行一次 操作 来最大化 s 中活跃区段的数量。在一次操作中，你可以：
将一个被 '0' 包围的连续 '1' 区块转换为全 '0'。然后，将一个被 '1' 包围的连续 '0' 区块转换为全 '1'。
此外，你还有一个 二维数组 queries，其中 queries[i] = [li, ri] 表示子字符串 s[li...ri]。
对于每个查询，确定在对子字符串 s[li...ri] 进行最优交换后，字符串 s 中 可能的最大 活跃区段数。
返回一个数组 answer，其中 answer[i] 是 queries[i] 的结果。
注意:对于每个查询，仅对 s[li...ri] 处理时，将其看作是在两端都加上一个 '1' 后的字符串，形成 t = '1' + s[li...ri] + '1'。
这些额外的 '1' 不会对最终的活跃区段数有贡献。各个查询相互独立。

示例 1：输入： s = "01", queries = [[0,1]];   输出： [1]
解释：因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数是 1。

示例 2：输入： s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]];   输出： [4,3,1,1]
解释：查询 [0, 3] → 子字符串 "0100" → 变为 "101001"
选择 "0100"，"0100" → "0000" → "1111"。最终字符串（去掉添加的 '1'）为 "1111"。最大活跃区段数为 4。
查询 [0, 2] → 子字符串 "010" → 变为 "10101"
选择 "010"，"010" → "000" → "111"。最终字符串（去掉添加的 '1'）为 "1110"。最大活跃区段数为 3。
查询 [1, 3] → 子字符串 "100" → 变为 "11001"
因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 1。
查询 [2, 3] → 子字符串 "00" → 变为 "1001"
因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 1。

示例 3：输入： s = "1000100", queries = [[1,5],[0,6],[0,4]];  输出： [6,7,2]
解释：查询 [1, 5] → 子字符串 "00010" → 变为 "1000101"
选择 "00010"，"00010" → "00000" → "11111"。最终字符串（去掉添加的 '1'）为 "1111110"。最大活跃区段数为 6。
查询 [0, 6] → 子字符串 "1000100" → 变为 "110001001"
选择 "000100"，"000100" → "000000" → "111111"。最终字符串（去掉添加的 '1'）为 "1111111"。最大活跃区段数为 7。
查询 [0, 4] → 子字符串 "10001" → 变为 "1100011"
因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 2。

示例 4：输入： s = "01010", queries = [[0,3],[1,4],[1,3]];    输出： [4,4,2]
解释：查询 [0, 3] → 子字符串 "0101" → 变为 "101011"
选择 "010"，"010" → "000" → "111"。最终字符串（去掉添加的 '1'）为 "11110"。最大活跃区段数为 4。
查询 [1, 4] → 子字符串 "1010" → 变为 "110101"
选择 "010"，"010" → "000" → "111"。最终字符串（去掉添加的 '1'）为 "01111"。最大活跃区段数为 4。
查询 [1, 3] → 子字符串 "101" → 变为 "11011"
因为没有被 '0' 包围的 '1' 区块，所以没有有效的操作可以进行。最大活跃区段数为 2。

提示：
1 <= n == s.length <= 10^5
1 <= queries.length <= 10^5
s[i] 只有 '0' 或 '1'。
queries[i] = [li, ri]
0 <= li <= ri < n
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-22.md

"""
from bisect import bisect_left, bisect_right
from itertools import groupby
from typing import List


# class SegmentTree:
#     def __init__(self, arr):
#         self.n = len(arr)
#         self.arr = arr
#         self.seg = [0] * (self.n << 2)
#
#         if self.n:
#             self.build(1, 0, self.n - 1)
#
#     def build(self, p: int, l: int, r: int) -> None:
#         if l == r:
#             self.seg[p] = self.arr[l]
#             return
#
#         mid = (l + r) >> 1
#
#         self.build(p << 1, l, mid)
#         self.build(p << 1 | 1, mid + 1, r)
#
#         self.seg[p] = max(
#             self.seg[p << 1],
#             self.seg[p << 1 | 1]
#         )
#
#     def query(self, L: int, R: int) -> int:
#         if L > R:
#             return 0

#         def _query(p: int, l: int, r: int) -> int:
#             if L <= l and r <= R:
#                 return self.seg[p]#
#             mid = (l + r) >> 1
#             res = 0
#             if L <= mid:
#                 res = max(res, _query(p << 1, l, mid))
#
#             if R > mid:
#                 res = max(res, _query(p << 1 | 1, mid + 1, r))
#             return res
#
#         return _query(1, 0, self.n - 1)


class SegmentTree:
    """线段树，维护区间最大值"""
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        mid = (l + r) // 2
        self._build(arr, node * 2, l, mid)
        self._build(arr, node * 2 + 1, mid + 1, r)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, ql, qr):
        """查询区间 [ql, qr] 最大值，包含边界"""
        return self._query(1, 0, self.n - 1, ql, qr)

    def _query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return -10**9  # 足够小的值
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self._query(node * 2, l, mid, ql, qr)
        right = self._query(node * 2 + 1, mid + 1, r, ql, qr)
        return max(left, right)

class SparseTable:
    def __init__(self, data: list):
        # st[0] = 原数组，长度为 1 的区间
        self.st = [list(data)]
        # i: 当前层的 k 值（从 1 开始）
        # N: 原数组长度
        i, N = 1, len(self.st[0])

        # 当 2^k <= N 时继续构建
        # 2*i <= N+1 等价于 i <= N/2，即 2^k <= N
        while 2 * i <= N+1:
            # 上一层（k-1 层）的数据
            pre = self.st[-1]
            # 计算当前层（k 层）的所有区间最大值
            # pre[j] = st[k-1][j]，左半部分的最大值
            # pre[j + i] = st[k-1][j + 2^(k-1)]，右半部分的最大值
            # 区间范围：j 从 0 到 N - 2^k，共 N - 2^k + 1 个区间
            self.st.append([max(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1  # i *= 2，进入下一层（k++）

    def query(self, begin: int, end: int):
        # 用两个重叠的 2^k 区间覆盖目标区间
        if begin > end:
            return 0
        # bit_length() 返回二进制位数
        # 例如 5 的二进制是 101，bit_length() = 3
        # 所以 lg = 3 - 1 = 2，即 2^2 = 4 <= 5
        lg = (end - begin+1).bit_length() - 1
        return max(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])


def maxActiveSectionsAfterTrade(s: str, queries: List[List[int]]) -> List[int]:
    # 解法一
    n = len(s)
    total1_all = s.count('1')

    # 1. 按连续字符分组
    groups = []  # (char, start, end)
    start = 0
    for char, g in groupby(s):
        length = sum(1 for _ in g)
        groups.append((char, start, start + length - 1))
        start += length

    # 2. 提取废丹堆（'0' 组）
    # 从所有区块中筛选出 '0' 区块，重新组织为：(起始位置, 结束位置, 长度)
    zero_groups = [(st, ed, ed - st + 1) for ch, st, ed in groups if ch == '0']
    m = len(zero_groups)

    if m < 2:
        # 没有废丹，任何操作都无法增加极品丹 / 或只有一个 '0' 区块，无法配对
        return [total1_all] * len(queries)

    # 提取所有 '0' 区块的起始位置数组、结束位置数组，用于二分查找
    zero_starts = [zg[0] for zg in zero_groups]
    zero_ends = [zg[1] for zg in zero_groups]

    # 提取所有 '0' 区块的长度数组，用于构建线段树
    zero_len = [zg[2] for zg in zero_groups]

    # 3. 构建相邻废丹堆长度和的线段树
    # adj[i] 表示第 i 个和第 i+1 个 '0' 区块的长度之和
    adj = [zero_len[i] + zero_len[i + 1] for i in range(m - 1)]
    # 用 adj 数组构建线段树，支持快速查询区间最大值
    seg = SegmentTree(adj)

    # 4. 处理查询
    ans = []
    for l, r in queries:
        # 二分定位：找到第一个右边界 >= l 的 '0' 区块索引 == 第一个与 [l, r] 相交的废丹组
        left_idx = bisect_left(zero_ends, l)
        # bisect_right 找第一个左边界 > r 的位置，减 1 就是最后一个左边界 <= r 的 '0' 区块索引 == 最后一个与 [l, r] 相交的废丹组
        right_idx = bisect_right(zero_starts, r) - 1

        # 区间内没有废丹组 / 只有一个废丹组，无法配对
        # left_idx >= m: 所有 '0' 区块的右边界都 < l，没有交集
        # right_idx < 0: 所有 '0' 区块的左边界都 > r，没有交集
        # left_idx >= right_idx: 区间内最多只有 1 个 '0' 区块（0 个或 1 个）
        if left_idx >= m or right_idx < 0 or left_idx >= right_idx:
            ans.append(total1_all)
            continue

        # 计算首尾废丹组被截断后的实际长度
        left_len = min(zero_ends[left_idx], r) - max(zero_starts[left_idx], l) + 1
        right_len = min(zero_ends[right_idx], r) - max(zero_starts[right_idx], l) + 1

        count = right_idx - left_idx + 1  # 区间内的废丹组数量
        if count == 2:
            # 恰好 2 个废丹组，直接配对
            mx = left_len + right_len
        else:
            # 超过 2 个废丹组，三种选择取最大值
            # 选择1：第一个（可能截断）+ 第二个（完整）
            val1 = left_len + zero_len[left_idx + 1]
            # 选择2：倒数第二个（完整）+ 最后一个（可能截断）
            val2 = zero_len[right_idx - 1] + right_len
            # 选择3：中间完整的相邻对（线段树查询）
            val3 = seg.query(left_idx + 1, right_idx - 2) if seg else 0
            # 查询 adj[left_idx+1 ... right_idx-2] 的最大值
            # adj[k] 对应 zero_groups[k] 和 zero_groups[k+1] 这对
            # 所以查询范围是从 (left_idx+1, left_idx+2) 到 (right_idx-2, right_idx-1)
            # 这些都是完全在查询区间内的完整相邻对
            # 如果 seg 为 None（只有一个 '0' 区块），返回 0

            mx = max(val1, val2, val3)

        ans.append(total1_all + mx)

    return ans


    # n = len(s)
    #
    # # 统计整个字符串中 '1' 的总数（家底，一颗都不会少）
    # cnt1 = s.count('1')
    #
    # # 预处理：提取所有连续 '0' 区块的信息
    # zeroBlocks = []  # 每个 '0' 区块的长度
    # blockLeft = []  # 每个 '0' 区块的左边界索引
    # blockRight = []  # 每个 '0' 区块的右边界索引
    #
    # i = 0
    # while i < n:
    #     st = i
    #     while i < n and s[i] == s[st]:
    #         i += 1
    #     if s[st] == '0':
    #         zeroBlocks.append(i - st)  # 区块长度 = 结束位置 - 起始位置
    #         blockLeft.append(st)  # 左边界
    #         blockRight.append(i - 1)  # 右边界（最后一个 '0' 的位置）
    #
    # m = len(zeroBlocks)
    # # 如果 '0' 区块少于 2 个，无法进行任何操作（需要至少两个 '0' 区块才能配对）
    # if m < 2:
    #     return [cnt1] * len(queries)
    #
    # # 预处理相邻 '0' 区块对的长度和
    # # tmpSum[i] 表示第 i 个和第 i+1 个 '0' 区块的长度之和
    # tmpSum = [zeroBlocks[i] + zeroBlocks[i + 1] for i in range(m - 1)]
    #
    # # 构建线段树，支持快速查询区间最大值
    # seg = SegmentTree(tmpSum)
    # # st = SparseTable(tmpSum)
    #
    # ans = []
    #
    # for l, r in queries:
    #     # 二分查找：找到查询区间 [l, r] 内包含的第一个和最后一个 '0' 区块的索引
    #
    #     # bisect_left(blockRight, l) 找到第一个右边界 >= l 的 '0' 区块
    #     # 这个区块可能与查询区间有交集（即使左边界 < l，只要右边界 >= l 就有交集）
    #     i = bisect_left(blockRight, l)
    #     # bisect_right(blockLeft, r) 找到第一个左边界 > r 的 '0' 区块
    #     # 减 1 后得到最后一个左边界 <= r 的 '0' 区块，这个区块也可能与查询区间有交集
    #     j = bisect_right(blockLeft, r) - 1
    #
    #     # 边界条件判断：
    #     # i > m - 1: 所有 '0' 区块的右边界都 < l，即没有 '0' 区块在查询区间内
    #     # j < 0: 所有 '0' 区块的左边界都 > r，即没有 '0' 区块在查询区间内
    #     # i >= j: 查询区间内最多只有 1 个 '0' 区块，无法配对
    #     if i > m - 1 or j < 0 or i >= j:
    #         # 无法进行操作，直接返回 '1' 的总数
    #         ans.append(cnt1)
    #         continue
    #
    #     # 计算第一个 '0' 区块在查询区间内的实际长度
    #     # blockRight[i] 是第 i 个 '0' 区块的右边界，max(blockLeft[i], l) 是该区块在查询区间内的实际左边界
    #     # +1 是因为长度 = 右边界 - 左边界 + 1
    #     firstLen = blockRight[i] - max(blockLeft[i], l) + 1
    #
    #     # 计算最后一个 '0' 区块在查询区间内的实际长度
    #     # min(blockRight[j], r) 是该区块在查询区间内的实际右边界，blockLeft[j] 是该区块的左边界
    #     lastLen = min(blockRight[j], r) - blockLeft[j] + 1
    #
    #     # 情况1：查询区间内恰好有 2 个 '0' 区块
    #     # 这两个区块可以直接配对（中间必然隔着至少一个 '1' 区块）
    #     if i + 1 == j:
    #         bestGain = firstLen + lastLen  # 收益就是两个区块的实际长度之和
    #         ans.append(cnt1 + bestGain)
    #         continue
    #
    #     # 情况2：查询区间内有超过 2 个 '0' 区块，有三种选择：
    #     # 选择1：第一个 '0' 区块（可能被截断） + 第二个完整的 '0' 区块
    #     val1 = firstLen + zeroBlocks[i + 1]
    #     # 选择2：倒数第二个完整的 '0' 区块 + 最后一个 '0' 区块（可能被截断）
    #     val2 = zeroBlocks[j - 1] + lastLen
    #     # 选择3：中间某两个完整的相邻 '0' 区块配对
    #     # seg.query(i + 1, j - 2) 查询 tmpSum[i+1 ... j-2] 的最大值
    #     # tmpSum[k] 对应 zeroBlocks[k] + zeroBlocks[k+1]
    #     # 所以查询范围是 [i+1, j-2]，对应从 (i+1, i+2) 到 (j-2, j-1) 的所有相邻对
    #     val3 = seg.query(i + 1, j - 2)
    #     # val3 = st.query(i + 1, j - 2)
    #
    #     # 取三种选择的最大值作为最优收益
    #     bestGain = max(val1, val2, val3)
    #
    #     # 最终答案 = 原有 '1' 的数量 + 最大收益
    #     ans.append(cnt1 + bestGain)
    #
    # return ans





# 对于每个查询，需要找到区间内相邻的两个 '0' 区块，使得它们的长度之和最大
# 但这需要 O(m) 的时间，总体还是 O(q*m)，可能超时

# 换个思路：预处理出所有相邻 '0' 区块对的长度和，以及它们覆盖的区间范围
# 然后用某种数据结构（如线段树或稀疏表）来快速查询区间最大值

# 但实际上，对于查询 [l, r]，我们只关心完全包含在 [l, r] 内的 '0' 区块
# 以及它们在原序列中的相邻关系

# 更优的思路：对于每对相邻的 '0' 区块，记录它们的长度和以及覆盖范围
# 然后对于查询，找出所有完全在查询范围内的相邻对，取最大值

# 构建相邻 '0' 区块对的信息
# pair_info[i] = (sum_of_lengths, left_block_start, right_block_end)





if __name__ == '__main__':
    print(maxActiveSectionsAfterTrade("01", [[0, 1]]))
    print(maxActiveSectionsAfterTrade("0100", [[0, 3], [0, 2], [1, 3], [2, 3]]))
    print(maxActiveSectionsAfterTrade("1000100", [[1, 5], [0, 6], [0, 4]]))
    print(maxActiveSectionsAfterTrade("01010", [[0, 3], [1, 4], [1, 3]]))











