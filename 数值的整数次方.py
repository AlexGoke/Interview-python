'''
题目：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

'''
思路：
考虑边界值，底数若为0的时候，特殊处理。
用位运算代替乘除法，优化了效率
'''

class Solution:
    def Power(self, base, exponent):
        # write code here
        boolInvalidInput = False
        if base == 0.0 and exponent < 0:
            boolInvalidInput = True
            return 0.0
        absExponent = abs(exponent)
        result = 0.0
        result = self.PowerWithUnsignedExponent(base, absExponent)
        if exponent < 0:
            return 1/result
        else:
            return result
     
     # 基础乘除   
    def PowerWithUnsignedExponent(self, base, absExponent):
        result = 1.0
        for i in range(absExponent):
            result *= base
        return result 

		
#右移运算符代替了除以2，位于运算符代替了求余运算符（%）
    def PowerWithUnsignedExponent(self, base, exponent):
        if exponent == 0:
            return 1 
        if exponent == 1:
            return base
        result = self.PowerWithUnsignedExponent(base, exponent>>1)
        result *= result 
        if (exponent & 0x1 == 1):
            result *= base
        return result
