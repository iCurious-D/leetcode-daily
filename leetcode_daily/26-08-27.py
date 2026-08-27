""" 3720. 大于目标字符串的最小字典序排列       中等
给你两个长度均为 n 且仅由小写英文字母组成的字符串 s 和 target。
返回 s 的 字典序最小的排列，要求该排列 严格 大于 target。如果 s 不存在任何字典序严格大于 target 的排列，则返回一个空字符串。
如果两个长度相同的字符串 a 和 b 在它们首次出现不同字符的位置上，
字符串 a 对应的字母在字母表中出现在 b 对应字母的 后面 ，则字符串 a 字典序严格大于 字符串 b。
排列 是字符串中所有字符的一种重新排列。

示例 1:输入: s = "abc", target = "bba";     输出: "bca"
解释:s 的排列（按字典序）有 "abc", "acb", "bac", "bca", "cab" 和 "cba"。
字典序严格大于 target 的最小排列是 "bca"。
示例 2:输入: s = "leet", target = "code";   输出: "eelt"
解释:s 的排列（按字典序）有 "eelt" ，"eetl" ，"elet" ，"elte" ，"etel" ，"etle" ，"leet" ，"lete" ，"ltee" ，"teel" ，"tele" 和 "tlee"。
字典序严格大于 target 的最小排列是 "eelt"。
示例 3:输入: s = "baba", target = "bbaa";   输出: ""
解释:s 的排列（按字典序）有 "aabb" ，"abab" ，"abba" ，"baab" ，"baba" 和 "bbaa"。
其中没有一个排列的字典序严格大于 target。因此，答案是 ""。

提示:
1 <= s.length == target.length <= 300
s 和 target 仅由小写英文字母组成。

"""
from collections import Counter
from string import ascii_lowercase


