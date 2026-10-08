""" 3090. 每个字符最多出现两次的最长子字符串     简单
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。

示例 1：输入： s = "bcbbbcba";    输出： 4
解释：以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
示例 2：输入： s = "aaaa";    输出： 2
解释：以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。

提示：
2 <= s.length <= 100
s 仅由小写英文字母组成。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-08-14.md

"""
def maximumLengthSubstring(s: str) -> int:
    # cnt = {}
    # ans = left = 0
    # for right, c in enumerate(s):
    #     cnt[c] = cnt.get(c, 0) + 1
    #     while cnt[c] > 2:
    #         cnt[s[left]] -= 1
    #         left += 1
    #     ans = max(ans, right - left + 1)
    #
    # return ans

    cnt = [0] * 26
    ans = left = 0
    for right, c in enumerate(s):
        idx = ord(c)-ord('a')
        cnt[idx] += 1
        while cnt[idx] > 2:
            cnt[ord(s[left])-ord('a')] -= 1
            left += 1
        ans = max(ans, right-left+1)
    return ans


if __name__ == '__main__':
    print(maximumLengthSubstring("bcbbbcba"))
    print(maximumLengthSubstring("aaaa"))
    print(maximumLengthSubstring("abc"))












