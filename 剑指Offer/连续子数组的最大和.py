'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和(子向量的长度至少是1)
'''

#解法一：利用数组的规律
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        input_invalid = False
        if array is None or len(array) <= 0:
            input_invalid = True
            return 0
        cursum = 0
        greatsum = array[0]
        for i in array:
            if cursum < 0:
                cursum = i
            else:
                cursum += i
            if cursum > greatsum:
                greatsum = cursum
        return greatsum

#解法二：动态规划
#递归写法
    def rec_DP(self, array):
        input_invalid = False
        if array is None or len(array) <= 0:
            input_invalid = True
            return 0
        alist = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or alist[i-1] <= 0:
                alist[i] = array[i]
            else:
                alist[i] = alist[i-1]+array[i]
        return max(alist)


s = solution()
arr1 = [1, -2, 3, 10, -4, 7, 2, -5]
arr2 = [-2,-8,-1,-5,-9]
print(s.FindGreatestSumOfSubArray(arr1))
print(s.FindGreatestSumOfSubArray(arr2))
print(s.rec_DP(arr1))
print(s.rec_DP(arr1))