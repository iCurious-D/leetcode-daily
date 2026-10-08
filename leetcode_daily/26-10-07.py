""" 301. 删除无效的括号    困难
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。

示例 1：输入：s = "()())()";  输出：["(())()","()()()"]
示例 2：输入：s = "(a)())()"; 输出：["(a())()","(a)()()"]
示例 3：输入：s = ")(";       输出：[""]

提示：
1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

"""
from typing import List


def removeInvalidParentheses(s: str) -> List[str]:
    def isValid(string):
        count = 0
        for ch in string:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    # DFS
    left_remove = right_remove = 0
    for ch in s:
        if ch == '(':
            left_remove += 1
        elif ch == ')':
            if left_remove > 0:
                left_remove -= 1
            else:
                right_remove += 1

    result = []

    def dfs(start, left_rem, right_rem, curr):
        if left_rem == 0 and right_rem == 0:
            if isValid(curr):
                result.append(curr)
            return

        for i in range(start, len(curr)):
            if i > start and curr[i] == curr[i - 1]:
                continue
            if curr[i] == '(' and left_rem > 0:
                dfs(i, left_rem - 1, right_rem, curr[:i] + curr[i + 1:])
            elif curr[i] == ')' and right_rem > 0:
                dfs(i, left_rem, right_rem - 1, curr[:i] + curr[i + 1:])

    dfs(0, left_remove, right_remove, s)
    return result

    # BFS
    # if isValid(s):
    #     return [s]
    #
    # queue = deque([s])
    # visited = {s}
    # found = False
    # result = []
    #
    # while queue:
    #     curr = queue.popleft()
    #     if isValid(curr):
    #         result.append(curr)
    #         found = True
    #     if found:
    #         continue
    #     for i in range(len(curr)):
    #         if curr[i] not in '()':
    #             continue
    #         next_str = curr[:i] + curr[i + 1:]
    #         if next_str not in visited:
    #             visited.add(next_str)
    #             queue.append(next_str)
    #
    # return result


if __name__ == '__main__':
    print(removeInvalidParentheses("()())()"))
    print(removeInvalidParentheses("(a)())()"))
    print(removeInvalidParentheses(")("))


