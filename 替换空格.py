'''
题目：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
思路：
首先要明白：特殊字符的转换原理（题目已经告诉）

C/C#中	每个字符串都以’\0’结尾，实际长度就是比字符数多一个字节

因此字符串会变长，所以两种办法：
1.在原来字符串上进行替换，就有可能覆盖修改该字符串后面的内存
2.创建新的字符串进行替换，需要更多的内存
'''

#在新的字符串上替换：
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
       
        new_s = ''
        for j in s:
            if j == ' ':
                new_s=new_s + '%20'
            else:
                new_s=new_s + j
        return new_s

		
#偷懒的方法：
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace( ' ', '%20')
