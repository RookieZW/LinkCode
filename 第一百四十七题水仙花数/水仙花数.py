'''
水仙花数的定义是，这个数等于他每一位数上的幂次之和 见维基百科的定义

比如一个3位的十进制整数153就是一个水仙花数。因为 153 = 13 + 53 + 33。

而一个4位的十进制数1634也是一个水仙花数，因为 1634 = 14 + 64 + 34 + 44。

给出n，找到所有的n位十进制水仙花数。

样例
样例 1:

输入: 1
输出: [0,1,2,3,4,5,6,7,8,9]
样例 2:

输入:  2
输出: []
样例解释: 没有2位数的水仙花数。
注意事项
你可以认为n小于8。
'''
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        assert(n > 0 and n < 8)
        out = []
        if n == 1:
            out.append(0)
        for i in range(10**(n-1), 10**n):
            res = 0
            k = i
            for j in range(n):
                res += (k % 10)**n
                k = k // 10
            if res == i:
                out.append(i)
        return out
### 思路
#  题目简单 注意python中的整除为//即可