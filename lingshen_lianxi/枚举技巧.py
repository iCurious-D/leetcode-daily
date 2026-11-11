""" 枚举技巧
§0.1 枚举右，维护左    &&      §0.2 枚举中间    &&    §0.3 遍历对角线
对于 双变量问题，例如两数之和 a_i + a_j = t，
可以枚举右边的 a_j ，转化成 单变量问题，也就是在 a_j 左边查找是否有 a_i = t − a_j ，
这可以用哈希表维护。我把这个技巧叫做 枚举右，维护左。
下面这些题目，如果可以，请用一次遍历实现。
"""
from collections import defaultdict, Counter
from math import inf, comb
from string import ascii_lowercase
from typing import List
from sortedcontainers import SortedList
MOD = 10 ** 9 + 7


# §0.1.1 基础 =====================================================================================
# 1. 两数之和
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


# 1512. 好数对的数目 1161 相当于两数之差等于 0
def numIdenticalPairs(nums: List[int]) -> int:
    ans = 0
    cnt = defaultdict(int)
    for x in nums:
        ans += cnt[x]
        cnt[x] += 1
    return ans


# 2441. 与对应负数同时存在的最大正整数 1168 相当于两数之和等于 0
def findMaxK(nums: List[int]) -> int:
    ans = -1
    s = set()
    for num in nums:
        if -num in s:
            ans = max(ans, abs(num))
        s.add(num)
    return ans


# 4074. 和为目标值的最大乘积对 1232
def maxProductPair(nums: List[int], target: int) -> List[int]:
    dt = {}
    best_i, best_j = -1, -1
    for i, num in nums:
        if num * 2 == target:
            continue
        j = dt.get(target - num, -1)
        if j >= 0 and (best_i < 0 or num * (target-num) > nums[best_i] * (target - nums[best_i])):
            best_i, best_j = i, j
        dt[num] = i
    if best_i >= 0 and nums[best_i] < nums[best_j]:
        best_i, best_j = best_j, best_i
    return [best_i, best_j]


# 121. 买卖股票的最佳时机
def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# 2016. 增量元素之间的最大差值 1246
def maximumDifference(nums: List[int]) -> int:
    max_diff = 0
    min_num = inf
    for num in nums:
        max_diff = max(max_diff, num - min_num)
        min_num = min(min_num, num)
    return max_diff or -1


# 624. 数组列表中的最大距离
def maxDistance(arrays: List[List[int]]) -> int:
    max_dis = 0
    min_num = inf
    max_num = -inf
    for a in arrays:
        max_dis = max(max_dis, a[-1] - min_num, max_num - a[0])
        min_num = min(min_num, a[0])
        max_num = max(max_num, a[-1])
    return max_dis


# 3880. 两个值之间的最小绝对差值 1257
def minAbsoluteDifference(nums: List[int], x: int) -> int:
    ans = inf
    last = [-inf] * 2
    for i, x in enumerate(nums):
        if x > 0:
            x -= 1
            ans = min(ans, i - last[x ^ 1])
            last[x] = i
    return ans if ans < inf else -1


# 2342. 数位和相等数对的最大和 1309
def maximumSum(nums: List[int]) -> int:
    ans = -inf
    # # max_num = defaultdict(int)
    max_num = [-inf] * 82
    # for i, x in enumerate(nums):
    #     s = sum(map(int, str(x)))
    #     # if s in max_num:
    #     #     ans = max(ans, x + max_num[s])
    #     ans = max(ans, x + max_num[s])
    #     max_num[s] = max(max_num[s], x)
    for i, x in enumerate(nums):
        s = 0
        num = x
        while num:
            s += num % 10
            num //= 10
        ans = max(ans, x + max_num[s])
        max_num[s] = max(max_num[s], x)
    return ans


# 3979. 最大有效数对和 1328
def maxValidPairSum(nums: List[int], k: int) -> int:
    ans = max_num = 0
    for j in range(k, len(nums)):
        max_num = max(max_num, nums[j])
        ans = max(ans, nums[j] + max_num)
    return ans


# 1128. 等价多米诺骨牌对的数量 1333
def numEquivDominoPairs(nums: List[List[int]]) -> int:
    ans = 0
    cnt = defaultdict(int)
    for x in nums:
        x = tuple(sorted(x))
        ans += cnt[x]
        cnt[x] += 1
    return ans


