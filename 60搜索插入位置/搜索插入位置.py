'''
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。

你可以假设在数组中无重复元素。

样例
[1,3,5,6]，5 → 2

[1,3,5,6]，2 → 1

[1,3,5,6]， 7 → 4

[1,3,5,6]，0 → 0

挑战
时间复杂度为O(log(n))
'''
lass Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        A_len = len(A)
        if A_len == 0:
            return 0
        start = 0
        end = A_len - 1
        if target > A[end]:
            print(A_len)
            return A_len
        elif target < A[start]:
            return 0
        else:
            while (start <= end):
                middle = (start + end) // 2
                if A[middle] > target:
                    end = middle - 1
                elif A[middle] < target:
                    start = middle + 1
                else:
                    return middle
            return start
'''
就很gay  二分查找
'''