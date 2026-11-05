""" 3505. 使 K 个子数组内元素相等的最少操作数   困难
给你一个整数数组 nums 和两个整数 x 和 k。你可以执行以下操作任意次（包括零次）：
将 nums 中的任意一个元素加 1 或减 1。
返回为了使 nums 中 至少 包含 k 个长度 恰好 为 x 的不重叠子数组（每个子数组中的所有元素都相等）所需要的 最少 操作数。
子数组 是数组中连续、非空的一段元素。

示例 1：输入： nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2;    输出： 8
解释：进行 3 次操作，将 nums[1] 加 3；进行 2 次操作，将 nums[3] 减 2。得到的数组为 [5, 1, 1, 1, 7, 3, 6, 4, -1]。
进行 1 次操作，将 nums[5] 加 1；进行 2 次操作，将 nums[6] 减 2。得到的数组为 [5, 1, 1, 1, 7, 4, 4, 4, -1]。
现在，子数组 [1, 1, 1]（下标 1 到 3）和 [4, 4, 4]（下标 5 到 7）中的所有元素都相等。总共进行了 8 次操作，因此输出为 8。
示例 2：输入： nums = [9,-2,-2,-2,1,5], x = 2, k = 2;     输出： 3
解释：进行 3 次操作，将 nums[4] 减 3。得到的数组为 [9, -2, -2, -2, -2, 5]。
现在，子数组 [-2, -2]（下标 1 到 2）和 [-2, -2]（下标 3 到 4）中的所有元素都相等。总共进行了 3 次操作，因此输出为 3。

提示：
2 <= nums.length <= 10^5
-10^6 <= nums[i] <= 10^6
2 <= x <= nums.length
1 <= k <= 15
2 <= k * x <= nums.length

"""
from collections import defaultdict
import heapq
from math import inf
from typing import List


class LazyHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        self.heap_sum = 0
        self.remove_cnt = defaultdict(int)

    def remove(self, num):
        self.remove_cnt[num] += 1
        self.size -= 1
        self.heap_sum -= num

    def apply_remove(self):
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heapq.heappop(self.heap)

    def top(self):
        self.apply_remove()
        return self.heap[0]

    def push(self, num):
        if self.remove_cnt[num] > 0:
            self.remove_cnt[num] -= 1
        else:
            heapq.heappush(self.heap, num)
        self.size += 1
        self.heap_sum += num

    def pop(self):
        self.apply_remove()
        self.size -= 1
        self.heap_sum -= self.heap[0]
        return heapq.heappop(self.heap)

    def pushpop(self, num):
        self.apply_remove()
        if not self.heap or num <= self.heap[0]:
            return num
        self.heap_sum += num - self.heap[0]
        return heapq.heappushpop(self.heap, num)

def medianSlidingWindow(nums: List[int], k: int) -> List[int]:
    left = LazyHeap()
    right = LazyHeap()

    ans = [0] * (len(nums) - k + 1)
    for i, x in enumerate(nums):
        if left.size == right.size:
            left.push(-right.pushpop(x))
        else:
            right.push(-left.pushpop(-x))

        l = i - k + 1
        if l < 0:
            continue

        v = -left.top()
        s1 = v * left.size + left.heap_sum
        s2 = right.heap_sum - v * right.size
        ans[l] = s1 + s2

        num = nums[l]
        if num <= -left.top():
            left.remove(-num)
            if left.size < right.size:
                left.push(-right.pop())
        else:
            right.remove(num)
            if right.size + 1 < left.size:
                right.push(-left.pop())

    return ans


def minOperations(nums: List[int], x: int, k: int) -> int:
    n = len(nums)
    dis = medianSlidingWindow(nums, x)
    dp = [[0] * (n+1) for _ in range(k+1)]
    for i in range(1, k+1):
        dp[i][i*x-1] = inf
        for j in range(i*x, n - (k-i)*x + 1):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-x] + dis[j-x])

    return dp[k][n]


if __name__ == '__main__':
    print(minOperations([5,-2,1,3,7,3,6,4,-1], 3, 2))
    print(minOperations([9,-2,-2,-2,1,5], 2, 2))
    print(minOperations([1,2,3,4,5,6,7,8,9,10], 5, 2))








