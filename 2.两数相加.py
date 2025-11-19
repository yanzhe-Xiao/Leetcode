# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode(0)
        current = r
        c = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            add = val1 + val2 + c
            c = add // 10
            add = add % 10
            current.next = ListNode(add)
            current = current.next

            # 移动到下一个节点
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 处理最后的进位
        if c > 0:
            current.next = ListNode(c)
        return r.next
            
# @lc code=end

