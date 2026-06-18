""" 1344. 时钟指针的夹角
给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。

示例 1：输入：hour = 12, minutes = 30;  输出：165
示例 2：输入：hour = 3, minutes = 30;  输出；75
示例 3：输入：hour = 3, minutes = 15;  输出：7.5
示例 4：输入：hour = 4, minutes = 50;  输出：155
示例 5：输入：hour = 12, minutes = 0;  输出：0

提示：
1 <= hour <= 12
0 <= minutes <= 59
与标准答案误差在 10^-5 以内的结果都被视为正确结果。
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-18.md

"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        :param hour: 小时
        :param minutes: 分钟
        :return: 夹角
        """
        # 获取时针和分针的夹角
        hour_angle = (hour % 12 + minutes / 60) * 30
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360 - angle)


if __name__ == '__main__':
    print(Solution().angleClock(12, 30))
    print(Solution().angleClock(3, 30))
    print(Solution().angleClock(3, 15))
