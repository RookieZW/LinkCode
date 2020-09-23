'''
给出 2 * n + 1个数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例
样例 1:

输入：[1,1,2,2,3,4,4]
输出：3
解释：
仅3出现一次
'''


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        assert(len(A)>0)
        A.sort()
        flag = A[0]
        if (len(A) == 1):
            return A[0]
        else:
            count = 0
            for i in range(len(A)):
                if flag == A[i]:
                    if i == 0:
                        continue
                    count+=1
                else:
                    if count != 0:
                        flag = A[i]
                        count=0
                    else:
                        return flag
            return flag

#思路
#首先排序，降低难度
#遍历  两个记录量
#一个记录出现次数
#一个记录新出现的数值
#若该值下一个数与其不相等，该值为落单的数