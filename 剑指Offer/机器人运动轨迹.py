'''
题目：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

'''
思路：
同矩阵中的路径一样，只是判断条件变为了：进入的各自行列坐标和不能大于给定值。
'''

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visitmatrix = [0] * (rows * cols)    #标记矩阵
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visitmatrix)
        return count
        
    def movingCountCore(self, threshold, rows, cols, row, col, visitmatrix):
        count = 0
        if self.check(threshold, rows, cols, row, col, visitmatrix):
            visitmatrix[row * cols + col] = True
            count = ( 1 + self.movingCountCore(threshold, rows, cols, row-1, col, visitmatrix)
                        + self.movingCountCore(threshold, rows, cols, row, col+1, visitmatrix)
                        + self.movingCountCore(threshold, rows, cols, row+1, col, visitmatrix)
                        + self.movingCountCore(threshold, rows, cols, row, col-1, visitmatrix))
        return count
    
    def check(self, threshold, rows, cols, row, col, visitmatrix):
        if (row >= 0 and row < rows and col >= 0 and col < cols and
            self.getDigitSum(row) + self.getDigitSum(col) <= threshold and
             not visitmatrix[row * cols + col] ):
            return True
        return False
    
    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10    #先个位，然后十位。。。
            number /= 10    #从个位不断往前走，个位，十位。。。
        return sum
