""" 2784 检查数组是否是好的
给你一个整数数组 nums ，如果它是数组 base[n] 的一个排列，我们称它是个 好 数组。
base[n] = [1, 2, ..., n - 1, n, n] （换句话说，它是一个长度为 n + 1 且包含 1 到 n - 1 恰好各一次，包含 n  两次的一个数组）。
比方说，base[1] = [1, 1] ，base[3] = [1, 2, 3, 3] 。
如果数组是一个好数组，请你返回 true ，否则返回 false 。
注意：数组的排列是这些数字按任意顺序排布后重新得到的数组。

=========================================================================
作为刚出新手村的小白，你今天要挑战的Boss，正是力扣第2784号“好数组鉴定官”。
看到它头顶绿色的难度标签(简单)，你有些激动地搓手手，翻出系统送的大礼包——Python 内置函数三件套：“看我三招之内拿下它！”
    # biggest, length = max(nums), len(nums)
    # if length != biggest + 1 or nums.count(biggest) != 2:
    #     return False
    # return True if len(set(nums)) == biggest else return False
这操作就像去副本打 Boss，先开个全屏扫描max()，再挨个查身份证count()，最后还整个全家桶去重大礼包set()。朴实无华？不，这是朴实且费电！

“年轻人，你这样打，虽然能过，但全是地毯式轰炸。max 扫一遍，count 又扫一遍，set 再扫一遍。
你这是把每个小怪都踹了三脚，人家小怪不要面子的啊？ 时间复杂度 O(n) 被你硬生生干成 O(3n)，内存也吃得跟猪一样。"

你回头一看，一位骑着 "O(1) 空间神兽" 的大佬正叼着草叶斜眼看你。
"那你说咋整？难道还能边打架边记账不成？"你握紧铁剑，一脸不服。
大佬嘴角上扬，手指翻飞，在虚空刻下四个大字：「原地蹦迪」。
    n = len(nums) - 1
    cnt_n = 0
    for x in nums:
        x = abs(x)
        if (x > n or x == n and cnt_n > 1 or x < n and nums[x] < 0):
            return False
        if x == n:
            cnt_n += 1
        else:
            nums[x] = -nums[x]
    return True

※ 开局先算卦，反推大 Boss：n = len(nums) - 1
看到数组长度，直接减一就能反推出那个会分身的 Boss n 是谁。
开局就把底裤看穿，稳如老狗。
顺手掏出一个计数器 cnt_n = 0，专门盯着 Boss n 的分身数量。现在还没遇到。

※  逐个来审问，强制现原形：for x in nums:
     x = abs(x)
重点来了！ 为啥要先 abs(x) ？因为后面我们会把数字狠狠拍进地里变成负数做标记。如果不取绝对值，等会儿捡起来一看是 -3，你就懵逼了："这货怎么还是负的？"
所以甭管你现在是倒立、躺平还是头插地，先给我摆正了，老老实实报上名来！﻿
※  审判有三连，红牌就滚蛋
    x > n         or       x == n and cnt_n > 1        or        x < n and nums[x] < 0
阎王殿三堂会审，任何一条触发，直接 return False，放悲伤唢呐，抬走下一位：
审判一：x > n —— 你谁啊？地图都没开到这！”叉出去，这数组绝对冒牌货。
审判二：x == n and cnt_n > 1 —— 遇到boss也不手软！"说好的最多两个，你搁这儿搞克隆人军团呢？灭霸都没你能复制！" 红牌罚下。
审判三：x < n and nums[x] < 0 —— 这坑已经被占了，滚！这是原地标记的精髓所在。当遇到小弟 x（小于 n 的数字）时，去检查数组索引 x 位置的值。如果 nums[x] 已经是负数，说明这个数字之前有小弟通过索引来过了，现在又来一个，那就是重复的狗血剧情——"这个位置已经有爷占坑了，你还敢来？" 直接判定非法，这数组连坑位都抢不明白。

※  老大加分身，小弟做标记
如果这哥们儿侥幸通过三堂会审，就可以办理"登记手续"了：
    if x == n: cnt_n += 1
    else: nums[x] = -nums[x]  # 标记 x 遇到过
如果 x 是 Boss n，计数器加一，允许它囤积一个分身。
如果是普通数字，那就进行灵魂操作：把 nums[x] 变成负数！ 相当于在索引 x 的位置插了面旗子，写上 “爷来过，别惹我” ，既保留了原本的数字信息（大不了以后 abs 回来），又留下一个“此地已被占”的铁证。
数组原地变成留言板，连个额外的哈希表都不肯开，资本家看了都流泪。

如果整个循环跑完，没有任何人被叉出去，那么恭喜，该数组成功认证为"好数组"，严格遵守了 "一个boss俩分身，其他成员全单身" 的纪律，堪称模范团队。

你不由得惊叹，“这个 '原地蹦迪流' 解法，极其骚包，空间复杂度 O(1)，把数组玩成了画板，简直是极简美学的典范，抠门艺术的巅峰。
大佬重新叼起草叶："记住，有时候，数组本身，就是最强的武器。"

"""
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # biggest = max(nums)
        # length = len(nums)
        # if length != biggest + 1 or nums.count(biggest) != 2:
        #     return False
        # if len(set(nums)) == biggest:
        #     return True
        # return False
        n = len(nums) - 1
        cnt_n = 0
        for x in nums:
            x = abs(x)
            if (x > n or
                    x == n and cnt_n > 1 or
                    x < n and nums[x] < 0):  # x 之前遇到过，现在又遇到了，所以 x 的出现次数至少是 2
                return False
            if x == n:
                cnt_n += 1
            else:
                nums[x] = -nums[x]  # 标记 x 遇到过
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isGood([1,3,3,2]))
    print(s.isGood([1,1]))
    print(s.isGood([3,4,4,1,1,2]))

