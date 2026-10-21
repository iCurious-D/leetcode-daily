""" 3886. 可排序整数求和   困难
给你一个长度为 n 的整数数组 nums。
如果一个整数 k 满足以下条件，则称其为 可排序整数：k 是 n 的 因数，且可以通过依次执行以下操作将 nums 排序为 非递减顺序：
将 nums 划分为长度为 k 的 连续子数组。独立地对每个子数组进行循环移动（左移或右移任意次数）。
返回所有可能的可排序整数 k 的和。
子数组 是数组中的一个连续、非空元素序列。

示例 1：输入： nums = [3,1,2];    输出： 3
解释：对于 n = 3，可能的因数是 1 和 3。
对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
对于 k = 3：单个子数组 [3, 1, 2] 可以通过左移一次得到 [1, 2, 3]，从而将数组排序。
只有 k = 3 可排序，因此答案是 3。
示例 2：输入： nums = [7,6,5];    输出： 0
解释：对于 n = 3，可能的因数是 1 和 3。
对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
对于 k = 3：单个子数组 [7, 6, 5] 无法通过任何移动排序为非递减顺序。
没有任何可排序的 k，因此答案是 0。
示例 3：输入： nums = [5,8];      输出： 3
解释：对于 n = 2，可能的因数是 1 和 2。由于 [5, 8] 本身已经有序，每个因数都可排序。因此答案是 1 + 2 = 3。

提示：
1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5

"""
from math import isqrt


def sumOfSortableIntegers(nums: list[int]) -> int:
    n = len(nums)
    next_dec = [0] * n  # nums[next_dec[i]] > nums[next_dec[i] + 1]
    next_dec[-1] = p = n
    # 对于每个 i，记录下一个递减的位置
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            p = i
        next_dec[i] = p

    def solve(k: int) -> None:
        last_max = 0  # 上一段的最大值
        for r in range(k - 1, n, k):
            l = r - k + 1
            m = next_dec[l]
            if m >= r:
                # [l, r] 是递增的，最小值为 nums[l]，最大值为 nums[r]
                # 最小值必须 >= 上一段的最大值
                if nums[l] < last_max:
                    return
                last_max = nums[r]
            else:
                # ：块内只能有一个断点，断点转到开头，然后检查「右半段自身有序 + 首元素 ≥ 上一块最大值 + 拼接缝不下降」这三处接缝。
                # [l, m] 是第一段，[m+1, r] 是第二段，旋转后为 第二段 + 第一段
                right_not_sorted = next_dec[m + 1] < r  # 右半段内部还有断点 → 块内 ≥2 个断点
                head_too_small = nums[m + 1] < last_max  # 旋转后首元素接不上上一块
                seam_descends = nums[r] > nums[l]  # 两段拼接处下降
                if right_not_sorted or head_too_small or seam_descends:
                    return
                last_max = nums[m]  # 旋转后块尾是 nums[m]，即本块最大值
        nonlocal ans
        ans += k  # 满足要求

    ans = 0
    # 枚举 n 的因子 k
    for k in range(1, isqrt(n) + 1):
        if n % k == 0:
            solve(k)
            if k * k < n:
                solve(n // k)
    return ans


if __name__ == '__main__':
    print(sumOfSortableIntegers([3, 1, 2]))
    print(sumOfSortableIntegers([7, 6, 5]))
    print(sumOfSortableIntegers([5, 8]))





