'''
描述
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            i = 3
            a = 1
            b = 2
            res = 0
            while i <= n:
                res = a + b
                a = b
                b = res
                i+=1
            return res
#思路
#爬楼梯这个公司很像斐波那契数列的式子
#楼层数        方法数
#1				1
#2				2
#3				3
#4				5
#F(n) = F(n-1)+F(n-2)