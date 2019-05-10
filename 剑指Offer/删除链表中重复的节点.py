'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        preNode = ListNode(None)
        preNode.next = pHead    #自己加的头节点
        head = preNode    #最终返回的是哑节点的下一个，真正的头节点。head.next
        flag = False
        while pHead and pHead.next:
            pNext = pHead.next
            if pHead.val == pNext.val:    #先删掉pNext
                flag = True
                pHead.next = pNext.next
                pNext.next = None     #断开pNext的与pNext.next的连接
            elif flag == True:                   #再把pHead给删掉
                preNode.next = pHead.next
                pHead = pHead.next    #pHead移动到下一个节点等待检测
                flag = False
            else:    #不需要删除节点
                preNode = pHead
                pHead = pHead.next
        if flag:
            preNode.next = None
        return head.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)    #1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.deleteDuplication(node1).next.next.val)    #打印第三个节点值，预计是5