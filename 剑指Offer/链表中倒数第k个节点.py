'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        pAhead = head
        pBehind = ListNode(None)
        while k>1:
            if pAhead.next is not None:
                pAhead = pAhead.next
            else:
                return None
            k -= 1
        
        pBehind = head
        while pAhead.next is not None:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node1.next = node2
node2.next = node3
		
s = Solution()
print(s.FindKthToTail(node1, 1).val)    #倒数第1个节点的值，预计是12