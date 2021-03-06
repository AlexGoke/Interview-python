'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
'''
利用二叉树前序遍历和中序遍历的特性。
前序遍历的第一个值一定为根节点，对应于中序遍历中间的一个点。
在中序遍历序列中，这个点左侧的均为根的左子树，这个点右侧的均为根的右子树。
这时可以利用递归，分别取前序遍历[1:i+1]和中序遍历的[:i]对应与左子树继续上一个过程，
取前序遍历[i+1:]和中序遍历[i+1]对应于右子树继续上一个过程，最终得以重建二叉树。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        
        #找到根节点在中序遍历中的位置index，前面就是左子树，后面就是右子树
        #val = tin.index(pre[0])    利用库函数
        for i in range(len(tin)):
            if pre[0] == tin[i]:
                index = i
                break
                
        root.left = self.reConstructBinaryTree(pre[1:index+1],tin[0:index])
        root.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
        return root