# 1679. K 和数对的最大数目 1346
def maxOperations(nums: List[int], k: int) -> int:
    ans = 0
    cnt = defaultdict(int)
    for x in nums:
        if cnt[k-x]:
            cnt[k-x] -= 1
            ans += 1
        else:
            cnt[x] += 1
    return ans


# 面试题 16.24. 数对和
def pairSums(nums: List[int], target: int) -> List[List[int]]:
    ans = []
    cnt = defaultdict(int)
    for x in nums:
        if cnt[target-x]:
            ans.append([target-x, x])
            cnt[target-x] -= 1
        else:
            cnt[x] += 1
    return ans


# 219. 存在重复元素 II
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    last = {}
    for i, x in enumerate(nums):
        if x in last and i - last[x] <= k:
            return True
        last[x] = i
    return False
    # seen = set()
    # for i, x in enumerate(nums):
    #     if x in seen:
    #         return True
    #     seen.add(x)
    #     if len(seen) > k:
    #         seen.remove(nums[i-k])
    # return False


# 2260. 必须拿起的最小连续卡牌数 1365
def minimumCardPickup(cards: List[int]) -> int:
    ans = inf
    last = {}
    for i, x in enumerate(cards):
        if x in last:
            ans = min(ans, i - last[x] + 1)
        last[x] = i
    return ans if ans < inf else 0


# 2001. 可互换矩形的组数 1436
def interchangeableRectangles(rectangles: List[List[int]]) -> int:
    seen = defaultdict(int)
    ans = 0
    for rec in rectangles:
        key = rec[0] / rec[1]
        if key in seen:
            ans += seen[key]
        seen[key] += 1
    return ans


# 2815. 数组中的最大数对和 非暴力做法
def maxSum(nums: List[int]) -> int:
    ans = -1
    seen = [-inf] * 10
    for x in nums:
        max_d = max(map(int, str(x)))
        ans = max(ans, x + seen[max_d])
        seen[max_d] = max(seen[max_d], x)
    return ans


# 3623. 统计梯形的数目 I 1580
def countTrapezoids(points: List[List[int]]) -> int:
    MOD = 1000000007
    ans = s = 0
    cnt = Counter(p[1] for p in points)
    for c in cnt.values():
        k = c * (c-1) // 2
        ans += s * k
        s += k
    return ans % MOD


# 2364. 统计坏数对的数目 1622
def countBadPairs(nums: List[int]) -> int:
    ans = comb(len(nums), 2)
    cnt = defaultdict(int)
    for i, x in enumerate(nums):
        ans -= cnt[x-i]
        cnt[x-i] += 1
    return ans


# 3805. 统计凯撒加密对数目 1624
def countPairs(words: List[str]) -> int:
    ans = 0
    cnt = defaultdict(int)
    for word in words:
        tmp = list(word)
        base = ord(tmp[0])
        for i in range(len(tmp)):
            tmp[i] = chr((ord(tmp[i])-base)%26)
        tmp = ''.join(tmp)
        ans += cnt[tmp]
        cnt[tmp] += 1
    return ans


# 3371. 识别数组中的最大异常值 1644
def getLargestOutlier(nums: List[int]) -> int:
    ans = -inf
    cnt = Counter(nums)
    total = sum(nums)
    for x in nums:
        cnt[x] -= 1
        if (total-x) % 2 == 0 and cnt[total-x] > 0:
            ans = max(ans, x)
        cnt[x] += 1
    return ans


# 3761. 镜像对之间最小绝对距离 1669
def minMirrorPairDistance(nums: List[int]) -> int:
    ans = inf
    last_seen = {}
    for i, x in enumerate(nums):
        if x in last_seen:
            ans = min(ans, i - last_seen[x])
        rev_x = int(str(x)[::-1])
        last_seen[rev_x] = i
    return ans if ans < inf else -1


# 1014. 最佳观光组合 1730
def maxScoreSightseeingPair(values: List[int]) -> int:
    ans = last_max = 0
    for i, x in enumerate(values):
        ans = max(ans, x-i+last_max)
        last_max = max(last_max, x+i)
    return ans


# 1814. 统计一个数组中好对子的数目 1738
def countNicePairs(nums: List[int]) -> int:
    MOD = 1000000007
    ans = 0
    cnt = defaultdict(int)
    for i, x in enumerate(nums):
        rev_x = int(str(x)[::-1])
        ans += cnt[x-rev_x]
        cnt[x-rev_x] += 1
    return ans % MOD


