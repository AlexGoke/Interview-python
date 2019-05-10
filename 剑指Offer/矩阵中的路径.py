'''
题目：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''
思路：
(参考书内容)
'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        boolmatrix = [0] * (rows * cols)
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmatrix):
                    return True
        return False
    
    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, boolmatrix ):
        if len(path) == pathLength:
            return True
        
        hasNextPath = False
        if ( row >= 0 and row < rows and col >= 0 and col < cols and 
            matrix[row*cols + col] == path[pathLength] and not boolmatrix[row*cols + col] ):
            pathLength += 1
            boolmatrix[row*cols + col] = True
            #进行该值的上下左右的递归(周围是否存在下一个路径点)
            hasNextPath = (self.hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, boolmatrix) 
                      or self.hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, boolmatrix) 
                      or self.hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, boolmatrix) 
                      or self.hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, boolmatrix))
            #对标记矩阵进行布尔值标记
            if not hasNextPath:    #说明周围4个点都存在下一路径
                pathLength -= 1    #回到前一个字符
                boolmatrix[row*cols + col] = False    #将该点重新设为未标记
        return hasNextPath
