""" 3420. 统计 K 次操作以内得到非递减子数组的数目 困难
给你一个长度为 n 的数组 nums 和一个整数 k 。
对于 nums 中的每一个子数组，你可以对它进行 至多 k 次操作。每次操作中，你可以将子数组中的任意一个元素增加 1 。
注意 ，每个子数组都是独立的，也就是说你对一个子数组的修改不会保留到另一个子数组中。
请你返回最多 k 次操作以内，有多少个子数组可以变成 非递减 的。
如果一个数组中的每一个元素都大于等于前一个元素（如果前一个元素存在），那么我们称这个数组是 非递减 的。

示例 1：输入：nums = [6,3,1,2,4,4], k = 7;    输出：17
解释：nums 的所有 21 个子数组中，只有子数组 [6, 3, 1] ，[6, 3, 1, 2] ，[6, 3, 1, 2, 4] 和 [6, 3, 1, 2, 4, 4] 无法在 k = 7 次操作以内变为非递减的。所以非递减子数组的数目为 21 - 4 = 17 。
示例 2：输入：nums = [6,3,1,3,6], k = 4;      输出：12
解释：
子数组 [3, 1, 3, 6] 和 nums 中所有小于等于三个元素的子数组中，除了 [6, 3, 1] 以外，都可以在 k 次操作以内变为非递减子数组。总共有 5 个包含单个元素的子数组，4 个包含两个元素的子数组，除 [6, 3, 1] 以外有 2 个包含三个元素的子数组，所以总共有 1 + 5 + 4 + 2 = 12 个子数组可以变为非递减的。

提示：1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9

"""
from typing import List
from collections import deque

def countNonDecreasingSubarrays(nums, k):
    n = len(nums)
    # nxt[i]：i 右侧第一个严格大于 nums[i] 的下标，不存在则为 n
    nxt = [n] * n
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            nxt[st.pop()] = i
        st.append(i)
    # 前缀和：O(1) 算出一段的垫高代价 = 段长 * 段最大值 - 段和
    pre = [0] * (n + 1)
    for i, x in enumerate(nums):
        pre[i + 1] = pre[i] + x

    ans = 0
    l = 0
    cost = 0
    last = 0  # 窗口内最后一个记录点（即窗口最大值的位置）
    for r, x in enumerate(nums):
        if x > nums[last]:
            last = r  # x 刷新纪录，自成一段，代价 +0
        else:
            cost += nums[last] - x  # x 并入最后一段，垫到 nums[last]
        while cost > k:
            # 左端点 l 必是第一个记录点，它管辖 [l, p-1]
            p = min(nxt[l], r + 1)
            cost -= nums[l] * (p - l) - (pre[p] - pre[l])
            # 删掉 l 后，段内沿 nxt 链诞生新记录点，逐段补回贡献
            # 每个元素一生只晋升一次，均摊 O(n)
            t = l + 1
            new_last = l
            while t < p:
                e = min(nxt[t], p)
                cost += nums[t] * (e - t) - (pre[e] - pre[t])
                new_last = t
                t = nxt[t]
            if l == last:
                last = new_last  # 整窗只有一段时，末记录点随之更新
            l += 1
        ans += r - l + 1  # 合法左端点是 [l, r]，共 r-l+1 个
    return ans


if __name__ == '__main__':
    print(countNonDecreasingSubarrays([6,3,1,2,4,4], 7))
    print(countNonDecreasingSubarrays([6,3,1,3,6], 4))
    print(countNonDecreasingSubarrays([1,2,3,4,5], 10))



