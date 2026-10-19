""" 1569. 将子数组重新排序得到同一个二叉搜索树的方案数    困难
给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉搜索树（BST）。
请你统计将 nums 重新排序后，统计满足如下条件的方案数：重排后得到的二叉搜索树与 nums 原本数字顺序得到的二叉搜索树相同。
比方说，给你 nums = [2,1,3]，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。
数组 [2,3,1] 也能得到相同的 BST，但 [3,2,1] 会得到一棵不同的 BST 。
请你返回重排 nums 后，与原数组 nums 得到相同二叉搜索树的方案数。
由于答案可能会很大，请将结果对 109 + 7 取余数。

示例 1：输入：nums = [2,1,3];     输出：1
解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。
示例 2：输入：nums = [3,4,5,1,2];     输出：5
解释：下面 5 个数组会得到相同的 BST：[3,1,2,4,5];[3,1,4,2,5];[3,1,4,5,2];[3,4,1,2,5];[3,4,1,5,2]
示例 3：输入：nums = [1,2,3];     输出：0
解释：没有别的排列顺序能得到相同的 BST 。

提示：
1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
nums 中所有数 互不相同 。

"""
import sys
from typing import List

MOD = 10 ** 9 + 7


def numOfWays(nums: List[int]) -> int:
    n = len(nums)
    sys.setrecursionlimit(n + 100)      # 最坏链状树，递归深度 = n

    # 组合数预处理：阶乘 + 费马小定理逆元，O(n) 空间
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)    # 费马小定理求 (n!)⁻¹
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(a: int, b: int) -> int:    # C(a, b)
        return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

    def ways(arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1
        root = arr[0]
        left = [x for x in arr if x < root]     # 保持原相对顺序
        right = [x for x in arr if x > root]
        # 根第一；左右两拨随便交错：l+r 个空位挑 l 个给左子树，其余归右
        return comb(len(left) + len(right), len(left)) * ways(left) % MOD * ways(right) % MOD

    return (ways(nums) - 1) % MOD       # 减去原排列本身


if __name__ == '__main__':
    print(numOfWays([2, 1, 3]))         # 1
    print(numOfWays([3, 4, 5, 1, 2]))   # 5
    print(numOfWays([1, 2, 3]))         # 0










