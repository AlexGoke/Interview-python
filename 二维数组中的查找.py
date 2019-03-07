'''
题目：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
从右上角/左下角开始搜索，每次可排除一列。
'''

#从右上角
class Solution:
    
    def Find(self, target, array):
    
        row = len(array)    #行数
        col = len(array[0])    #列数
        i = 0
        j = col-1    #i，j为右上角的行列值
        while i < row and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i+=1
            else:
                j-=1
        return False
 

#从左下角
class Solution:
    
    def Find(self, target, array):
       
        row = len(array)
        col = len(array[0])
        i = row-1 
        j = 0    #左下角数字的行列值
        while i >= 0 and j < col:
            if array[i][j] == target:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1
        return False
