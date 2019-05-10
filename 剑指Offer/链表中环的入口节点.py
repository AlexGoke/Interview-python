'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
		
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None
			
        # 得到环中节点的数目
        nodesInLoop = 1
        FlagNode = meetingNode
        while FlagNode.next != meetingNode:
            FlagNode = FlagNode.next
            nodesInLoop += 1
			
        # 先移动pNode1,先走环中节点的数目
        pNode1 = pHead
        for i in range(nodesInLoop):
            pNode1 = pNode1.next
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1
        
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        pSlow = pHead.next
        if not pSlow:
            return None
        pFast = pSlow.next
        while pFast and pSlow:
            if pFast is pSlow:
                return pFast
            pSlow = pSlow.next    # 漫指针每次走一步
            pFast = pFast.next    # 快指针每次走两步
            if pFast:
                pFast = pFast.next
        return None
		
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node4

s = Solution()
print(s.EntryNodeOfLoop(node1).val)    #设计的环入口是节点4，其值返回也应该是4.