'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印'，
其他行以此类推。
'''

'''
按之字形顺序打印二叉树需要两个栈。
我们在打印某一行节点时，拔下一层的子节点保存到相应的栈里。
如果当前打印的奇数层，则先保存左子节点再保存右子节点到第一个栈里；
如果当前打印的是偶数层，则先保存右子节点再保存左子节点到第二个栈里。
(判断奇偶数，用一个bool值就可以)
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        LeftToRight = True    #从左向右
        while nodes:
            curStack, nextStack = [], []
            if LeftToRight:    #从左到右
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:    #从右到左
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()    #反转，起到栈的效果，先读出来后进入的
            LeftToRight = not LeftToRight    #变换方向
            result.append(curStack)
            nodes = nextStack 
        return result