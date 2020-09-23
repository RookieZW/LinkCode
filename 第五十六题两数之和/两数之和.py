'''
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

样例
Example1:
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
Example2:
给出 numbers = [15, 2, 7, 11], target = 9, 返回 [1, 2].
挑战
给自己加点挑战

O(n)O(n) 空间复杂度，O(nlogn)O(nlogn) 时间复杂度，
O(n)O(n) 空间复杂度，O(n)O(n) 时间复杂度，
'''

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # numbers.append(target)
        A = sorted(numbers)
        # index = A.index(target)
        index = len(A)
        j = index - 1
        i= 0
        while i < index:
            if A[i] + A[j] == target:
                if A[i] == A[j]:
                    number=numbers
                    numbers.reverse()
                    return number.index(A[i]), len(numbers)-numbers.index(A[i])-1
                else:
                    if numbers.index(A[i])>numbers.index(A[j]):
                        return numbers.index(A[j]), numbers.index(A[i])
                    return numbers.index(A[i]),numbers.index(A[j])
            elif A[i] +A[j] > target:
                j -= 1
            elif A[i] +A[j] < target:
                i+=1
                j = index - 1
            elif i >= j:
                break
##思路
#   先排序  （降低难度）
#   遍历整个列表
#   两端向中间遍历
#     两数之和大于target， 右端左移
#     两数之和小于target， 左端右移
#     两数之和等于targrt 返回两值索引