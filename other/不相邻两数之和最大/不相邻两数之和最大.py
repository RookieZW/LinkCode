'''
	动态规划中  选不选的问题

	不相邻的数字最大和：
		选择该数字即  A = opt[i - 2] + nums[i]
		不选择该数组即 B = opt[i-1]
		最终结果   max(A, B)
'''

def compute_max_sum(nums, i):
	if i == 0:
		return nums[0]
	elif i == 1:
		return max(nums[0], nums[1])
	else:
		nums_len = len(nums)
		opt = [0] * nums_len
		opt[0] = nums[0]
		opt[1] = max(nums[0], nums[1])
		for j in range(2, nums_len):
			opt[j] = max(opt[j-1], opt[j - 2]+nums[j])
			if j == i:
				break
		return max(opt)

def rec_opt(nums, i):
	if i == 0:
		return nums[0]
	elif i == 1:
		return max(nums[0], nums[1])
	else:
		return max(rec_opt(nums, i - 1), rec_opt(nums, i - 2) + nums[i])

def main():
	# nums = [1,2,4,1,7,8,3]
	nums = [3, 34, 4, 12, 5, 2]
	print(compute_max_sum(nums, 4))
	print(rec_opt(nums, 4))


if __name__ == "__main__":
	main()