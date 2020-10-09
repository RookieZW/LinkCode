'''
给出一个字符串，以 字符在串中出现的次数 为第一关键字，字典序为第二关键字排序字符串。

样例
样例1

输入: str = "bloomberg"
输出: "bbooeglmr"
解释:
'b'和'o'出现次数最多，但是'b'字典序较小，排名第一，其次是'o'，以此类推.
样例2

输入: str = "lintcode"
输出: "cdeilnot"
解释:
所有字符出现次数一样多，所以直接按照字典序排序。
注意事项
字符串长度小于10000
所有字符均为小写
'''
class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        # Write your code here
        str_list = list(str)
        str_list.sort()
        set_list = list(set(str_list))
        set_list.sort()
        set_len = len(set_list)
        set_num = [0] * set_len
        
        res_list = []
        
        list_len = len(str_list)

        for s in str_list:
            set_num[set_list.index(s)] += 1
        res = ""
        i= 0
        while i < set_len:
            num = max(set_num)
            index = set_num.index(num)
            set_num[index] = -1
            res += (set_list[index]*num)
            i += 1
        return res
'''
先排序  保证字典排序  然后按照次数拼接
'''