# 3584. 子序列首尾元素的最大乘积 1763
def maximumProduct(nums: List[int], m: int) -> int:
    ans = -inf
    mn = inf
    mx = -inf
    for i in range(m-1, len(nums)):
        mn = min(mn, nums[i-m+1])
        mx = max(mx, nums[i-m+1])
        ans = max(ans, nums[i] * mn, nums[i] * mx)
    return ans


# 2905. 找出满足差值条件的下标 II 1764 思考题：求下标对的个数
def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    max_idx = min_idx = 0
    for j in range(indexDifference, len(nums)):
        i = j - indexDifference
        if nums[i] > nums[max_idx]:
            max_idx = i
        elif nums[i] < nums[min_idx]:
            min_idx = i
        if nums[max_idx] - nums[j] >= valueDifference:
            return [max_idx, j]
        elif nums[j] - nums[min_idx] >= valueDifference:
            return [min_idx, j]
    return [-1, -1]


# 3837. 相等元素的延迟计数（会员题）
# 3907. 统计具有相反奇偶性的较小元素（会员题）


# §0.1.2 进阶 =========================================================================================
# 1010. 总持续时间可被 60 整除的歌曲
# 3185. 构成整天的下标对数目 II 同 1010 题
# 2748. 美丽下标对的数目
# 2506. 统计相似字符串对的数目
# 2874. 有序三元组中的最大值 II 1583
# 1497. 检查数组对是否可以被 k 整除 1787
# 1477. 找两个和为目标值且不重叠的子数组 1851
# 1031. 两个无重叠子数组的最大和
# 2555. 两个线段获得的最多奖品 2081
# 1995. 统计特殊四元组 四个数
# 3404. 统计特殊子序列的数目 2445 四个数
# 3267. 统计近似相等数对 II 2545
# 3480. 删除一个冲突对后最大子数组数目 2764
# 1214. 查找两棵二叉搜索树之和（会员题）
# 2964. 可被整除的三元组数量（会员题）

# 思维扩展 ====================================================================================================
# 3917. 统计下标的相反奇偶性得分 做到 O(n)
# 2078. 两栋颜色不同且距离最远的房子 做到 O(n)
# 454. 四数相加 II
# 220. 存在重复元素 III
# 3027. 人员站位的方案数 II 2020
# 3548. 等和矩阵分割 II 2245 代码复用
# 3713. 最长的平衡子串 I 非暴力写法


""" §0.2 枚举中间 ==============================================================================================
对于有三个或者四个变量的问题，枚举中间的变量往往更好算。
为什么？比如问题有三个下标，需要满足 0 ≤ i < j < k < n，对比一下：
枚举 i，后续计算中还需保证 j < k。枚举 k 同理。
枚举 j，那么 i 和 k 自动被 j 隔开，互相独立，后续计算中无需关心 i 和 k 的位置关系。
所以枚举中间的变量更简单。
"""
# §0.2.1 基础 =======================================================================================
# 3583. 统计特殊三元组 1510 也可以一次遍历
def specialTriplets(nums: List[int]) -> int:
    suf = Counter(nums)
    pre = defaultdict(int)
    ans = 0
    for x in nums:
        suf[x] -= 1
        ans += pre[x * 2] * suf[x * 2]
        pre[x] += 1
    return ans % MOD
    # cnt1 = defaultdict(int)
    # cnt12 = defaultdict(int)
    # cnt123 = 0
    # for x in nums:
    #     if x % 2 == 0:
    #         cnt123 += cnt12[x//2]
    #     cnt12[x] += cnt1[x * 2]
    #     cnt1[x] += 1
    # return cnt123 % MOD


# 1930. 长度为 3 的不同回文子序列 1533
def countPalindromicSubsequence(s: str) -> int:
    suf = Counter(s[1:])
    pre = set()
    ans = set()
    for i in range(1, len(s)-1):
        mid = s[i]
        suf[mid] -= 1
        if suf[mid] == 0:
            del suf[mid]
        pre.add(s[i-1])
        for alpha in pre & suf.keys():
            ans.add(alpha + mid)
    return len(ans)
    # ans = 0
    # for alpha in ascii_lowercase:
    #     i = s.find(alpha)
    #     if i < 0:
    #         continue
    #     j = s.rfind(alpha)
    #     ans += len(set(s[i+1:j]))
    # return ans


# 3128. 直角三角形 1541
def numberOfRightTriangles(grid: List[List[int]]) -> int:
    ans = 0
    col_sum = [sum(col) - 1 for col in zip(*grid)]
    for row in grid:
        row_sum = sum(row) - 1
        ans += row_sum * (sum(cs for x, cs in zip(row, col_sum) if x))
    return ans


