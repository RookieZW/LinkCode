'''
给出一个字符串，找出第一个只出现一次的字符。

样例
样例 1:
	输入: "abaccdeff"
	输出:  'b'
	
	解释:
	'b' 是第一个出现一次的字符


样例 2:
	输入: "aabccd"
	输出:  'b'
	
	解释:
	'b' 是第一个出现一次的字符
'''
import re
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        str_l = list(str)
        str_l.sort()
        i = 0
        while i < len(str_l):
            pattern = re.compile(str_l[i])
            l = pattern.findall(str)
            if len(l) == 1:
                return str_l[i]
            i+=len(l)
        return '0'
#思路
#使用正则表达时查找每个字符的个数（我太菜了）