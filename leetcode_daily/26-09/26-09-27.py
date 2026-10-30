""" 1190. 反转每对括号间的子串    中等
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。

示例 1：输入：s = "(abcd)";           输出："dcba"
示例 2：输入：s = "(u(love)i)";       输出："iloveu"
解释：先反转子字符串 "love" ，然后反转整个字符串。
示例 3：输入：s = "(ed(et(oc))el)";   输出："leetcode"
解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。

提示：
1 <= s.length <= 2000
s 中只有小写英文字母和括号
题目测试用例确保所有括号都是成对出现的

"""

def reverseParentheses(s: str) -> str:
    # stack = []
    # for c in s:
    #     if c == ")":
    #         temp = ""
    #         while stack[-1] != "(":
    #             temp += stack.pop()
    #         stack.pop()
    #         stack += temp
    #     else:
    #         stack.append(c)
    #
    # return "".join(stack)

    n = len(s)
    pair = [0] * n
    stack = []

    # 预处理：匹配所有括号对，建立双向映射
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            j = stack.pop()
            pair[i] = j
            pair[j] = i

    # 线性遍历：遇到括号就跳转到匹配端，方向反转
    result = []
    i, direction = 0, 1
    while i < n:
        if s[i] == '(' or s[i] == ')':
            i = pair[i]  # 瞬移到括号另一端
            direction = -direction  # 掉头
        else:
            result.append(s[i])
        i += direction

    return "".join(result)


if __name__ == '__main__':
    print(reverseParentheses("(abcd)"))
    print(reverseParentheses("(u(love)i)"))
    print(reverseParentheses("(ed(et(oc))el)"))