# §0.2.2 进阶 ========================================================================================
# 2909. 元素和最小的山形三元组 II 1479
def minimumSum(nums: List[int]) -> int:
    n = len(nums)
    suf = [0] * n
    suf[-1] = nums[-1]
    for i in range(n-2, 1, -1):
        suf[i] = min(suf[i+1], nums[i])
    ans = inf
    pre = nums[0]
    for j in range(1, n-1):
        if pre < nums[j] > suf[j+1]:
            ans = min(ans, pre + nums[j] + suf[j+1])
        pre = min(pre, nums[j])
    return ans if ans < inf else -1


# 2874. 有序三元组中的最大值 II 1583 也可以一次遍历
def maximumTripletValue(nums: List[int]) -> int:
    n = len(nums)
    suf_max = [0] * n
    suf_max[-1] = nums[-1]
    for i in range(n-2, 1, -1):
        suf_max[i] = max(suf_max[i+1], nums[i])
    ans = 0
    pre_max = nums[0]
    for j in range(1, n-1):
        ans = max(ans, (pre_max - nums[j]) * suf_max[j+1])
        pre_max = max(pre_max, nums[j])
    return ans
    # ans = max_diff = pre_max = 0
    # for x in nums:
    #     ans = max(ans, max_diff * x)
    #     max_diff = max(max_diff, pre_max - x)
    #     pre_max = max(pre_max, x)
    # return ans


# 456. 132 模式
def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    left_min = nums[0]
    right_all = SortedList(nums[2:])
    for j in range(1, n-1):
        if left_min < nums[j]:
            index = right_all.bisect_right(left_min)
            if index < len(right_all) and right_all[index] < nums[j]:
                return True
        left_min = min(left_min, nums[j])
        right_all.remove(nums[j+1])
    return False
    # stack = []
    # two = -inf
    # for x in reversed(nums):
    #     if x < two:
    #         return True
    #     while stack and stack[-1] < x:
    #         two = stack.pop()
    #     stack.append(x)
    # return False


# 3067. 在带权树网络中统计可连接服务器对数目 1909
def countPairsOfConnectableServers(edges: List[List[int]], signalSpeed: int) -> List[int]:
    n = len(edges) + 1
    g = [[] for _ in range(n)]
    for x, y, wt in edges:
        g[x].append((y, wt))
        g[y].append((x, wt))

    def dfs(x: int, fa: int, s: int) -> int:
        cnt = 0 if s % signalSpeed else 1
        for y, wt in g[x]:
            if y != fa:
                cnt += dfs(y, x, s + wt)
        return cnt

    ans = [0] * n
    for i, gi in enumerate(g):
        if len(gi) == 1:
            continue
        s = 0
        for y, wt in gi:
            cnt = dfs(y, i, wt)
            ans[i] += cnt * s
            s += cnt
    return ans
    # @cache
    # def dfs(x: int, fa: int, s: int) -> int:
    #     cnt = 0 if s else 1
    #     for y, wt in g[x]:
    #         if y != fa:
    #             cnt += dfs(y, x, (s + wt) % signalSpeed)
    #     return cnt
    #
    # ans = [0] * n
    # for i, gi in enumerate(g):
    #     if len(gi) == 1:
    #         continue
    #     s = 0
    #     for y, wt in gi:
    #         cnt = dfs(y, i, wt % signalSpeed)
    #         ans[i] += cnt * s
    #         s += cnt
    # return ans


# 1534. 统计好三元组 做到 O(n 2)
# 3455. 最短匹配子字符串 2303
# 2242. 节点序列的最大得分 2304
# 2867. 统计树中的合法路径数目 2428
# 2552. 统计上升四元组 2433 做法不止一种
# 3257. 放三个车的价值之和最大 II 2553
# 3073. 最大递增三元组（会员题）

""" §0.3 遍历对角线 =======================================================================================
"""
# 3446. 按对角线进行矩阵排序 1373
# 2711. 对角线上不同值的数量差 1429
# 1329. 将矩阵按对角线排序 1548
# 498. 对角线遍历
# 面试题 17.23. 最大黑方阵 做到 O(n 2logn)，难度约 2800
# 562. 矩阵中最长的连续1线段（会员题）

# 思维扩展：=======================================================================
# 1424. 对角线遍历 II 1780

