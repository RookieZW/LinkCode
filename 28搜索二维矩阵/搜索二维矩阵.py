'''
写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                row = i - 1
                break

        if i == 0:
            return False
        elif i == len(matrix):
            row = i - 1
        print(i)
        for i in range(len(matrix[0])):
            if matrix[row][i] == target:
                return True
        return False
#思路：
#先确定在第几行
#遍历此行  
#需要注意的是:
#最后一层的的第一个数恰好等于target