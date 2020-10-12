'''
假设你有一个特殊的键盘，键盘上有如下键:

键1: (A): 在屏幕上打印一个'A'。
键2: (Ctrl-A): 选择整个屏幕。
键3: (Ctrl-C): 复制选择到缓冲区。
键4: (Ctrl-V): 在屏幕上已有的内容后面追加打印缓冲区的内容。
现在，你只能按键盘上N次(使用以上四个键)，找出你可以在屏幕上打印的“A”的最大数量

样例
样例 1:

输入: 3
输出: 3
解释: A, A, A
样例 2:

输入: 7
输出: 9
解释: A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
注意事项
1 <= N <= 50
答案将在32位有符号整数的范围内。
'''

class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        dp = [0] * (N+1)
        for i in range(1, N + 1):
            dp[i] = max(dp[i], dp[i - 1] + 1)
            for j in range(i - 2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[N]
'''
动态规划问题
	转移方程：
		dp[i] = max(dp[i], dp[i]*(i-j-1))  循环找最值  j [0, i - 2]

'''