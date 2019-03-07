'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 n<=39
'''

'''
思路1：
最普通的递归解法，虽然简洁，但是效率很低。因为里面有大量的重复运算，不实用。
'''

    def Fibonacci(self, n):
        # write code here
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

'''
思路2：
因为递归重复计算太多，避免重复计算，把已经得到的数列中间项保存起来。
'''

class Solution:
    def Fibonacci(self, n):
        # write code here
        num1 = 0
        num2 = 1
        if n == 0:
            return 0
        elif n == 1: 
            return 1
        for i in range(2, n+1):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return temp

		
class Solution:
    def Fibonacci(self,n):
        # write code here
        arr = [0,1]
        while len(arr) <= n:
            arr.append( arr[-1]+arr[-2] )
        return arr[n]
