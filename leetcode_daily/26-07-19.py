""" 1081. 不同字符的最小子序列    中等
返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。

示例 1：输入：s = "bcabc"     输出："abc"
示例 2：输入：s = "cbacdcbc"      输出："acdb"

提示：
1 <= s.length <= 1000
s 由小写英文字母组成
注意：该题与 316相同
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-19.md

"""
from collections import Counter


def smallestSubsequence(s: str) -> str:
    cnt = Counter(s)
    ans_stack = []
    ans_set = set()
    for c in s:
        cnt[c] -= 1
        if c in ans_stack:
            continue
        while ans_stack and ans_stack[-1]>c and cnt[ans_stack[-1]]:
            ans_set.remove(ans_stack.pop())
        ans_stack.append(c)
        ans_set.add(c)

    return "".join(ans_stack)


if __name__ == '__main__':
    print(smallestSubsequence(s = "bcabc"))
    print(smallestSubsequence(s = "cbacdcbc"))
    print(smallestSubsequence(s = "ecbafed"))

