'''
实现一个算法确定字符串中的字符是否均唯一出现

样例
样例 1:

输入:  "abc_____"
输出:  false
样例 2:

输入:  "abc"
输出:  true   
挑战
如果不使用额外的存储空间，你的算法该如何改变？
'''

class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        for i in range(len(str)):
            if str.find(str[i], i+1) != -1:
                return False
        return True

#思路：
#
#查找字符串中该位置后是否还有该字符出现（目前没有啥好想法 以后补充  太菜了）