""" 2213. 由单个字符重复的最长子字符串    困难
给你一个下标从 0 开始的字符串 s 。另给你:
一个下标从 0 开始、长度为 k 的字符串 queryCharacters ，一个下标从 0 开始、长度也是 k 的整数 下标 数组 queryIndices ，
这两个都用来描述 k 个查询。
第 i 个查询会将 s 中位于下标 queryIndices[i] 的字符更新为 queryCharacters[i] 。
返回一个长度为 k 的数组 lengths ，其中 lengths[i] 是在执行第 i 个查询 之后 s 中仅由 单个字符重复 组成的 最长子字符串 的 长度 。


示例 1：输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3];  输出：[3,3,4]
解释：- 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
- 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
- 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
因此，返回 [3,3,4] 。
示例 2：输入：s = "abyzz", queryCharacters = "aa", queryIndices = [2,1];  输出：[2,3]
解释：- 第 1 次查询更新后 s = "abazz" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
- 第 2 次查询更新后 s = "aaazz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
因此，返回 [2,3] 。

提示：
1 <= s.length <= 10^5
s 由小写英文字母组成
k == queryCharacters.length == queryIndices.length
1 <= k <= 10^5
queryCharacters 由小写英文字母组成
0 <= queryIndices[i] < s.length
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-13.md

"""
from typing import List
from sortedcontainers import SortedList


