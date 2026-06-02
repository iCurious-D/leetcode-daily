""" 3629. 通过质数传送到达终点的最少跳跃次数
给你一个长度为 n 的整数数组 nums。你从下标 0 开始，目标是到达下标 n - 1。
在任何下标 i 处，你可以执行以下操作之一：
移动到相邻格子：跳到下标 i + 1 或 i - 1，如果该下标在边界内。
质数传送：如果 nums[i] 是一个质数 p，你可以立即跳到任何满足 nums[j] % p == 0 的下标 j 处，且下标 j != i 。
返回到达下标 n - 1 所需的 最少 跳跃次数。
质数 是一个大于 1 的自然数，只有两个因子，1 和它本身。
"""

""" 【翻译】
你被困在一条由 数字密室 连接而成的长廊里，密室从左到右排开，编号 0 到 n-1。
每间密室的墙壁上写着一个数字 nums[i]。
你的目标是：从 0 号密室出发，用最少的步数，抵达 n-1 号密室，逃出生天。

你有两种移动手段：
挪步：老老实实推开隔壁的门，走到 i+1 或 i-1（只要那间密室还在长廊里）。每推开一扇门，算作 1 次跳跃。
质数宝石：如果当前密室墙上的数字是一个 质数 p，那么恭喜你，你手心里会出现一颗发光的宝石。握紧它，你会瞬间被传送到 任意一间墙上数字能被 p 整除的密室（不能原地不动）。这次传送也算作 1 次跳跃。

你看着长廊，心里明白：
这就是一张隐形的网。每间密室是一个节点，挪步是短边，质数宝石是超级长边。你要找的，是从起点到终点的最短路径。

于是你知道是时候召唤出 光波神器（BFS），从起点开始一圈一圈向外扩散，不断点亮下一个可达的密室。
第 0 层：只有起点 0。
第 1 层：所有从起点走一步能到的密室（相邻的，以及如果起点数字是质数的话，所有能被它整除的密室）。
第 2 层：从第 1 层再走一步能到的密室……
以此类推，直到某一天，光波触及了终点 n-1，那一刻的层数，就是最少的跳跃次数。

这里有个时间陷阱：
如果某颗质数宝石对应的质数是 p，那么从任何一间密室触发这颗宝石，你都会被传送到 同一批 密室（所有能整除 p 的房间）。
如果光波每到达一个拥有 p 的密室，都去把那一批房间全部重新检查一遍，那就像拿着同一把钥匙反复去开已经打开的锁，白白浪费力气，光波的速度会慢到让你绝望。
所以你立下一条规矩：
每一颗质数宝石，一生只能用一次。

当光波第一次点亮了某个质数 p 的密室，你立刻就捏碎这颗宝石，让宝石的光芒点亮所有 nums[j] % p == 0 的未知密室，将它们全部收入下一层。
然后这颗宝石就永远粉碎了，之后再有密室拿着同样的质数 p，也再榨不出一丝新的光芒——因为这些密室早已经被照亮过了。
这样，每个质数至多被处理一次，每间密室也至多被入队一次，光纹才能以最快的速度抵达终点。

为了让光波扩散时不手忙脚乱，你决定在出发前，提前使用欧拉筛，画好传送阵：
筛选出 1 到 max(nums) 里的所有质数，为每个质数 p 准备一个空名单；
遍历一遍数组，遇到能整除 p 的数字，就把它的下标写进 p 的名单里。
这些名单，就是“传送阵眼”。
日后光波触发某颗宝石 p 时，只需把 p 的名单里所有还没被点亮的密室，一口气灌入下一层光芒，并标记点亮（等于捏碎宝石），绝不拖沓。

行动吧！
步伐计数，出口浮现：
当光芒终于照到 n-1 号密室的那一刹那，你站的这一层，就是答案。
收起光波神器，你知道，有光波神器助力和捏碎宝石的决心，任何长廊的长度和数字的大小，都不足以困住你太久。
"""

from typing import List
from collections import deque


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # 如果只有一个密室，起点即终点，不需要移动

        max_val = max(nums)

        # ---------- 1. 欧拉筛，求出每个数的最小质因子 (预处理) ----------
        spf = list(range(max_val + 1))  # smallest prime factor
        is_prime = [False] * (max_val + 1)
        primes = []
        for i in range(2, max_val + 1):
            if spf[i] == i:  # i 是质数
                is_prime[i] = True
                primes.append(i)
            for p in primes:
                if p * i > max_val:
                    break
                spf[p * i] = p
                if i % p == 0:
                    break

        # ---------- 2. 为每个质数准备“传送名单” (索引构建) ----------
        # prime_to_indices[p] 记录所有下标 j，满足 nums[j] % p == 0
        prime_to_indices = [[] for _ in range(max_val + 1)]
        for idx, val in enumerate(nums):
            temp = val
            while temp > 1:
                p = spf[temp]  # 查表，直接拿出 temp 的最小质因子 p
                prime_to_indices[p].append(idx)  # 在当前质因子 p 的名单里记下当前下标。
                while temp % p == 0:
                    temp //= p  # 把 temp 里所有的 p 因子全部除干净，以便寻找下一个不同的质因子

        # ---------- 3. 光之波纹 (BFS) ----------
        visited = [False] * n
        used_prime = [False] * (max_val + 1)  # 记录哪些质数的“传送能力”已经用过了（每颗宝石只用一次）

        q = deque()
        q.append((0, 0))  # (下标, 已走步数)
        visited[0] = True

        while q:
            # 当前位置 i
            i, step = q.popleft()

            # 到达终点？
            if i == n - 1:
                return step  # 如果到了最后一个密室，因为 BFS 的特性，这一定是最短步数，直接返回。

            # 下一层：
            # 第一种情况：挪步到相邻密室
            for nb in (i - 1, i + 1):
                if 0 <= nb < n and not visited[nb]:
                    visited[nb] = True
                    q.append((nb, step + 1))

            # 第二种情况：质数宝石传送
            #  看看当前这个密室的数值是不是个质数宝石:
            p = nums[i]
            if p <= max_val and is_prime[p] and not used_prime[p]:
                used_prime[p] = True  # 捏碎这颗宝石：一旦使用，立即标记为已消耗。
                # 翻出之前准备好的“传送名单”，把名单上所有没去过的地方全部标记并入队
                for j in prime_to_indices[p]:
                    if not visited[j]:
                        visited[j] = True
                        q.append((j, step + 1))

        # 有相邻移动兜底，理论上不会执行到这里
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.minJumps(nums=[100, 23, 23, 404, 100, 23, 23, 23, 3, 404]))  # 4
    print(s.minJumps(nums=[7]))  # 0
    print(s.minJumps(nums=[7, 6, 9, 6, 9, 6, 9, 7]))  # 1
    print(s.minJumps(nums=[6, 1, 7]))  # 2
    print(s.minJumps(nums=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))  # 2
    print(s.minJumps(nums=[5, 4, 3, 2, 1]))  # 4








