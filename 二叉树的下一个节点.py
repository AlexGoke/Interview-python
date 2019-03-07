'''
题目：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

'''
思路：
大致分为两种节点：有右子节点的，无右子节点的。
有右子节点的，根据中序遍历的顺序，它一定是某子树的根节点，所以下一节点就是其右子节点的最左子节点；

无右子节点的，先考虑是其父节点的左子节点还是右子节点。
若是其父节点的左子节点，那么下一节点就是其父节点。
若是其父节点的右子节点，情况较复杂。。。

复杂情况的节点：如果一个节点既没有右子树，并且它还是它父节点的右子节点。
可以沿着它的父节点一直向上遍历，直到找到一个节点——是其父节点的左子节点，如果这样的情况存在，那么该节点的父节点就是下一节点。
'''

# 注意：“树中的节点同时包含了指向父节点的指针”——Node.next -> Node.parernt

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return 
        #先考虑有右子节点的
        if pNode.right != None:
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        #再考虑无右子节点的
        elif pNode.next != None:    #有父节点的， 
            while pNode.next != None and pNode == pNode.next.right:    #这句前后顺序不可倒
                pNode = pNode.next
            pNode = pNode.next
            return pNode
        else: 
            return pNode.next
