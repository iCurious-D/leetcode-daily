""" 921. 使括号有效的最少添加     中等
只有满足下面几点之一，括号字符串才是有效的：
它是一个空字符串，或者
它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
它可以被写作 (A)，其中 A 是有效字符串。
给定一个括号字符串 s ，在每一次操作中，你都可以在字符串的任何位置插入一个括号
例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
返回 为使结果字符串 s 有效而必须添加的最少括号数。

示例 1：输入：s = "())";  输出：1
示例 2：输入：s = "(((";  输出：3

提示：
1 <= s.length <= 1000
s 只包含 '(' 和 ')' 字符。

"""
def minAddToMakeValid(s: str) -> int:
    bal = ans = 0
    for c in s:
        bal += 1 if c == '(' else -1
        if bal < 0:
            ans += 1
            bal = 0
    return ans + bal

    # # 答案 = 总长度 - 2 × 能配对的括号数
    # matched = 0
    # depth = 0
    # for c in s:
    #     if c == '(':
    #         depth += 1
    #     elif depth > 0:
    #         depth -= 1
    #         matched += 1
    # return len(s) - 2 * matched


if __name__ == '__main__':
    print(minAddToMakeValid("())"))
    print(minAddToMakeValid("((("))
    print(minAddToMakeValid("()"))