def longestRepeating(s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    # 解法一
    n = len(s)
    s = list(s)
    segs = SortedList()  # (left, right)
    lens = SortedList()  # 每段长度

    # 初始化连续段
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        segs.add((i, j - 1))
        lens.add(j - i)
        i = j

    ans = []

    for pos, ch in zip(queryIndices, queryCharacters):
        if s[pos] == ch:
            ans.append(lens[-1])
            continue

        # 删掉 pos 所在旧段
        idx = segs.bisect_right((pos, n)) - 1
        L, R = segs[idx]
        segs.pop(idx)
        lens.remove(R - L + 1)

        # 旧段拆成左右两部分
        if L <= pos - 1:
            segs.add((L, pos - 1))
            lens.add(pos - L)
        if pos + 1 <= R:
            segs.add((pos + 1, R))
            lens.add(R - pos)

        # 新字符先单独成段
        newL = newR = pos

        # 合并右边相邻段
        if pos + 1 < n and s[pos + 1] == ch:
            idx = segs.bisect_left((pos + 1, -1))
            rightL, rightR = segs[idx]
            segs.pop(idx)
            lens.remove(rightR - rightL + 1)
            newR = rightR

        # 合并左边相邻段
        if pos > 0 and s[pos - 1] == ch:
            idx = segs.bisect_left((pos, -1)) - 1
            leftL, leftR = segs[idx]
            segs.pop(idx)
            lens.remove(leftR - leftL + 1)
            newL = leftL

        segs.add((newL, newR))
        lens.add(newR - newL + 1)
        s[pos] = ch
        ans.append(lens[-1])

    return ans

    # n = len(s)
    # s = list(s)
    #
    # segs = SortedList()  # (left, right)
    # lens = SortedList()  # 每段长度
    #
    # def add_seg(l: int, r: int) -> None:
    #     segs.add((l, r))
    #     lens.add(r - l + 1)
    #
    # def pop_seg(idx: int):
    #     l, r = segs.pop(idx)
    #     lens.remove(r - l + 1)
    #     return l, r
    #
    # # 初始化连续段
    # i = 0
    # while i < n:
    #     j = i
    #     while j < n and s[j] == s[i]:
    #         j += 1
    #     add_seg(i, j - 1)
    #     i = j
    #
    # ans = []
    #
    # for pos, ch in zip(queryIndices, queryCharacters):
    #     if s[pos] == ch:
    #         ans.append(lens[-1])
    #         continue
    #
    #     # 删掉 pos 所在旧段
    #     idx = segs.bisect_right((pos, n)) - 1
    #     L, R = pop_seg(idx)
    #
    #     # 旧段拆成左右两部分
    #     if L <= pos - 1:
    #         add_seg(L, pos - 1)
    #     if pos + 1 <= R:
    #         add_seg(pos + 1, R)
    #
    #     # 新字符先单独成段
    #     newL = newR = pos
    #
    #     # 合并右边相邻段
    #     if pos + 1 < n and s[pos + 1] == ch:
    #         idx = segs.bisect_left((pos + 1, -1))
    #         _, newR = pop_seg(idx)
    #
    #     # 合并左边相邻段
    #     if pos > 0 and s[pos - 1] == ch:
    #         idx = segs.bisect_left((pos, -1)) - 1
    #         newL, _ = pop_seg(idx)
    #
    #     add_seg(newL, newR)
    #     s[pos] = ch
    #     ans.append(lens[-1])
    #
    # return ans


    # n = len(s)
    # s = list(s)
    # segs = SortedList()
    # lens = SortedList()
    #
    # i = 0
    # while i < n:
    #     j = i
    #     while j < n and s[j] == s[i]:
    #         j += 1
    #     segs.add((i, j - 1))
    #     lens.add(j - i)
    #     i = j
    #
    # k = len(queryIndices)
    # ans = []
    #
    # for q in range(k):
    #     pos = queryIndices[q]
    #     ch = queryCharacters[q]
    #
    #     if s[pos] != ch:
    #         idx = segs.bisect_right((pos, n)) - 1
    #         L, R = segs[idx]
    #         segs.pop(idx)
    #         lens.remove(R - L + 1)
    #
    #         if L <= pos - 1:
    #             segs.add((L, pos - 1))
    #             lens.add(pos - L)
    #         if pos + 1 <= R:
    #             segs.add((pos + 1, R))
    #             lens.add(R - pos)
    #
    #         newL, newR = pos, pos
    #
    #         if pos + 1 < n and s[pos + 1] == ch:
    #             idx2 = segs.bisect_left((pos + 1, -1))
    #             if idx2 < len(segs) and segs[idx2][0] == pos + 1:
    #                 rightL, rightR = segs[idx2]
    #                 lens.remove(rightR - rightL + 1)
    #                 newR = rightR
    #                 segs.pop(idx2)
    #
    #         if pos > 0 and s[pos - 1] == ch:
    #             idx3 = segs.bisect_right((pos - 1, n)) - 1
    #             if idx3 >= 0 and segs[idx3][1] == pos - 1:
    #                 leftL, leftR = segs[idx3]
    #                 lens.remove(leftR - leftL + 1)
    #                 newL = leftL
    #                 segs.pop(idx3)
    #
    #         segs.add((newL, newR))
    #         lens.add(newR - newL + 1)
    #         s[pos] = ch
    #
    #     ans.append(lens[-1])
    #
    # return ans


# 解法二
class SegmentTree:
    def __init__(self, s: list[str]):
        self._n = n = len(s)
        self._s = s
        self._tree = [None] * (2 << (n - 1).bit_length())
        self._build(s, 1, 0, n - 1)

    def _node_info(self, node: int, l: int, m: int, r: int):
        a_mx, a_pre, a_suf = self._tree[node * 2]
        b_mx, b_pre, b_suf = self._tree[node * 2 + 1]
        same = self._s[m] == self._s[m + 1]
        self._tree[node] = (
            max(a_mx, b_mx, a_suf + b_pre) if same else max(a_mx, b_mx),
            a_pre + b_pre if same and a_pre == m - l + 1 else a_pre,
            a_suf + b_suf if same and b_suf == r - m else b_suf
        )

    def _build(self, s: list[str], node: int, l: int, r: int):
        if l == r:
            self._tree[node] = (1, 1, 1)
            return
        m = (l + r) // 2
        self._build(s, node * 2, l, m)
        self._build(s, node * 2 + 1, m + 1, r)
        self._node_info(node, l, m, r)

    def _update(self, node: int, l: int, r: int, i: int, val: str):
        if l == r:
            self._s[i] = val
            return
        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, val)
        else:
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._node_info(node, l, m, r)

    def update(self, i: int, val: str):
        self._update(1, 0, self._n - 1, i, val)

    def query_all(self):
        return self._tree[1][0]


def longestRepeating2(s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    t = SegmentTree(list(s))
    ans = []
    for i, ch in zip(queryIndices, queryCharacters):
        t.update(i, ch)
        ans.append(t.query_all())
    return ans








