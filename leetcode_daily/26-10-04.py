""" 678. 有效的括号字符串   中等
给你一个只包含三种字符的字符串，支持的字符类型分别是 '('、')' 和 '*'。请你检验这个字符串是否为有效字符串，如果是 有效 字符串返回 true 。
有效 字符串符合如下规则：
任何左括号 '(' 必须有相应的右括号 ')'。
任何右括号 ')' 必须有相应的左括号 '(' 。
左括号 '(' 必须在对应的右括号之前 ')'。
'*' 可以被视为单个右括号 ')' ，或单个左括号 '(' ，或一个空字符串 ""。

示例 1：输入：s = "()";   输出：true
示例 2：输入：s = "(*)";  输出：true
示例 3：输入：s = "(*))"; 输出：true

提示：
1 <= s.length <= 100
s[i] 为 '('、')' 或 '*'

"""


def checkValidString(self, s: str) -> bool:
    # left = []  # 存 '(' 的下标
    # star = []  # 存 '*' 的下标
    #
    # for i, c in enumerate(s):
    #     if c == '(':
    #         left.append(i)
    #     elif c == '*':
    #         star.append(i)
    #     else:
    #         # 遇到 ')'，优先用 '(' 匹配，没有就用 '*' 顶替
    #         if left:
    #             left.pop()
    #         elif star:
    #             star.pop()
    #         else:
    #             return False
    #
    # # 处理剩余的 '('：需要 '*' 在其右边才能当 ')' 来匹配
    # while left:
    #     l_idx = left.pop()
    #     if not star or star.pop() < l_idx:
    #         return False
    #
    # return True

    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo -= 1
            hi -= 1
        else:
            lo -= 1
            hi += 1
        if hi < 0:
            return False
        lo = max(lo, 0)
    return lo == 0


if __name__ == '__main__':
    print(checkValidString("(*)"))
    print(checkValidString("(*))"))
    print(checkValidString("()"))
