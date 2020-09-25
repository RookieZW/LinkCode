class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        nums_len = len(nums)
        if nums_len == -1:
            return -1
        middle = nums_len // 2
        start = 0
        end = nums_len-1
        while start <= end:
            middle = (start + end)//2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                start = middle+1
            elif target < nums[middle]:
                end = middle - 1
        return -1
#思路：
#很明显呀  二分查找  题目都说了