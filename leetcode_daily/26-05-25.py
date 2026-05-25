""" 1871. 跳跃游戏 VII
给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。
当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：
i + minJump <= j <= min(i + maxJump, s.length - 1) 且  s[j] == '0'.
如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。

示例 1：输入：s = "011010", minJump = 2, maxJump = 3  输出：true
解释：第一步，从下标 0 移动到下标 3 。第二步，从下标 3 移动到下标 5 。

示例 2：输入：s = "01101110", minJump = 2, maxJump = 3  输出：false

提示：
2 <= s.length <= 105
s[i] 要么是 '0' ，要么是 '1'
s[0] == '0'
1 <= minJump <= maxJump < s.length
==========================================================================================

题解路径：. / leetcode_daily_stories / 26-05-25.md

"""
from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # # 超时
        # n = len(s)
        # if s[-1] == "1":
        #     return False
        #
        # queue = deque({0})
        # seen = {0}
        # while queue:
        #     i = queue.popleft()
        #     if i == n - 1:
        #         return True
        #     start = i + minJump
        #     end = min(i + maxJump, n - 1)
        #     for j in range(start, end + 1):
        #         if s[j] == "0" and j not in seen:
        #             queue.append(j)
        #             seen.add(j)
        # return False
        # ======================================
        # n = len(s)
        # if s[-1] == "1":
        #     return False
        #
        # queue = deque({0})
        # far = 0
        # # seen = {0}
        # while queue:
        #     i = queue.popleft()
        #     if i == n - 1:
        #         return True
        #     # start = i + minJump
        #     start = max(i+minJump, far+1)
        #     end = min(i + maxJump, n - 1)
        #     for j in range(start, end + 1):
        #         if s[j] == "0":
        #             queue.append(j)
        #             if j==n-1:
        #                 return True
        #     far = max(far, end)
        #         # if s[j] == "0" and j not in seen:
        #         #     queue.append(j)
        #         #     seen.add(j)
        # return False
        # ===============================
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True
        # pre[i] 表示 dp[0..i-1] 中 True 的个数
        pre = [0] * (n + 1)
        pre[1] = 1  # dp[0] 是 True

        for i in range(1, n):
            # 1. 区间 [i-maxJump, i-minJump] 内是否有可达点
            dp[i] = (i >= minJump and s[i] == '0' and
                     pre[i - minJump + 1] > pre[max(i - maxJump, 0)])
            # 2. 更新前缀和
            pre[i + 1] = pre[i] + dp[i]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().canReach("011010", 2, 3))
    print(Solution().canReach("01101110", 2, 3))
    print(Solution().canReach("01101110", 1, 2))


















