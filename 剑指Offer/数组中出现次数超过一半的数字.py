'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:

        #基于划分Partition函数的O(n)算法
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0
        
        middle = length>>1
        #print( "middle is : "+ str(middle))
        start = 0
        end = length-1
        index = self.Partition(numbers, start, end)    #快排中的分区
        while index != middle:
            if index > middle:
                end = index-1
                index = self.Partition(numbers, start, end)
            elif index < middle:
                start = index+1
                index = self.Partition(numbers, start, end)
        
        #print("index is : " + str(index))
        result = numbers[middle]    #
        #print("result is :" + str(result))
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
		
		
    #返回数组中位数的序号, 划分算法   
    def Partition(self, arr, left, right):
        length = len(arr)	
        if arr == None or length <= 0 or left < 0 or right >= length:
            return None
        if left == right:
            return right
			
        pivot = arr[left]
        i = left
        j = right
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot
        return i
		
	#检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid
	
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in numbers:
            if i == number:
                times += 1
        isMoreThanHalf = True
        if times * 2 <= length:
            isMoreThanHalf = False
        return isMoreThanHalf

#-------------------------------以上是基于 划分 的方法寻找------------------------------------#

    #根据数组特点找出O(n)的算法
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if self.CheckInvalidArray(numbers, length):
            return 0
        result = numbers[0]
        times = 1
        for i in numbers:
            if times == 0:
                result = i
                times = 1
            elif i == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

s = Solution()

#print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
#print(s.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))

#print(s.MoreThanHalfNum([1,2,3,2,2,2,5,4,2]))
print(s.MoreThanHalfNum([1,2,3,2,4,2,5,2,3]))