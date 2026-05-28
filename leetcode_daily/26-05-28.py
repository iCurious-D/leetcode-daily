""" 3093. 最长公共后缀查询
给你两个字符串数组 wordsContainer 和 wordsQuery 。
对于每个 wordsQuery[i] ，你需要从 wordsContainer 中找到一个与 wordsQuery[i] 有 最长公共后缀 的字符串。
如果 wordsContainer 中有两个或者更多字符串有最长公共后缀，那么答案为长度 最短 的。
如果有超过两个字符串有 相同 最短长度，那么答案为它们在 wordsContainer 中出现 更早 的一个。
请你返回一个整数数组 ans ，其中 ans[i]是 wordsContainer中与 wordsQuery[i] 有 最长公共后缀 字符串的下标。

示例 1：输入：wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
输出：[1,1,1]
解释：我们分别来看每一个 wordsQuery[i] ：
对于 wordsQuery[0] = "cd" ，wordsContainer 中有最长公共后缀 "cd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。
对于 wordsQuery[1] = "bcd" ，wordsContainer 中有最长公共后缀 "bcd" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。
对于 wordsQuery[2] = "xyz" ，wordsContainer 中没有字符串跟它有公共后缀，所以最长公共后缀为 "" ，下标为 0 ，1 和 2 的字符串都得到这一公共后缀。这些字符串中， 答案是下标为 1 的字符串，因为它的长度为 3 ，是最短的字符串。

示例 2：输入：wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]
输出：[2,0,2]
解释：我们分别来看每一个 wordsQuery[i] ：
对于 wordsQuery[0] = "gh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。
对于 wordsQuery[1] = "acbfgh" ，只有下标为 0 的字符串有最长公共后缀 "fgh" 。所以尽管下标为 2 的字符串是最短的字符串，但答案是 0 。
对于 wordsQuery[2] = "acbfegh" ，wordsContainer 中有最长公共后缀 "gh" 的字符串下标分别为 0 ，1 和 2 。这些字符串中，答案是下标为 2 的字符串，因为它的长度为 6 ，是最短的字符串。


提示：
1 <= wordsContainer.length, wordsQuery.length <= 10^4
1 <= wordsContainer[i].length <= 5 * 10^3
1 <= wordsQuery[i].length <= 5 * 10^3
wordsContainer[i] 只包含小写英文字母。
wordsQuery[i] 只包含小写英文字母。
wordsContainer[i].length 的和至多为 5 * 10^5 。
wordsQuery[i].length 的和至多为 5 * 10^5 。
================================================================================================

解路径：. / leetcode_daily_stories / 26-05-28.md


"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_len = float('inf')
        self.best_idx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int):
        node = self.root
        if len(word) < node.best_len:
            node.best_len = len(word)
            node.best_idx = idx
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(word) < node.best_len:
                node.best_len = len(word)
                node.best_idx = idx

    def query(self, word: str) -> int:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                break
        return node.best_idx


class Node:
    __slots__ = 'son', 'min_len', 'best_index'

    def __init__(self):
        self.son = [None] * 26
        self.min_len = float('inf')  # 子树中的最短字符串的长度


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # ans = []
        # for q in wordsQuery:
        #     best_idx = -1
        #     best_len = -1
        #     best_word_len = float('inf')
        #     for idx, w in enumerate(wordsContainer):
        #         i, j = len(q) - 1, len(w) - 1
        #         common = 0
        #         while i >= 0 and j >= 0 and q[i] == w[j]:
        #             common += 1
        #             i -= 1
        #             j -= 1
        #         if common > best_len:
        #             best_len = common
        #             best_idx = idx
        #             best_word_len = len(w)
        #         elif common == best_len:
        #             if best_word_len > len(w) or (best_word_len == len(w) and idx < best_idx):
        #                 best_idx = idx
        #                 best_word_len = len(w)
        #     ans.append(best_idx)
        # return ans

        # trie = Trie()
        # for idx, w in enumerate(wordsContainer):
        #     rev_word = w[::-1]
        #     trie.insert(rev_word, idx)
        # res = []
        # for q in wordsQuery:
        #     rev_q = q[::-1]
        #     res.append(trie.query(rev_q))
        # return res

        ord_a = ord('a')
        root = Node()
        for i, s in enumerate(wordsContainer):
            len_s = len(s)
            if len_s < root.min_len:
                root.min_len = len_s
                root.best_index = i

            # 把 s[::-1] 插入字典树
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    cur.son[c] = Node()
                cur = cur.son[c]
                # 维护 cur 子树中的最短字符串的长度及其下标
                # 由于我们是按照 i 从小到大的顺序遍历，字符串长度相同时不更新 best_index
                if len_s < cur.min_len:
                    cur.min_len = len_s
                    cur.best_index = i

        ans = []
        for s in wordsQuery:
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            # 退出循环时，cur 即最长公共前缀（的对应节点），cur.best_index 是前缀为 cur 的最短字符串的下标
            ans.append(cur.best_index)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.stringIndices(wordsContainer=["abcd", "bcd", "xbcd"], wordsQuery=["cd", "bcd", "xyz"]))
    print(s.stringIndices(wordsContainer=["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"]))
    print(s.stringIndices(wordsContainer=["a", "b", "c"], wordsQuery=["a", "b", "c"]))
