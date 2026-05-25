"""  1345. 跳跃游戏 IV
给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j ：
i + 1 需满足：i + 1 < arr.length;  i - 1 需满足：i - 1 >= 0; j 需满足：arr[i] == arr[j] 且 i != j
请你返回**到达数组最后一个元素的下标处所需的 最少操作次数 **。  注意：任何时候你都不能跳到数组外面。

示例 1：输入：arr = [100,-23,-23,404,100,23,23,23,3,404]  输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

示例 2：输入：arr = [7]   输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。

示例 3：输入：arr = [7,6,9,6,9,6,9,7]   输出：1
解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

提示：
1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
"""
from typing import List
import collections


def minJumps(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0

    # 护法一：待办队列 (当前位置, 已走步数)
    queue = collections.deque([(0, 0)])
    # 护法二：已踩黑名单
    seen = {0}
    # 护法三：传送门字典 值 -> 索引列表
    portal = collections.defaultdict(list)
    for i, val in enumerate(arr):
        portal[val].append(i)

    while queue:
        i, step = queue.popleft()
        # 情形一：已到终点
        if i == n - 1:
            return step

        # 情形二：三路齐出
        # 1) 向前一步
        # 2) 向后一步
        for j in (i + 1, i - 1):
            if 0 <= j < n and j not in seen:
                seen.add(j)
                queue.append((j, step + 1))
        # 3) 同值传送门，用完立刻销毁
        if arr[i] in portal:
            for j in portal[arr[i]]:
                if j not in seen:
                    seen.add(j)
                    queue.append((j, step + 1))
            # 关键优化：清空该值的传送网络，后续不再重复处理
            portal[arr[i]] = []

    return -1


if __name__ == '__main__':
    print(minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
    print(minJumps([7]))
    print(minJumps([7, 6, 9, 6, 9, 6, 9, 7]))
