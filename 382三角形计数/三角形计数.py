'''
给定一个整数数组，在该数组中，寻找三个数，分别代表三角形三条边的长度，问，可以寻找到多少组这样的三个数来组成三角形？

样例
样例 1:

输入: [3, 4, 6, 7]
输出: 3
解释:
可以组成的是 (3, 4, 6), 
           (3, 6, 7),
           (4, 6, 7)
样例 2:

输入: [4, 4, 4, 4]
输出: 4
解释:
任何三个数都可以构成三角形
所以答案为 C(3, 4) = 4
'''
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S_len = len(S)
        count = 0
        if not S or S_len < 3:
            return 0
        S.sort()
        for i in range(2, S_len):
            longest = S[i]
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] > longest:
                    count += right - left
                    right -= 1
                if S[left] + S[right] <= longest:
                    left += 1
                    
        return count
'''
此处用到了快排的思想
    时间复杂度 O（n^2）
'''