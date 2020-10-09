'''
查看列表中是否含sum等于target的情况
若有  返回true  否则返回false
'''
import numpy as  np
def rec_subset(nums, i, s):
	if s == 0:
		return True
	elif i == 0:
		return s == nums[0]
	elif nums[i] > s:
		return rec_subset(nums, i - 1, s)
	else:
		A = rec_subset(nums, i - 1, s)
		B = rec_subset(nums, i - 1, s - nums[i])
		return A or B

def dp_subset(nums, s):
	nums_len = len(nums)
	opt = np.zeros((nums_len, s + 1), dtype=bool)

	opt[:, 0] = True
	opt[0, :] = False
	opt[0, nums[0]] = True
	for i in range(1, nums_len):
		for j in range(1, s + 1):
			if s < nums[i]:
				opt[i, j] = opt[i - 1, j]
			else:
				A = opt[i - 1, j]
				B = opt[i - 1, j - nums[i]]
				opt[i, j] = A or B
	return opt[nums_len - 1][s]

def main():
	nums = [3, 34, 4, 12, 5, 2]
	print(dp_subset(nums, 13))

if __name__ == "__main__":
	main()
'''
考虑出口：
	1、 S刚好为0
	2、 还剩一个值，还未出现相等
	3、 当前值大于s， 只考虑不选
	4、 其他  选/不选
无论选择或者不选择，
都是只考虑前面的值  但对应的target不同
'''