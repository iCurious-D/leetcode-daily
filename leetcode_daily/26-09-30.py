""" 1111. 有效括号的嵌套深度     中等
如果一个字符串仅由字符 "(" 和 ")" 组成，并且满足以下条件，则称为有效括号字符串（VPS）：
它是空字符串，或
它可以表示为 AB（A 连接 B），其中 A 和 B 都是VPS，或者
它可以表示为 (A)，其中 A 是一个 VPS。
我们可以类似地定义任何 VPS S 的嵌套深度 depth(S) 如下：
depth("") = 0
depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 VPS
depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 VPS。
例如，""，"()()" 和 "()(()())" 都是 VPS（嵌套深度 0，1 和 2），并且 ")(" 和 "(()" 不是 VPS。
给定一个 VPS 序列，将其拆分成两个不相交的子序列 A 和 B，使得 A 和 B 都是 VPS（且 A.length + B.length = seq.length）。
这些子序列不一定是连续的。
例如，对于序列 123456789，一种可能的拆分是：
A = {1, 3, 5, 7, 9}，
B = {2, 4, 6, 8}。
这对应于输出 [0, 1, 0, 1, 0, 1, 0, 1, 0]，其中 0 表示属于 A，1 表示属于 B。
现在选择 任意 这样的 A 和 B，使得 max(depth(A), depth(B)) 的值是最小的。
返回一个 answer 数组（长度为 seq.length），该数组编码了 A 和 B 的选择：
如果 seq[i] 是 A 的一部分则 answer[i] = 0，否则 answer[i] = 1。
请注意，尽管可能存在多种答案，但你可以返回其中任意一种。

示例 1：输入：seq = "(()())";     输出：[0,1,1,1,1,0]
示例 2：输入：seq = "()(())()";   输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。

提示：
1 < seq.size <= 10000

"""
from itertools import accumulate
from typing import List


def maxDepthAfterSplit(self, seq: str) -> List[int]:
    ans = []
    depth = 0
    for ch in seq:
        if ch == '(':
            depth += 1
            ans.append(depth & 1)
        else:
            ans.append(depth & 1)
            depth -= 1
    return ans

    # ans = []
    # depth = 0
    # for ch in seq:
    #     if ch == '(':
    #         ans.append(depth & 1)
    #         depth += 1
    #     else:
    #         depth -= 1
    #         ans.append(depth & 1)
    # return ans

    # return [(d - (c == ')')) % 2
    #         for d, c in zip(accumulate(seq, lambda d, c: d + (c == '(') - (c == ')'), initial=0), seq)]


def check(seq: str, ans: List[int]) -> None:
    """答案不唯一，所以校验 A/B 是否都是 VPS 并输出各自深度"""
    A = ''.join(c for c, t in zip(seq, ans) if t == 0)
    B = ''.join(c for c, t in zip(seq, ans) if t == 1)

    def depth(s: str) -> int:
        d = best = 0
        for c in s:
            d += 1 if c == '(' else -1
            if d < 0:
                return -1  # 前缀出现负余额 → 不是 VPS
            best = max(best, d)
        return best if d == 0 else -1

    print(f"{seq} -> {ans}")
    print(f"    A = {A} (深度 {depth(A)}), B = {B} (深度 {depth(B)}), "
          f"max = {max(depth(A), depth(B))}")


if __name__ == '__main__':
    check("(()())", maxDepthAfterSplit("(()())"))
    check("()(())()", maxDepthAfterSplit("()(())()"))
    check("(((()))((())))", maxDepthAfterSplit("(((()))((())))"))



