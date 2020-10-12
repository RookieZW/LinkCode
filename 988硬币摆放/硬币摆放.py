'''
你有 n 枚硬币，想要摆放成阶梯形状，即第 k 行恰好有 k 枚硬币。

给出 n，找到可以形成的完整楼梯行数。

n 是一个非负整数，且在32位有符号整数范围内。

样例
样例 1:

输入：n = 5
输出：2
解释：
硬币可以形成以下行：
¤
¤ ¤
¤ ¤
因为第3行不完整，我们返回2。
样例 2:

输入：n = 8
输出：3
解释：
硬币可以形成以下行：
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第4行不完整，我们返回3。

'''

class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        count = 0
        i = 1
        while True:
            if n >= i:
                count += 1
                n -= i
                i += 1
            else:
                return count
'''
本质为 1+2+3求和
'''