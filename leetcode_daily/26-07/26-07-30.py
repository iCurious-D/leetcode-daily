""" 3014. 输入单词需要的最少按键次数 I   简单
给你一个字符串 word，由 不同 小写英文字母组成。
电话键盘上的按键与 不同 小写英文字母集合相映射，可以通过按压按键来组成单词。
例如，按键 2 对应 ["a","b","c"]，我们需要按一次键来输入 "a"，按两次键来输入 "b"，按三次键来输入 "c"。
现在允许你将编号为 2 到 9 的按键重新映射到 不同 字母集合。
每个按键可以映射到 任意数量 的字母，但每个字母 必须 恰好 映射到 一个 按键上。
你需要找到输入字符串 word 所需的 最少 按键次数。
返回重新映射按键后输入 word 所需的 最少 按键次数。

示例 1：输入：word = "abcde";     输出：5
解释：图片中给出的重新映射方案的输入成本最小。总成本为 1 + 1 + 1 + 1 + 1 = 5 。可以证明不存在其他成本更低的映射方案。
示例 2：输入：word = "xycdefghij";    输出：12
解释：图片中给出的重新映射方案的输入成本最小。总成本为 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12 。
可以证明不存在其他成本更低的映射方案。

提示：
1 <= word.length <= 26
word 仅由小写英文字母组成。
word 中的所有字母互不相同。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-07-30.md

"""
def minimumPushes(word: str) -> int:
    # n = len(word)
    # if n <= 8:
    #     return n
    # elif n <= 16:
    #     return 8 + (n-8)*2
    # elif n <= 24:
    #     return 8 + 16 + (n-16)*3
    # return 8 + 16 + 24 + (n-24)*4

    # return sum(i//8 + 1 for i in range(len(word)))

    k, rem = divmod(len(word), 8)
    return (4*k + rem) * (k + 1)




if __name__ == '__main__':
    print(minimumPushes("abcde"))
    print(minimumPushes("xycdefghij"))
    print(minimumPushes("abcdefghijklmnopqrstuvwxyz"))




