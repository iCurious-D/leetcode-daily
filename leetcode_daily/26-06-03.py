""" 3635. 最早完成陆地和水上游乐设施的时间 II
给你两种类别的游乐园项目：陆地游乐设施 和 水上游乐设施。
陆地游乐设施: landStartTime[i] – 第 i 个陆地游乐设施最早可以开始的时间。
            landDuration[i] – 第 i 个陆地游乐设施持续的时间。
水上游乐设施: waterStartTime[j] – 第 j 个水上游乐设施最早可以开始的时间。
            waterDuration[j] – 第 j 个水上游乐设施持续的时间。
一位游客必须从 每个 类别中体验 恰好一个 游乐设施，顺序 不限 。
游乐设施可以在其开放时间开始，或 之后任意时间 开始。如果一个游乐设施在时间 t 开始，它将在时间 t + duration 结束。
完成一个游乐设施后，游客可以立即乘坐另一个（如果它已经开放），或者等待它开放。
返回游客完成这两个游乐设施的 最早可能时间 。

提示:
1 <= n, m <= 5 * 10^4
landStartTime.length == landDuration.length == n
waterStartTime.length == waterDuration.length == m
1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 10^5
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-03.md

"""
class Solution:
    def solve(self, firstStart, firstDur, secondStart, secondDur):
        # 从第一类设施中找出最早结束时间
        min_finish = min(start + dur for start, dur in zip(firstStart, firstDur))
        # 在第二类设施中，找最早完成时间
        return min(max(start, min_finish) + dur for start, dur in zip(secondStart, secondDur))

    def earliestCompletionTime(self, landStart, landDur, waterStart, waterDur):
        return min(self.solve(landStart, landDur, waterStart, waterDur), self.solve(waterStart, waterDur, landStart, landDur))


if __name__ == '__main__':
    print(Solution().earliestCompletionTime([2,8], [4,1], [6], [3]))
    print(Solution().earliestCompletionTime([5], [3], [1], [10]))
    print(Solution().earliestCompletionTime([1,2,3,4], [2,3,4,5], [1,2,3,4], [2,3,4,5]))
