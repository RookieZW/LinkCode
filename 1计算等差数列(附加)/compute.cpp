#include <iostream>

class Solution {

	public int ComputeSum(int n) {
		int sum = 0;
		n && sum = ComputeSum(n--);
		return sum;
	}
};

/*
* ����������
* ��1+2+3+...+n
*����ʹ��if else  for   (����) switch * / case�ȹؼ��� while
* 
* ���õݹ�Ͷ�·��˼�룺
*	��n=0ʱ���ݹ�������䵱�˵ݹ�ĳ��ڣ�
* 
*/