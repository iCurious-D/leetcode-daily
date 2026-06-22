""" 1189. “气球” 的最大数量    简单
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

示例 1：输入：text = "nlaebolko";     输出：1
示例 2：输入：text = "loonbalxballpoon";  输出：2
示例 3：输入：text = "leetcode";  输出：0

提示：
1 <= text.length <= 10^4
text 全部由小写英文字母组成
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-22.md

"""
from collections import Counter


class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     cnt = Counter(text)
    #     return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])

    def maxNumberOfBalloons(self, text: str, word: str) -> int:
        cnt_word = Counter(word)
        cnt_text = Counter(text)
        return min(cnt_text[char] // cnt_word[char] for char in word)


if __name__ == '__main__':
    print(Solution().maxNumberOfBalloons("nlaebolko", "balloon"))
    # print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
    # print(Solution().maxNumberOfBalloons("leetcode"))
