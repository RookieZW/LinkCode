'''
小林是班级的英语课代表，他想开发一款软件来处理班上同学的成绩
小林的软件有一个神奇的功能，能够通过一个百分数来反应你的成绩在班上的位置。“成绩超过班级 …% 的同学”。
设这个百分数为 p，考了 s 分，则可以通过以下式子计算得出 p：
p = ( 分数不超过 s 的人数 - 1) / 班级总人数 * 100%
请你设计一下这个软件

样例
例1:

输入: score = [100,98,87], ask=[1,2,3]
输出: [66,33,0] 
解释:
第一个人考了100分，超过了66%的学生
注意事项
给出score数组代表第i个人考了score[i]分
给出ask数组代表询问第i个人的成绩百分数
每询问一次输出对应的成绩百分数，不需要输出百分号
答案向下取整（为避免精度丢失，请优先计算乘法）
'''
class Solution:
    """
    @param score: Each student's grades
    @param ask: A series of inquiries
    @return: Find the percentage of each question asked
    """
    def getIndex(self, scores, value, nums):
        flag = -1;
        for i in range(nums - 1, -1, -1):
            if scores[i] == value:
                flag = i
                break
        return flag
        
    def englishSoftware(self, score, ask):
        # write your code here
        per_len = len(ask)
        sorces = sorted(score)
        
        nums = len(score)
        percentage = [0] * nums
        for i in range(nums):
                percentage[i] = i * 100 // nums
        res = []
        for i in ask:
            value = score[i - 1]
            index = self.getIndex(sorces, value, nums)
            res.append(percentage[index])
        return res