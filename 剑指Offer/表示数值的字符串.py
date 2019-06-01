'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) <= 0:
            return False
        #分别标记是否已经出现过正负号、小数点、e。因为这几个需要特殊考虑
        has_sign = False
        has_point = False
        has_e = False
        for i in range(len(s)):
            # e的情况：
            # 1.不能出现两个e；
            # 2.e不能出现在最后面
            if s[i] == 'e' or s[i] == 'E':
                if has_e:
                    return False
                else:
                    has_e = True
                    if i == len(s)-1:
                        return False
            
            # 符号位的情况：
            # 1.如果前面出现过符号位，那么这个符号位一定是在e后面
            # 2.如果这是第一次出现符号位，而且这个位置不是第一位，那么只能是e后面
            elif s[i] == '+' or s[i] == '-':
                if has_sign:
                    if s[i-1] != 'e' and s[i-1] != 'E':
                        return False
                else:
                    has_sign = True
                    if i > 0 and s[i-1]!='e' and s[i-1]!='E':
                        return False
                        
            # 小数点的情况：
            # 1. 小数点不能出现两次；而且已经出现过e了，那么就不能再出现小数点了，因为e后面只能是整数
            # 2. 如果是第一次出现小数点，但如果前面出现过e，那么还是不能出现小数点
            elif s[i] == '.':
                if has_point or has_e:
                    return False
                else:    # 这里都是前面没有出现过小数点和e的情况
                    has_point = True
                    #if i > 0 and ( s[i-1] == 'e' or s[i-1] == 'E' ):
                    #    return False
            # 其他字符必须都是’0‘到’9‘之间
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True

s = Solution()
# True正案例
print(s.isNumeric('+100'))
print(s.isNumeric('5e2'))
print(s.isNumeric('-123'))
print(s.isNumeric('3.1416'))
print(s.isNumeric('-1E-16'))    
# False案例
print(s.isNumeric('12e'))
print(s.isNumeric('1a3.14'))
print(s.isNumeric('1.2.3'))    # 有问题，关乎小数点
print(s.isNumeric('+-5'))
print(s.isNumeric('12e+4.3'))