def lexGreaterPermutation(s: str, target: str) -> str:
    # # 解法一：逐位贪心 + 回溯
    # n = len(s)
    # # 统计 s 中每个字符的可用次数
    # cnt = [0] * 26
    # for ch in s:
    #     cnt[ord(ch) - 97] += 1
    #
    # # path 记录当前已经选了哪些字符，相当于拼到一半的答案
    # ans = []
    #
    # # 辅助函数：把剩余字符按字典序升序拼起来
    # # 用在"已经赢了"的时候——某一位放了比 target 大的字符，后面随便最小化就行
    # def fill_remaining():
    #     res = []
    #     # 从 a 到 z 遍历，有几个就放几个，天然有序
    #     for c in range(26):
    #         if cnt[c] > 0:
    #             res.append(chr(c + 97) * cnt[c])
    #     return ''.join(res)
    #
    # # 回溯函数：当前要填第 i 位
    # def backtrack(i):
    #     # 所有位都填完了，说明恰好等于 target（每一位都打平），没有严格大于，返回空
    #     if i == n:
    #         return ""
    #
    #     # 从 a 到 z 枚举当前位可以放的字符（保证从小到大尝试，找到第一个合法的就是最优）
    #     for c in range(26):
    #         # 这个字符已经用光了，或者放这个字符会比 target[i] 小，那整个结果就会比 target 小，不合法，跳过
    #         if cnt[c] == 0 or c < ord(target[i]) - 97:
    #             continue
    #
    #         # 选了 ch，可用数量 -1，加入当前路径
    #         cnt[c] -= 1
    #         ans.append(chr(c + 97))
    #
    #         if c > ord(target[i]) - 97:
    #             # 情况一：ch > target[i]，这一位已经赢了！
    #             # 后面所有位不需要再跟 target 比较了，直接升序排列剩余字符就是最小答案
    #             return ''.join(ans) + fill_remaining()
    #         else:
    #             # 情况二：ch == target[i]，这一位打平，胜负未分，继续去填第 i+1 位
    #             res = backtrack(i + 1)
    #             if res != "":
    #                 # 后续位成功找到了一个排列 > target，直接返回
    #                 return res
    #             # 否则说明这一位选 ch（== target[i]）走不通，回溯，换更大的字符试试
    #
    #         # 撤销选择：字符数量恢复，path 弹出，进入下一轮循环尝试更大的字符
    #         ans.pop()
    #         cnt[c] += 1
    #
    #     # 26 个字母都试过了，没有能 >= target[i] 的，这一位无解，返回空触发上层回溯
    #     return ""
    #
    # # 从第 0 位开始填
    # return backtrack(0)

    # 解法二：倒序贪心
    n = len(s)
    # s 中每个字符的数量
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - 97] += 1

    # pre 当前表示 target 中尚未去掉的字符数
    # 循环中会先减掉 target[i]，使 pre 变成 target[0..i-1] 的计数
    pre = [0] * 26
    for ch in target:
        pre[ord(ch) - 97] += 1

    for i in range(n - 1, -1, -1):
        ti = ord(target[i]) - 97

        # 现在 pre 是 target[0..i-1] 的字符计数
        pre[ti] -= 1

        # 前缀必须可以由 s 中的字符组成
        if any(pre[c] > cnt[c] for c in range(26)):
            continue

        # 找一个比 target[i] 大且还剩下的最小字符
        use = -1
        for c in range(ti + 1, 26):
            if cnt[c] - pre[c] > 0:
                use = c
                break

        if use == -1:
            continue

        # 构造答案
        ans = list(target[:i])
        ans.append(chr(use + 97))

        rem = [cnt[c] - pre[c] for c in range(26)]
        rem[use] -= 1

        for c in range(26):
            if rem[c] > 0:
                ans.extend(chr(c + 97) * rem[c])

        return ''.join(ans)

    return ""


    # 优化版
    # left = Counter(s)
    # for c in target:
    #     left[c] -= 1  # 消耗 s 中的一个字母 c
    #
    # # 从右往左尝试
    # for i in range(len(s) - 1, -1, -1):
    #     c = target[i]
    #     left[c] += 1  # 撤销消耗
    #     if any(cnt < 0 for cnt in left.values()):
    #         continue  # [0,i-1] 无法做到全部一样
    #
    #     # 把 target[i] 增大到 j
    #     for j in range(ord(c) - ord('a') + 1, 26):
    #         ch = ascii_lowercase[j]
    #         if left[ch] == 0:
    #             continue
    #
    #         # 找到答案（下面的循环在整个算法中只会跑一次）
    #         left[ch] -= 1
    #         ans = list(target[:i + 1])
    #         ans[i] = ch
    #
    #         # 中间可以随便填
    #         for ch in ascii_lowercase:
    #             ans.extend(ch * left[ch])
    #         return ''.join(ans)
    #     # 增大失败，继续枚举
    #
    # return ""



# 典型构造：
# 尽可能保留 target 前缀，
# 在某个位置 i 选择一个比 target[i] 大的字符（从 s 可用字符中选最小的可用的比 target[i] 大的字符），放在该位置，
# 然后剩余字符按升序排列，得到一个候选排列，字典序大于 target 且在该前缀后最小。
# 一般方法：
# 从右到左，尝试在位置 i 放置一个比 target[i] 大的可用字符，
# 并且剩余字符任意排序（最小升序）能形成长度正确的排列。
# 核心思路：
# 字典序比较。
# 假设答案是 ans，一定存在一个位置 i 使得 ans[0..i-1] == target[0..i-1]，ans[i] > target[i]。
# 为了让 ans 尽可能小，这个“首次变大”的位置 i 应该尽量靠右（即前缀保留得尽量长）。因此从右往左枚举 i。
# 对于每个 i，检查：
# target 的前 i 个字符是否能由 s 中的字符组成（字符计数不超）。
# 去掉这 i 个已用的字符后，是否还有一个可用字符 c > target[i]。
# 如果满足，选择最小的 c > target[i] 放在位置 i，其余字符升序放在后面，得到候选答案。因为 i 从右往左第一个可行，所以它是最小字典序。









