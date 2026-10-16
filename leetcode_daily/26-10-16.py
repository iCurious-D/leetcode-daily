""" 2916. 子数组不同元素数目的平方和 II  困难
给你一个下标从 0 开始的整数数组 nums 。
定义 nums 一个子数组的 不同计数 值如下：
令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），
那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。
请你返回 nums 中所有子数组的 不同计数 的 平方 和。
子数组指的是一个数组里面一段连续 非空 的元素序列。由于答案可能会很大，请你将它对 109 + 7 取余 后返回。

示例 1：输入：nums = [1,2,1];     输出：15
解释：六个子数组分别为：[1]: 1 个互不相同的元素。[2]: 1 个互不相同的元素。[1]: 1 个互不相同的元素。
[1,2]: 2 个互不相同的元素。[2,1]: 2 个互不相同的元素。[1,2,1]: 2 个互不相同的元素。
所有不同计数的平方和为 12 + 12 + 12 + 22 + 22 + 22 = 15 。
示例 2：输入：nums = [2,2];       输出：3
解释：三个子数组分别为：[2]: 1 个互不相同的元素。[2]: 1 个互不相同的元素。
[2,2]: 1 个互不相同的元素。所有不同计数的平方和为 12 + 12 + 12 = 3 。

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

"""
from collections import defaultdict
from typing import List


def sumCounts(nums: List[int]) -> int:
    MOD = 10 ** 9 + 7
    n = len(nums)

    # # 暴力法-挂
    # cnt = [0] * n  # cnt[j] = 子数组 [j..i] 的不同计数
    # last = {}  # 值 -> 上次出现的下标
    # ans = 0
    # for i, v in enumerate(nums):
    #     p = last.get(v, -1)
    #     for j in range(p + 1, i + 1):  # 区间加 1：一个一个改
    #         cnt[j] += 1
    #     ans = (ans + sum(c * c for c in cnt[:i + 1])) % MOD  # 重扫一遍算平方和
    #     last[v] = i
    # return ans

    sumv = [0] * (4 * n)    # 节点区间内 cnt 之和
    sqv = [0] * (4 * n)     # 节点区间内 cnt² 之和
    lazy = [0] * (4 * n)    # 懒标记：整段被加了几次、还没转告孩子

    def apply(o: int, length: int, x: int) -> None:
        # 整段每个数 c 变 c+x：
        # 平方和增量 Σ((c+x)²-c²) = 2x·Σc + x²·length
        # 注意：必须先用旧的 sumv 算 sqv，再更新 sumv，顺序不能反
        sqv[o] += 2 * x * sumv[o] + x * x * length
        sumv[o] += x * length
        lazy[o] += x                    # 账记在自己头上

    def push(o: int, length: int) -> None:
        # 孩子要单独改，先把欠下的旧账分给他们
        if lazy[o]:
            x = lazy[o]
            left_len = (length + 1) // 2
            apply(o << 1, left_len, x)
            apply(o << 1 | 1, length - left_len, x)
            lazy[o] = 0                 # 账已转出，清零

    def update(o: int, l: int, r: int, ql: int, qr: int) -> None:
        # 对 [ql, qr] 整体加 1，o 负责 [l, r]
        if ql <= l and r <= qr:         # 整段被覆盖：懒，apply 就收工
            apply(o, r - l + 1, 1)
            return
        push(o, r - l + 1)              # 半覆盖：先清旧账，孩子值才准
        mid = (l + r) >> 1
        if ql <= mid:                   # 左孩子有交集
            update(o << 1, l, mid, ql, qr)
        if qr > mid:                    # 右孩子有交集
            update(o << 1 | 1, mid + 1, r, ql, qr)
        sumv[o] = sumv[o << 1] + sumv[o << 1 | 1]   # 孩子改了，父亲重算
        sqv[o] = sqv[o << 1] + sqv[o << 1 | 1]

    last = {}                           # 值 -> 上次出现的下标
    ans = 0
    for i, v in enumerate(nums):
        p = last.get(v, -1)             # v 上次在哪？没有就是 -1
        # j > p 的子数组 [j..i] 里 v 是新面孔，cnt[j] 加 1
        update(1, 0, n - 1, p + 1, i)
        ans = (ans + sqv[1]) % MOD      # 根节点的 sqv = 全局 Σcnt²
        last[v] = i
    return ans


if __name__ == '__main__':
    print(sumCounts([1, 2, 1]))   # 15
    print(sumCounts([2, 2]))      # 3





