'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# -*- coding:utf-8 -*-
class Solution:

    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变，用sorted排序
    def reOrderArray(self, array):
        # write code here
        if len(array) < 1:
            return []
        pBegin = 0
        pEnd = len(array)-1
        while pBegin < pEnd:
            while (array[pBegin] & 0x1 == 1):    #奇数
                pBegin += 1
            while (array[pEnd] & 0x1 == 0):    #偶数
                pEnd -= 1
            if pBegin < pEnd:
                temp = array[pBegin]
                array[pBegin] = array[pEnd]
                array[pEnd] = temp
        return sorted(array[:pBegin])+sorted(array[pBegin:])

	 # 直接利用Python的trick, 写一个简单的排列数组, 顺序不变
	 def reOrderArray2(self, array):
		left = [x for x in array if x & 1]
		right = [x for x in array if not x & 1]
		return left + right
		
		
S = Solution()
# print(S.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(S.reOrderArray2([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))