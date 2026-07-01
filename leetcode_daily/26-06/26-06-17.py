""" 3614. 用特殊操作处理字符串 II
给你一个字符串 s，它由小写英文字母和特殊字符：'*'、'#' 和 '%' 组成。同时给你一个整数 k。
请根据以下规则从左到右处理 s 中每个字符，构造一个新的字符串 result：
    如果字符是 小写 英文字母，则将其添加到 result 中。
    字符 '*' 会 删除 result 中的最后一个字符（如果存在）。
    字符 '#' 会 复制 当前的 result 并 追加 到其自身后面。
    字符 '%' 会 反转 当前的 result。
返回最终字符串 result 中第 k 个字符（下标从 0 开始）。如果 k 超出 result 的下标索引范围，则返回 '.'。

示例 1：输入： s = "a#b%*", k = 1； 输出： "a"
解释：
i	s[i]	操作	当前 result
0	'a'	添加 'a'	"a"
1	'#'	复制 result	"aa"
2	'b'	添加 'b'	"aab"
3	'%'	反转 result	"baa"
4	'*'	删除最后一个字符	"ba"
最终的 result 是 "ba"。下标为 k = 1 的字符是 'a'。

示例 2：输入： s = "cd%#*#", k = 3； 输出： "d"
解释：
i	s[i]	操作	当前 result
0	'c'	添加 'c'	"c"
1	'd'	添加 'd'	"cd"
2	'%'	反转 result	"dc"
3	'#'	复制 result	"dcdc"
4	'*'	删除最后一个字符	"dcd"
5	'#'	复制 result	"dcddcd"
最终的 result 是 "dcddcd"。下标为 k = 3 的字符是 'd'。

示例 3：输入： s = "z*#", k = 0；输出： "."
解释：
i	s[i]	操作	当前 result
0	'z'	添加 'z'	"z"
1	'*'	删除最后一个字符	""
2	'#'	复制字符串	""
最终的 result 是 ""。由于下标 k = 0 越界，输出为 '.'。

提示:
1 <= s.length <= 10^5
s 只包含小写英文字母和特殊字符 '*'、'#' 和 '%'。
0 <= k <= 10^15
处理 s 后得到的 result 的长度不超过 10^15。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-17.md

"""
class Solution:
    # def processStr(self, s: str) -> str:
    #     result = []
    #     for c in s:
    #         if c == '*':
    #             if result:
    #                 result.pop()
    #         elif c == '#':
    #             result += result
    #         elif c == '%':
    #             result.reverse()
    #         else:
    #             result.append(c)
    #     return ''.join(result)

    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        sz = 0
        for c in s:
            if c == '*':
                sz = max(sz - 1, 0)
            elif c == '#':
                sz *= 2
            elif c != '%':
                sz += 1

        if k >= sz:
            return '.'

        for c in reversed(s):
            if c == '*':
                sz += 1
            elif c == '#':
                sz //= 2
                if k >= sz:
                    k -= sz
            elif c == '%':
                k = sz - 1 - k
            else:
                sz -= 1
                if k == sz:
                    return c

        return '.'

        # n = len(s)
        #
        # size = [0] * n
        # for i, c in enumerate(s):
        #     if c.isalpha():
        #         size[i] = (size[i - 1] if i > 0 else 0) + 1
        #     elif c == '*':
        #         size[i] = max(0, (size[i - 1] if i > 0 else 0) - 1)
        #     elif c == '#':
        #         size[i] = (size[i - 1] if i > 0 else 0) * 2
        #     else:
        #         size[i] = size[i - 1] if i > 0 else 0
        #
        # if k >= size[-1]:
        #     return '.'
        #
        # for i in range(n - 1, -1, -1):
        #     c = s[i]
        #     if c.isalpha():
        #         if k == size[i]-1:
        #             return c
        #     elif c == '*':
        #         continue
        #     elif c == '#':
        #         m = size[i] // 2
        #         if k >= m:
        #             k -= m
        #     else:
        #         k = size[i] - 1 - k
        #
        # return '.'


if __name__ == '__main__':
    print(Solution().processStr("a#b%*", 1))
    print(Solution().processStr("cd%#*#", 3))
    print(Solution().processStr("z*#", 0))






