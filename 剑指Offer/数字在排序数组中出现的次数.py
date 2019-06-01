'''
统计一个数字在排序数组中出现的次数。
'''

'''
二分查找的扩展。可以构造两个函数。第一个函数查找目标数字出现的最前面的位置，
先使用二分查找找到该数字，如果该数字的index > 0而且该数字前面一个数字等于k的话，那么就令end=middle-1，
继续二分查找。对于第二个函数，查找目标数字出现的最后面的位置，反之编写。
最后如果数字存在的话，令走后面的index减去最前面的index然后+1即可。
在进行有序数组的元素查找，可以先尝试一下二分查找
'''

class Solution:
    def GetNumberOfK(self, data, K):
        # write code here
        if not data:
            return 0
        if self.GetFirstK(data, K) == -1 and self.GetLastK(data, K) == -1:
            return 0
        print(self.GetFirstK(data, K))
        print(self.GetLastK(data, K))
        return self.GetLastK(data, K)-self.GetFirstK(data, K) + 1
    
    def GetFirstK(self, data, K):    #二分法
        low = 0
        high = len(data)-1
        while low <= high:
            mid = (low+high)//2
            if data[mid] < K:
                low = mid+1
            elif data[mid] > K:
                high = mid-1
            else: #data[mid] = k
                if mid == low or data[mid-1] != K:    #如果mid是第一个数，或者 data[mid-1]不是K
                    return mid    #说明找到了第一个K出现的位置
                else:  #说明mid不是第一个K，前面还有，缩小范围
                    high = mid-1
        return -1

    def GetLastK(self, data, K):
        low = 0
        high = len(data)-1
        while low <= high:
            mid = (low+high)//2
            if data[mid] < K:
                low = mid+1
            elif data[mid] > K:
                high = mid-1
            else:
                if mid == high or data[mid+1] != K:    #如果mid是最后一个数，或者 data[mid+1]不是K
                    return mid    #说明找到了最后一个K出现的位置
                else:    #说明mid不是最后一个K，后面还有，缩小范围
                    low = mid+1
        return -1
        
s = Solution()
nums = [1,2,3,3,3,3,4,6]
K = 3
result = s.GetNumberOfK(nums, K)
print(result)