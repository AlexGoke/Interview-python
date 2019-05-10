'''
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4,。
'''

# -*- coding:utf-8 -*-
class Solution:

    # O(n)的算法, 只有当我们可以修改输入的数组时可用
    # 基于Partition的方法
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if tinput is None or length <= 0 or k <= 0:
            return []
        start = 0
        end = length - 1
        index = self.Partition(tinput, start, end)
        while index != k-1:
            if index > k-1:
                end = index-1 
                index = self.Partition(tinput, start, end)
            else:
                start = index+1
                index = self.Partition(tinput, start, end)
        output = tinput[:k]
        output.sort()
        return output
            
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
		
    # O(nlogk)的算法, 适合海量数据
    # 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
    def GetLeastNumbers(self, tinput, k):
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        output = []
        for number in tinput:    # k容量的容器
            if len(output) < k:
                output.append(number)
            else:
			    # 构造最小堆， 不推荐
                # output = heapq.nsmallest(k, output)
                # if number >= output[-1]:
                #     continue
                # else:
                #     output[-1] = number
			    
				#构造最大堆
                output = heapq.nlargest(k, output)    #返回列表中的n个最大值和最小值
                if number >= output[0]:    #output[0]根节点，即最大值
                    continue
                else:
                    output[0] = number

        return output[::-1]  

		
tinput = [4,5,1,6,2,7,3,8]
s = Solution()
#print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers(tinput, 4))
#print(s.GetLeastNumbers(tinput, 5))