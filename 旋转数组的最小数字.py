'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
思路：
这一题也不好解，在算法上，考虑数字没有重复的情况的话，使用二分法，有两个指针，第一个指针指向front，第二个指针指向rear，
midIndex是中间数字，只要是旋转数组，那么首位一定大于中间位，所以如果首位大于中间位的话，那么就把指针从首位移到中间
位，前面数字向后移动，不断迭代，当首位和最后位只差1时，最后维就是最小值。此时最坏时间复杂度是O(logn),但是要考虑数字
重复的话，情况只可能是首位和末尾和中间重这种[1,0,1,1]只能取其中最小值，逐一排列，对于首位和中间位重的，比如[1,1,0],
把首位移动到后面去，可以处理，或者中间位和末尾重，比如[1,0,0]，也是能处理，其他情况不存在，因为前提要求是旋转数组
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        index1, index2 = 0, len(rotateArray)-1
        indexMid = index1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index1+index2)//2
            if rotateArray[index1] == rotateArray[indexMid] and rotateArray[index1] == rotateArray[index2]:
                return self.minOrder(rotateArray, index1, index2)
            
            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid
            elif rotateArray[indexMid] <= rotateArray[index2]:
                index2 = indexMid
        return rotateArray[indexMid]
    
    def minOrder(self, array, front, end):
        result = array[front]
        for i in (front+1, end+1):
            if result > array[i]:
                result = array[i]
        return result
