""" 3120. 统计特殊字母的数量 I
给你一个字符串 word。如果 word 中同时存在某个字母的小写形式和大写形式，则称这个字母为 特殊字母 。
返回 word 中 特殊字母 的数量。

示例 1: 输入：word = "aaAbcBC"  输出：3
解释：word 中的特殊字母是 'a'、'b' 和 'c'。

示例 2: 输入：word = "abc"  输出：0
解释：word 中不存在大小写形式同时出现的字母。

示例 3:  输入：word = "abBCab"  输出：1
解释：word 中唯一的特殊字母是 'b'。

提示：
1 <= word.length <= 50
word 仅由小写和大写英文字母组成。
====================================================================

解路径：. / leetcode_daily_stories / 26-05-26.md



"""
import string


class Solution:
    def numofSpecialChars(self, word: str) -> int:
        # s = set(word)
        # return sum(c in s and c.upper() in s for c in string.ascii_lowercase)

        # lower = set()
        # upper = set()
        # for c in word:
        #     if c.islower():
        #         lower.add(c)
        #     else:
        #         upper.add(c.lower())
        # return len(lower & upper)

        mask = [0] * 2
        for c in map(ord, word):
            mask[c>>5 & 1] |= 1<<(c & 31)
        return (mask[0]&mask[1]).bit_count()


if __name__ == '__main__':
    print(Solution().numofSpecialChars(word="aaAbcBC"))
    print(Solution().numofSpecialChars(word="abc"))
    print(Solution().numofSpecialChars(word="abBCab"))
