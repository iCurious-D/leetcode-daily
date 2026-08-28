""" 3734. 大于目标字符串的最小字典序回文排列     困难
给你两个长度均为 n 的字符串 s 和目标字符串 target，它们都由小写英文字母组成。
返回 字典序 最小的字符串 ，该字符串 既 是 s 的一个 回文 排列 ，又是字典序 严格 大于 target 的。
如果不存在这样的排列，则返回一个空字符串。
如果字符串 a 和字符串 b 长度相同，在它们首次出现不同的位置上，字符串 a 处的字母在字母表中的顺序晚于字符串 b 处的对应字母，则字符串 a 在 字典序上严格大于 字符串 b。
排列 是指对字符串中所有字符的重新排列。
如果一个字符串从前向后读和从后向前读都一样，则该字符串是 回文 的。

示例 1：输入：s = "baba", target = "abba";    输出："baab"
解释：s 的回文排列（按字典序）是 "abba" 和 "baab"。字典序最小的、且严格大于 target 的排列是 "baab"。
示例 2：输入：s = "baba", target = "bbaa";     输出：""
解释：s 的回文排列（按字典序）是 "abba" 和 "baab"。它们中没有一个在字典序上严格大于 target。因此，答案是 ""。
示例 3：输入：s = "abc", target = "abb";   输出：""
解释：s 没有回文排列。因此，答案是 ""。
示例 4：输入：s = "aac", target = "abb";   输出："aca"
解释:s 唯一的回文排列是 "aca"。"aca" 在字典序上严格大于 target。因此，答案是 "aca"。

提示:
1 <= n == s.length == target.length <= 300
s 和 target 仅由小写英文字母组成。

"""
from collections import Counter


def lexPalindromicPermutation(s: str, target: str) -> str:
    n = len(s)
    cnt = Counter(s)

    # 1. 检查是否能构成回文串：单个字符最多只有一个，而且必须放中间
    odd = [ch for ch in cnt if cnt[ch] % 2 == 1]
    if len(odd) > 1:
        return ""
    mid = odd[0] if odd else ""

    # 2. 看左半边，右半边是镜像
    half = n // 2
    rem = Counter({ch: c // 2 for ch, c in cnt.items()})
    t = target[:half]

    # 3.1 先尝试最小字符串
    lowest = "".join(sorted(rem.elements()))
    if lowest > t:
        return lowest + mid + lowest[::-1]

    # 3.2 如果rem和t的字符组成相同（rem能拼出t）：考察中间/右边
    if Counter(t) == rem:
        if n % 2:
            if mid > target[half] or (mid == target[half] and t[::-1] > target[half+1:]):
                return t + mid + t[::-1]
        elif t[::-1] > target[half:]:
            return t + t[::-1]

    # 3.3 如果上述都不成立，找下一个排列——从右往左找第一个能抬高的位置
    for i in range(half-1, -1, -1):
        needed = Counter(t[:i])
        if any(needed[ch] > rem[ch] for ch in needed):
            continue
        for code in range(ord(t[i])+1, ord('z')+1):
            ch = chr(code)
            if rem[ch] > needed[ch]:
                rest = rem - needed
                rest[ch] -= 1
                R = t[:i] + ch + "".join(sorted(rest.elements()))
                return R + mid + R[::-1]

    return ""


if __name__ == '__main__':
    print(lexPalindromicPermutation("baba", "abba"))
    print(lexPalindromicPermutation("baba", "bbaa"))
    print(lexPalindromicPermutation("abc", "abb"))
















