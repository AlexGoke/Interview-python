'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    
     # 使用冒泡排序
    def PrintMinNumber1(self, numbers):
        # write code here
        if not numbers:
            return ''        
        str_num = [str(m) for m in numbers ]    
        for i in range( len(numbers)-1 ):
            for j in range( i+1, len(numbers) ):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    str_num[i], str_num[j] = str_num[j], str_num[i]
        return ''.join(str_num)
    
    #正则表达式
    def PrintMinNumber2(self, numbers):
        # write code here
        if numbers == None or len(numbers) <= 0:
            return ''
        strList = []
        for i in numbers:
            strList.append( str(i) )
        #key是一种比较规则
        #比较x+y和x-y的大小，因为是string，需要先转换成int
        key = cmp_to_key(lambda x,y: int(x+y)-int(y+x) )
        strList.sort(key = key)
        return ''.join(strList)
        
s = Solution()
numbers = [3, 32, 321]
result1 = s.PrintMinNumber1(numbers)
result2 = s.PrintMinNumber2(numbers)
print(result)