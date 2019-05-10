'''
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''

'''
思路1：
哈希表，从头到尾扫描，每扫描到一个数字，都可以用O(1)的时间来判断哈希表里是否已经包含这个数字。
如果已经包含，就找到一个重复的数字。时间复杂度O(n), 空间复杂度O(n)。
'''

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):

        if not numbers:
            return False
        
        nums = []    #用一个数组做哈希表
        for i in numbers:
            if i in nums:
                duplication[0] = i
                return True
            nums.append(i)
        return False

		
'''
思路2：
因为数组中的数字都是0~n-1的范围内，如果其中没有重复数字的话，那么排序后数字i将出现在下标为i的位置。
重排数组，从头到尾扫描，当扫描到下标i的数字时，首先比较该数字（m）是否等于i。若是，继续扫描下一个；若不是，则拿它和下标为m的数字作比较。
如果它和第m个数字相等，就找到一个重复数字；如果不相等，就把第i个和第m个数字交换，	把数字m放到属于它的位置上。

时间复杂度是O(n), 空间复杂度是O(1)
'''

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        
        if not numbers:
            return False
            
        length = len(numbers)
        for i in range(length):
            while numbers[i] != i:
                temp = numbers[i]
                if numbers[i] == numbers[temp]:
                    duplication[0] = numbers[i]
                    return True
                numbers[i] = numbers[temp]
                numbers[temp] = temp;
        return False
