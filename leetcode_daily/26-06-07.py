"""  2196. 根据描述创建二叉树
给你一个二维整数数组 descriptions ，
其中 descriptions[i] = [parenti, childi, isLefti] 表示 parenti 是 childi 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。
此外：
如果 isLefti == 1 ，那么 childi 就是 parenti 的左子节点。
如果 isLefti == 0 ，那么 childi 就是 parenti 的右子节点。
请你根据 descriptions 的描述来构造二叉树并返回其 根节点 。
测试用例会保证可以构造出 有效 的二叉树。

示例 1：输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
输出：[50,20,80,15,17,19]  解释：根节点是值为 50 的节点，因为它没有父节点。

示例 2：输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]]
输出：[1,2,null,null,3,4]  解释：根节点是值为 1 的节点，因为它没有父节点。

提示：
1 <= descriptions.length <= 10^4
descriptions[i].length == 3
1 <= parenti, childi <= 10^5
0 <= isLefti <= 1
descriptions 所描述的二叉树是一棵有效二叉树
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-07.md

"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> TreeNode:
        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)
        for x, node in nodes.items():
            if x not in children:
                return node


if __name__ == '__main__':
    print(Solution().createBinaryTree(descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
    print(Solution().createBinaryTree(descriptions = [[1,2,1],[2,3,0],[3,4,1]]))

