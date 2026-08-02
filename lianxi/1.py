""" Q1. 给定数位和的最大整数
给你两个非负整数 n 和 s。返回满足下述条件的 最大 整数：
最多有 n 位数字。
其各位数字之和等于 s 。
如果不存在这样的整数，则返回 -1。
"""
from collections import Counter


def largestInteger(self, n: int, s: int) -> int:
    if s > 9 * n:
        return -1
    ans = ''
    while n > 0:
        # 当前位能放的最大数字
        digit = min(9, s)
        ans += str(digit)
        s -= digit
        n -= 1
    return int(ans)


""" Q2. 聚合两个时间序列    中等  4 分
给你两个二维整数数组 series1 和 series2。
两个序列中的每个元素都表示为 [timestamp, value]，其中：
timestamp 是表示时间的整数。
value 是表示该时间点对应值的整数。
每个数组都按照 timestamp 的 严格递增 顺序排列。
若某个序列中某个时间戳 缺失 ，且该序列中存在更晚的时间戳，则将该缺失时间戳的值设为下一个更晚时间戳对应的值。否则，该时间点的值视为 0。
聚合序列 通过以下方式构造：对于两个序列中出现过的每个时间戳，将两个序列在该时间戳对应的值相加。
返回聚合后的序列，格式为二维整数数组 [timestamp, summedValue]，并按照 timestamp 严格递增 排序。
如果一个数组中的每个元素都严格大于前一个元素，则称该数组为 严格递增 。
"""
from typing import List

def aggregateTwoSeries(series1: List[List[int]], series2: List[List[int]]) -> List[List[int]]:
    # 收集所有时间戳并排序
    all_timestamps = sorted(set([t for t, _ in series1] + [t for t, _ in series2]))

    # 构建字典
    dict1 = {t: v for t, v in series1}
    dict2 = {t: v for t, v in series2}

    def get_backfill(series_dict: dict, series_list: List[List[int]], timestamp: int) -> int:
        """获取 timestamp 时刻的后向填充值（用下一个更晚时间戳的值）"""
        if timestamp in series_dict:
            return series_dict[timestamp]

        # 找大于 timestamp 的最小时间戳
        for t, v in series_list:
            if t > timestamp:
                return v  # 找到第一个更晚的时间戳，返回它的值

        # 没有更晚的时间戳，返回 0
        return 0

    ans = []
    for t in all_timestamps:
        # 获取 series1 在时间 t 的值（后向填充）
        val1 = get_backfill(dict1, series1, t)
        val2 = get_backfill(dict2, series2, t)
        ans.append([t, val1 + val2])


    # i, j = 0, 0
    # ans = []
    # while i<len(series1) and j<len(series2):
    #     if series1[i][0] < series2[j][0]:
    #         ans.append([series1[i][0], series1[i][1]+series2[j][1]])
    #         i += 1
    #     elif series1[i][0] > series2[j][0]:
    #         ans.append([series2[j][0], series1[i][1]+series2[j][1]])
    #         j += 1
    #     else:
    #         ans.append([series1[i][0], series1[i][1]+series2[j][1]])
    #         i += 1
    #         j += 1
    # if i==len(series1):
    #     while j<len(series2):
    #         ans.append([series2[j][0], series2[j][1]])
    #         j += 1
    # elif j==len(series2):
    #     while i<len(series1):
    #         ans.append([series1[i][0], series1[i][1]])
    #         i += 1
    # return ans


""" Q3. 统计有效序列数目    中等  5 分
给你两个正整数 n 和 k。
一个 有效序列 是一个由 k 个正整数组成的序列，满足以下条件：
序列中所有整数的 和 等于 n。
序列中所有整数的 乘积 是 偶数 。
返回有效序列的数量。由于答案可能很大，请将其对 109 + 7 取余 后返回。
如果两个序列在任何下标处不同，则认为它们是 不同 的序列。
例如，[1, 1, 2] 和 [1, 2, 1] 被认为是不同的序列。
提示：
1 <= n <= 5 * 10^5
1 <= k <= n
"""



