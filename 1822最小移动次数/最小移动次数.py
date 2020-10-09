'''
给定由N个字母 'a' 和/或 'b' 组成的字符串S。 在一次操作中，可以将一个字母替换为另一个字母（'a' 替换为 'b' 或 'b' 替换为 'a'）。 返回得到不包含三个连续相同字母的字符串所需的最小操作次数。

样例
示例1:
输入:
S = "baaaaa"
输出: 1
解释：将字符串变成: "baabaa", 这样一次操作就可以使得字符串S没有三个相同的连续字母。
示例2:
输入:
S = "baaabbaabbba"
输出: 2
解释：将字符串变成: "bbaabbaabbaa", 这样两次次操作就可以使得字符串S没有三个相同的连续字母。
示例3:
输入:
S="baabab"
输出: 0
注意事项
N 是一个整数，范围是: [0, 2000000]
字符串S仅仅由字母 'a' 和/或 'b' 组成
'''
class Solution:
    """
    @param S: a string
    @return:  return the minimum number of moves
    """
    def MinimumMoves(self, S):
        # write your code here
        count = 0
        a_count = 0
        b_count = 0
        for s in S:
            if s == 'a':
                a_count += 1
                if b_count >= 3:
                    count += b_count // 3
                b_count = 0
            
            if s == 'b':
                b_count += 1
                if a_count >= 3:
                    count += a_count // 3
                a_count = 0
        if a_count != 0:
            count += a_count // 3
        elif b_count != 0:
            count += b_count // 3
        return count
'''
每三个相邻移动加1   //3即可
'''