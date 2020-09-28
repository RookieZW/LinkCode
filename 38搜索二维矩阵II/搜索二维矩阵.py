'''
描述
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
您在真实的面试中是否遇到过这个题？  
样例
例1:

输入:
[[3,4]]
target=3
输出:1
'''
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        count = 0
        
        m = len(matrix)      #行  
        n = len(matrix[0]) - 1 #列
        r = 0
        if m < 1:
            return 0
        while r < m and n >= 0:
            if matrix[r][n] > target:
                n -= 1
            elif matrix[r][n] < target:
                r += 1
            else:
                count += 1
                if n >= 0:
                    n -= 1 
                elif r < m: 
                    r += 1
                else:
                    break
        return count
#思路：
#暴力搜索
#从右上角开始查找
#若大于 target  列前移
#若小于target   行后移
#否则：
#	计数+1
#	行列符合条件的移动