""" 22. 括号生成    中等
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：输入：n = 3;   输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：输入：n = 1;   输出：["()"]

提示：
1 <= n <= 8

"""
from typing import List


def generateParenthesis(n: int) -> List[str]:
    multiverse = []  # 存活时间线收集器
    timeline = []  # 当前正在演化的时间线

    def observe(open_cnt, close_cnt):
        # 2n 次观测完成，时间线定型
        if len(timeline) == 2 * n:
            multiverse.append(''.join(timeline))
            return

        if open_cnt < n:
            timeline.append('(')
            observe(open_cnt + 1, close_cnt)
            timeline.pop()  # 退相干：擦掉这步，回到观测前

        if close_cnt < open_cnt:
            timeline.append(')')
            observe(open_cnt, close_cnt + 1)
            timeline.pop()  # 换一条平行时间线继续观测

    observe(0, 0)  # 宇宙大爆炸：从虚无开始
    return multiverse


if __name__ == '__main__':
    print(generateParenthesis(3))
    print(generateParenthesis(1))
    print(generateParenthesis(2))


