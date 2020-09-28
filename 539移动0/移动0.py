'''
描述
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
'''

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        nums_len = len(nums)
        i = j = 0
        while j < nums_len:
            if nums[i] == 0:
                nums.remove(nums[i])
            else:
                i += 1
            j+=1
        nums.extend([0]*(nums_len-len(nums)))
        return nums
#思路
#这个很简单   我就是用判断0移除0最后补零的方式  效率有点差  
