'''
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例
样例 1:

输入: source = "source" ， target = "target"
输出:-1   
样例解释: 如果source里没有包含target的内容，返回-1
'''

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def getNext(self, target):
        next = [-1]
        j = 0
        k = -1
        while len(target)>j:
            if j == -1 or target[j] == target[k]:
                k+=1
                j+=1
                next.append(k)
            else:
                j = next[j]
        return next
            
    def strStr(self, source, target):
        # Write your code here
        next = self.getNext(target)
        i = 0
        j = 0
        while i < len(source) and j < len(target):
            if j == -1 or source[i] == target[j]:
                j+=1
                i+=1
            else:
                j = next[j]
        if j == len(target):
            return i - j
        else:
            return -1


#解题思路
#KMP算法
#计算next数组（重点）
#https://v.qq.com/x/page/r086243vwn1.html