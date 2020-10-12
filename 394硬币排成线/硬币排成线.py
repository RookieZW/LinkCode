'''
有 n 个硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。拿到最后一枚硬币的人获胜。

请判定 先手玩家 必胜还是必败?

若必胜, 返回 true, 否则返回 false.

样例
样例 1:

输入: 1
输出: true
样例 2:

输入: 4
输出: true
解释: 
先手玩家第一轮拿走一个硬币, 此时还剩三个.
这时无论后手玩家拿一个还是两个, 下一次先手玩家都可以把剩下的硬币拿完.
挑战
O(1) 时间复杂度且O(1) 存储。
'''

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n % 3 == 0:
            return False
        else:
            return True
'''
这个代码肯定不是要考察的东西
就很gay   发现了一个不一样的规律
'''