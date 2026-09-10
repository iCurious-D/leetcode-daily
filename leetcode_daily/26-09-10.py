""" 2265. 统计值等于子树平均值的节点数    中等
给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。
注意：n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。
root 的 子树 由 root 和它的所有后代组成。

示例 1：输入：root = [4,8,5,0,1,null,6];      输出：5
解释：对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。
对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。
对值为 0 的节点：子树的平均值 0 / 1 = 0 。
对值为 1 的节点：子树的平均值 1 / 1 = 1 。
对值为 6 的节点：子树的平均值 6 / 1 = 6 。
示例 2：输入：root = [1];     输出：1
解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。

提示：
树中节点数目在范围 [1, 1000] 内
0 <= Node.val <= 1000

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfSubtree(root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(node: TreeNode) -> (int, int):
        nonlocal ans
        if not node:
            return 0, 0
        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)
        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1
        avg = total_sum // total_count
        if node.val == avg:
            ans += 1
        return total_sum, total_count

    dfs(root)
    return ans


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)
    print(averageOfSubtree(root))


