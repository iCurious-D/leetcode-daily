""" 1358. 包含所有三种字符的子字符串数目   中等
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

示例 1：输入：s = "abcabc";   输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。

示例 2：输入：s = "aaacb";    输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。

示例 3：输入：s = "abc";  输出：1

提示：
3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-30.md

"""
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # # 解法一：枚举+二分
        # n = len(s)
        # ans = 0
        # pre = [[0] * (n+1) for _ in range(3)]
        # for i in range(n):
        #     for j in range(3):
        #         pre[j][i+1] = pre[j][i]
        #     pre[ord(s[i])-ord('a')][i+1] += 1
        # for i in range(n):
        #     left, right = i+1, n
        #     pos = -1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if (pre[0][mid] - pre[0][i] >= 1 and
        #             pre[1][mid] - pre[1][i] >= 1 and
        #             pre[2][mid] - pre[2][i] >= 1):
        #             right = mid - 1
        #             pos = mid
        #         else:
        #             left = mid + 1
        #     if pos != -1:
        #         ans += n - pos + 1
        # return ans

        # # 解法二：双指针+滑动窗口
        # n = len(s)
        # ans = 0
        # cnt = [0, 0, 0]
        # l, r = 0, -1
        # while l < n:
        #     while r < n and not (cnt[0] and cnt[1] and cnt[2]):
        #         r += 1
        #         if r == n:
        #             break
        #         cnt[ord(s[r]) - ord('a')] += 1
        #     if r < n:
        #         ans += n - r
        #     cnt[ord(s[l]) - ord('a')] -= 1
        #     l += 1
        # return ans

        # 解法三：滑动窗口
        cnt = defaultdict(int)
        ans = left = 0
        for c in s:
            cnt[c] += 1
            while len(cnt) == 3:
                out = s[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    print(Solution().numberOfSubstrings("abcabc"))
    print(Solution().numberOfSubstrings("aaacb"))
    print(Solution().numberOfSubstrings("abc"))
