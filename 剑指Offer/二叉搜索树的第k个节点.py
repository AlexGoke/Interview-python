'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
'''
'''
中序遍历输出一个序列，然后找到序列中第k个数即可。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None
        curStack = []
        nodeStack = []
        pNode = pRoot
        while pNode or len(nodeStack):
            #任何一个节点，都先走到左子树最远端
            while pNode:
                nodeStack.append(pNode)
                pNode = pNode.left
            if len(nodeStack):
                pNode = nodeStack.pop()
                curStack.append(pNode)
                pNode = pNode.right
        if k > len(curStack):
            return None
        return curStack[k-1]
        