'''
给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

样例
例1:

输入:[1, 2, -3, 1]
输出:6
解释:
子数组是 [1,2] 和[-3].所以答案是 6.
例2:

输入:[0,-1]
输出:1
解释:
子数组是 [0] 和 [-1].所以答案是 1.
挑战
时间复杂度为O(n)，空间复杂度为O(n)

注意事项
子数组最少包含一个数
'''
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        nums = list(set(nums))
        nums.append(0)
        nums.sort()
        index = nums.index(0)
        if index == len(nums)-1:
            return nums[-2] - sum(nums[:-2])
        elif nums[index] == nums[-1]:
            return 0 - sum(nums)
        else:
            return sum(nums[index:])-sum(nums[0:index])
#思路
#我觉得这个题 答案错了
#这个不是三种情况？
#1、所有数均小于0    那么就是最接近0的数 -  其他数的和
#2、所有数小于等于0（0必存在）  0-其他数的和
#3、大于小于的0都有    大于0的数的和-小于0的数的和
#例如[-4,-5,-22]
#官方答案是21    奇奇怪怪的   难道不应该是  [-4] [-5,-22]嘛这个结构不是23嘛