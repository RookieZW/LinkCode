'''
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大

样例
输入:  nums = [3,4,1,2]
输出: 24
注意事项
nums.size <= 500000nums.size<=500000
-10000 <= nums[i] <= 10000−10000<=nums[i]<=10000
'''

class Solution:
    """
    @param nums: Unordered array
    @return: return the largest product
    """
    def MaximumProduct(self, nums):
        # write your code here
        nums.sort()
        max_1 = nums[-1]*nums[-2]*nums[-3]
        max_2 = nums[-1]*nums[0]*nums[1] 
        if max_1 >= max_2:
            return max_1
        return max_2
'''
不限定几个数字时
'''
class Solution:
    """
    @param nums: Unordered array
    @return: return the largest product
    """
    def MaximumProduct(self, nums):
        # write your code here
        nums_len = len(nums)
        opt = nums_len * [0]
        opt[0] = nums[0]
        for i in range(1,nums_len):
            opt[i] = max(opt[i-1], opt[i-1] * nums[i])
        return max(opt)
'''
DP
'''