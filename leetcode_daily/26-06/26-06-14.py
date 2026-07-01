""" 2130. 链表最大孪生和
在一个大小为 n 且 n 为 偶数 的链表中，对于 0 <= i <= (n / 2) - 1 的 i ，第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。
比方说，n = 4 那么节点 0 是节点 3 的孪生节点，节点 1 是节点 2 的孪生节点。这是长度为 n = 4 的链表中所有的孪生节点。
孪生和 定义为一个节点和它孪生节点两者值之和。
给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 。

示例 1：输入：head = [5,4,2,1];  输出：6
解释：节点 0 和节点 1 分别是节点 3 和 2 的孪生节点。孪生和都为 6 。链表中没有其他孪生节点。所以，链表的最大孪生和是 6 。

示例 2：输入：head = [4,2,2,3];  输出：7
解释：链表中的孪生节点为：
- 节点 0 是节点 3 的孪生节点，孪生和为 4 + 3 = 7 。
- 节点 1 是节点 2 的孪生节点，孪生和为 2 + 2 = 4 。
所以，最大孪生和为 max(7, 4) = 7 。

示例 3：输入：head = [1,100000];  输出：100001
解释：链表中只有一对孪生节点，孪生和为 1 + 100000 = 100001 。

提示：链表的节点数目是 [2, 10^5] 中的 偶数 。
1 <= Node.val <= 10^5
=========================================================================================

题解路径：. / leetcode_daily_stories / 26-06-14.md

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def pairSum(self, head: Optional[ListNode]) -> int:
        # mid_node = self.middleNode(head)
        # second_head = self.reverseList(mid_node)
        # max_sum = 0
        # while second_head:
        #     max_sum = max(max_sum, head.val + second_head.val)
        #     head = head.next
        #     second_head = second_head.next
        # return max_sum
        ans = 0
        left = head

        def dfs(right: Optional[ListNode]) -> None:
            if right.next:
                dfs(right.next)
            nonlocal ans, left
            ans = max(ans, left.val + right.val)
            left = left.next

        dfs(head)
        return ans


if __name__ == '__main__':
    head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    print(Solution().pairSum(head))
    head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    print(Solution().pairSum(head))
