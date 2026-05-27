""" 3121. 统计特殊字母的数量 II
给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，
并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。
返回 word 中 特殊字母 的数量。

示例 1:输入：word = "aaAbcBC"  输出：3
解释：特殊字母是 'a'、'b' 和 'c'。

示例 2:输入：word = "abc"  输出：0
解释：word 中不存在特殊字母。

示例 3: 输入：word = "AbBCab"  输出：0
解释：word 中不存在特殊字母。

提示：
1 <= word.length <= 2 * 105
word 仅由小写和大写英文字母组成。
========================================================

解路径：. / leetcode_daily_stories / 26-05-27.md


"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # last_lower = {}
        # first_upper = {}
        #
        # for i, c in enumerate(word):
        #     if c.islower():
        #         last_lower[c] = i  # 不断更新，保留最后一次
        #     else:
        #         if c not in first_upper:  # 只记录第一次
        #             first_upper[c] = i
        # cnt = 0
        # for c in "abcdefghijklmnopqrstuvwxyz":
        #     if c in last_lower and c.upper() in first_upper and last_lower[c] < first_upper[c.upper()]:
        #         cnt += 1
        # return cnt
        #
        # lower = set()
        # upper = set()
        # invalid = set()  # 非法字母集合（大写后面又出现小写的字母）
        # for c in word:
        #     if c.islower():  # 小写字母
        #         lower.add(c)
        #         if c in upper:  # 大写的后面不能有小写
        #             invalid.add(c)  # 标记为非法！
        #     else:  # 大写字母
        #         upper.add(c.lower())
        # # 从 lower 和 upper 的交集中去掉不合法的字母 invalid
        # return len((lower & upper) - invalid)
        #
        # lower = upper = invalid = 0  # 三个整数，代替三个集合
        # for c in map(ord, word):
        #     bit = 1 << (c & 31)  # 计算该字母对应的位掩码
        #     if c & 32:  # 小写字母
        #         lower |= bit
        #         if upper & bit:  # c 也在 upper 中
        #             invalid |= bit  # 标记为非法
        #     else:  # 大写字母
        #         upper |= bit
        # # 从 lower 和 upper 的交集中去掉不合法的字母 invalid
        # return (lower & upper & ~invalid).bit_count()

        ans = 0
        state = [0] * 27  # 26个字母的状态数组，索引1-26，索引0闲置
        for c in map(ord, word):
            x = c & 31  # 提取字母编号（1-26）
            if c & 32:  # 小写字母
                if state[x] == 0:    # 状态0：第一次见到该字母（小写）
                    state[x] = 1     # 转为状态1：已见小写，还没见大写
                elif state[x] == 2:  # 状态2：之前已成功配对
                    state[x] = -1    # 转为状态-1：配对后又见小写，非法！
                    ans -= 1         # 答案减1
            else:  # 大写字母
                if state[x] == 0:    # 状态0：第一次见到该字母（大写）
                    state[x] = -1    # 转为状态-1：直接非法（没见小写就见大写）
                elif state[x] == 1:  # 状态1：之前见过小写
                    state[x] = 2     # 转为状态2：完整配对成功！
                    ans += 1         # 答案加1
        return ans


if __name__ == '__main__':
    print(Solution().numberOfSpecialChars(word = "aaAbcBC"))
    print(Solution().numberOfSpecialChars(word = "abc"))
    print(Solution().numberOfSpecialChars(word = "AbBCab"))