""" Q1. 偶数次骑士移动 简单  3 分
给你两个整数数组 start 和 target，每个数组的形式均为 [x, y]，表示标准 8 x 8 国际象棋棋盘上的一个格子。
如果骑士可以用 偶数 次移动从 start 到达 target，则返回 true；否则返回 false。
注意：骑士的一次合法移动是：沿一个方向移动两格，再沿与其垂直的方向移动一格。
示例 1：
输入： start = [1,1], target = [2,2];  输出： true
解释：一种可行的移动序列为 (1, 1) -> (3, 2) -> (2, 4) -> (4, 3) -> (2, 2)。骑士经过 4 次移动到达目标位置，4 是偶数。因此答案为 true。
示例 2：
输入： start = [4,5], target = [6,6];  输出： false
解释：骑士无法用偶数次移动从 start = [4, 5] 到达 target = [6, 6]。因此答案为 false。

提示：
start.length == target.length == 2
0 <= start[i], target[i] <= 7
"""



""" Q1. 重新排列字符串以避免字符对   简单  3 分
给你一个字符串 s 和两个 不同 的小写英文字母 x 和 y。
重新排列 s 中的字符来构造一个新的字符串 t，使得：
t 是 s 的一个 排列。
在 t 中，所有 y 都必须在所有 x 之前。
返回 任意 一个有效的字符串 t。
排列 是对一个字符串中所有字符的重新排列。

提示：
1 <= s.length <= 100
s 仅由小写英文字母组成。
x 和 y 都是小写英文字母。
x != y
"""


def rearrangeString(s: str, x: str, y: str) -> str:
    cnt = Counter(s)
    if x not in cnt.values() and y not in cnt.values():
        return s
    ans = ''
    if y in cnt.values():
        ans = cnt[y] * y
    for c, num in enumerate(cnt):
        if c == x or c == y:
            continue
        ans = ans + cnt[c] * num
    if x in cnt.values():
        ans = ans + cnt[x] * x
    return ans


""" Q1. 按下时间最长的按钮   简单  3 分
给你一个二维数组 events，表示孩子在键盘上按下一系列按钮触发的按钮事件。
每个 events[i] = [indexi, timei] 表示在时间 timei 时，按下了下标为 indexi 的按钮。
数组按照 time 的递增顺序排序。
按下一个按钮所需的时间是连续两次按钮按下的时间差。按下第一个按钮所需的时间就是其时间戳。
返回按下时间 最长 的按钮的 index。如果有多个按钮的按下时间相同，则返回 index 最小的按钮。
 
示例 1：输入： events = [[1,2],[2,5],[3,9],[1,15]];   输出： 1
解释：下标为 1 的按钮在时间 2 被按下。
下标为 2 的按钮在时间 5 被按下，因此按下时间为 5 - 2 = 3。
下标为 3 的按钮在时间 9 被按下，因此按下时间为 9 - 5 = 4。
下标为 1 的按钮再次在时间 15 被按下，因此按下时间为 15 - 9 = 6。
最终，下标为 1 的按钮按下时间最长，为 6。

提示：
1 <= events.length <= 1000
events[i] == [indexi, timei]
1 <= indexi, timei <= 105
输入保证数组 events 按照 timei 的递增顺序排序。
"""
def buttonWithLongestTime(events: List[List[int]]) -> int:
    max_duration = -1
    result_idx = float('inf')

    prev_time = 0
    for i, (idx, time) in enumerate(events):
        # 计算当前事件的持续时间
        if i == 0:
            duration = time
        else:
            duration = time - prev_time

        # 更新结果:找持续时间最长的按钮
        if duration > max_duration or (duration == max_duration and idx < result_idx):
            max_duration = duration
            result_idx = idx

        prev_time = time

    return result_idx


