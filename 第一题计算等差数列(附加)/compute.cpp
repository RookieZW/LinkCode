#include <iostream>

class Solution {

	public int ComputeSum(int n) {
		int sum = 0;
		n && sum = ComputeSum(n--);
		return sum;
	}
};

/*
* 问题描述：
* 求1+2+3+...+n
*不能使用if else  for   (？：) switch * / case等关键字 while
* 
* 利用递归和短路的思想：
*	当n=0时，递归结束（充当了递归的出口）
* 
*/