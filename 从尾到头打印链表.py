'''
题目：
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

'''
思路1：（用库函数）
使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表list

对list切片，只用一个" : "表示从头到尾，切片操作第三个参数表示每N个取一个。
[::2]每两个取一个，[::-1]逆序。

这个方法效率应该还可以，先存入vector，再反转vector
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        result = []
        while listNode.next is not None:
            result.extend(listNode.val)
            listNode = listNode.next
        result.extend(listNode.val)
        
        return result[ : : -1]

		
	
'''	
思路2：
书本思路，利用栈，后进先出。

但因为python是一个很上层的语言，封装了内存管理，程序员无需知道堆、栈这些东西。他们的内存管理都由垃圾回收器自动管理。
'''