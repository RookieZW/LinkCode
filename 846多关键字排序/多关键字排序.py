'''
给定 n 个学生的学号(从 1 到 n 编号)以及他们的考试成绩，表示为(学号，考试成绩)，请将这些学生按考试成绩降序排序，若考试成绩相同，则按学号升序排序。

样例
样例1

输入: array = [[2,50],[1,50],[3,100]]
输出: [[3,100],[1,50],[2,50]]
样例2

输入: array = [[2,50],[1,50],[3,50]]
输出: [[1,50],[2,50],[3,50]]
'''
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        res=[]
        array.sort(key=lambda x: x[0])
        array.sort(key=lambda x: x[1], reverse=True)
        return array
#思路
#先排次关键字
#再排主关键字
#那要是有三个关键字咋个办呢？？？？？
#不得不说 lamba太棒了