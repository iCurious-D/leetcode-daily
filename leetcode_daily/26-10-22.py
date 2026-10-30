""" 3942. 排序排列的最少操作数    中等
给你一个长度为 n 的整数数组 nums，其中 nums 是区间 [0..n - 1] 中所有数字的一个排列。
你 只能 执行以下操作：
反转 整个数组。
左旋一位：将第一个元素移动到数组末尾，其余元素整体向左移动一位。
返回将数组按 递增 顺序排序所需的 最少 操作次数。如果仅使用给定操作无法将数组排序，则返回 -1。
排列 是数组中所有元素的一种重新排列。

示例 1：输入： nums = [0,2,1];    输出： 2
解释：左旋一位：[2, 1, 0]; 反转数组：[0, 1, 2]; 数组在 2 次操作后变为有序，这是最少操作次数。
示例 2：输入： nums = [1,0,2];    输出： 2
解释：反转数组：[2, 0, 1]; 左旋一位：[0, 1, 2]
数组在 2 次操作后变为有序，这是最少操作次数。
示例 3：输入： nums = [2,0,1,3];  输出： -1
解释：无法将该数组变为 [0, 1, 2, 3]。因此答案为 -1。

提示：
1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums 是从 0 到 n - 1 的整数排列。

"""
from typing import List

def minOperations(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:  # 模 1 恒为 0，判定失效
        return 0

    prev = nums[-1]  # 环形前驱：最后一对是 (nums[-1], nums[0])
    fwd = bwd = True
    for x in nums:
        if fwd and not (x == prev + 1 or (prev == n - 1 and x == 0)):
            fwd = False  # 正向环：只允许 +1，和唯一一次 n-1 -> 0 回卷
        if bwd and not (x == prev - 1 or (prev == 0 and x == n - 1)):
            bwd = False  # 反向环：只允许 -1，和唯一一次 0 -> n-1 回卷
        if not fwd and not bwd:
            return -1  # 两个方向都判死刑，提前收工
        prev = x

    if fwd:
        p = nums.index(0)  # 0 的位置就是需要的左旋次数
        return min(p, n - p + 2)  # 或走 R L^{n-p} R，代价 n-p+2
    q = nums.index(n - 1)  # n-1 的位置：转 q 次得降序，再整体反转
    return 1 + min(q, n - q)  # L^q R 与 R L^{n-q} 取更短的那个


if __name__ == '__main__':
    print(minOperations([0,2,1]))
    print(minOperations([1,0,2]))
    print(minOperations([2,0,1,3]))









