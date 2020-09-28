'''
描述
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。
'''
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def factorial(self, n):
        if n == 0:
            return 0
        count = 1
        while n >= 1:
            count *= n
            n -= 1
        return count
        
    def permutationIndex(self, A):
        # write your code here
        A_len = len(A)  #记录数据
        B = sorted(A)    #排序
        
        i = 0
        count = 0
        while len(B) > 0:
            index = B.index(A[i])
            print(index)
            count += index * self.factorial(len(B) - 1)
            B.remove(A[i])
            i+=1
        return count+1
#思路
#记住全排列的计算    n！
# 判断一个数前面有几个数(n)  出现了几个了(m)
# 然后计算每一位数  (n-m)*j!   还剩几维（j）
# 求和   最后补充+1  因为之前计算此排列之前多少个