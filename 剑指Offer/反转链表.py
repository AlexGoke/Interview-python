'''
输入一个链表，反转链表后，输出新链表的表头。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
		
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pReversedHead = None
        pNode = pHead
        pPre = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode
            pNode.next = pPre
            
            pPre = pNode
            pNode = pNext
        return pReversedHead