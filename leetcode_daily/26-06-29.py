""" 1967. 作为子字符串出现在单词中的字符串数目    简单
给你一个字符串数组 patterns 和一个字符串 word ，统计 patterns 中有多少个字符串是 word 的子字符串。返回字符串数目。
子字符串 是字符串中的一个连续字符序列。

示例 1：输入：patterns = ["a","abc","bc","d"], word = "abc";  输出：3
解释：
- "a" 是 "abc" 的子字符串。
- "abc" 是 "abc" 的子字符串。
- "bc" 是 "abc" 的子字符串。
- "d" 不是 "abc" 的子字符串。
patterns 中有 3 个字符串作为子字符串出现在 word 中。

示例 2：输入：patterns = ["a","b","c"], word = "aaaaabbbbb";  输出：2
解释：
- "a" 是 "aaaaabbbbb" 的子字符串。
- "b" 是 "aaaaabbbbb" 的子字符串。
- "c" 不是 "aaaaabbbbb" 的字符串。
patterns 中有 2 个字符串作为子字符串出现在 word 中。

示例 3：输入：patterns = ["a","a","a"], word = "ab";  输出：3
解释：patterns 中的每个字符串都作为子字符串出现在 word "ab" 中。

提示：
1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
patterns[i] 和 word 由小写英文字母组成
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-29.md

"""
from typing import List
from collections import deque

# 解法一
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         return sum(p in word for p in patterns)

# 解法二
class Node:
    __slots__ = 'son', 'fail', 'last', 'cnt'

    def __init__(self):
        self.son = [None] * 26
        self.fail = None  # 当 node.son[i] 失配时，node.fail.son[i] 即为下一个待匹配节点（等于 root 则表示没有匹配）
        self.last = None  # 后缀链接（suffix link），用来快速跳到一定是某个模式串末尾的节点（等于 root 则表示匹配结束）
        self.cnt = 0  # node 是 cnt 个模式串的末尾


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    # 把模式串 pattern 插入 AC 自动机（代码和字典树一样）
    def put(self, pattern: str) -> None:
        cur = self.root
        for ch in pattern:
            i = ord(ch) - ord('a')
            if cur.son[i] is None:
                cur.son[i] = Node()
            cur = cur.son[i]
        cur.cnt += 1

    # BFS，构建 AC 自动机的 fail 和 last，方便快速查询
    def build_fail(self) -> None:
        self.root.fail = self.root.last = self.root

        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
                continue
            son.fail = son.last = self.root  # 第一层的 fail 都指向根节点
            q.append(son)

        # BFS
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    # 把虚拟子节点 cur.son[i] 设置为 cur.fail.son[i]
                    # 方便失配时直接跳到下一个可能匹配的位置（但不一定是某个模式串的末尾）
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]  # 计算失配位置
                # 沿着 last 往上走，可以直接跳到一定是某个模式串末尾的节点（如果跳到 root 表示匹配结束）
                son.last = son.fail if son.fail.cnt else son.fail.last
                q.append(son)


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ac = AhoCorasick()
        for pattern in patterns:
            ac.put(pattern)
        ac.build_fail()

        ord_a = ord('a')
        cur = ac.root
        ans = 0
        for ch in word:
            cur = cur.son[ord(ch) - ord_a]  # 如果没有匹配，相当于移动到 fail 的 son[ord(ch)-ord_a]
            match_node = cur
            while match_node.cnt >= 0:
                ans += match_node.cnt
                match_node.cnt = -1  # 避免重复统计
                match_node = match_node.last  # 可能匹配更短的模式串，要继续在 last 链上找
        return ans


if __name__ == '__main__':
    print(Solution().numOfStrings(patterns = ["a","abc","bc","d"], word = "abc"))
    print(Solution().numOfStrings(patterns = ["a","b","c"], word = "aaaaabbbbb"))
    print(Solution().numOfStrings(patterns = ["a","a","a"], word = "ab"))




