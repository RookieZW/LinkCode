#include <iostream>

public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        if (a == 0)
            return b;
        if (b == 0)
            return a;
        int i, sum;
        i = a ^ b;
        sum = (a & b) << 1;
        return aplusb(sum, i);
    }
}

/*
* ��������
*   ������+����  ʹ��λ����ʵ�ּӷ�
* 
* 
* ���˼·��
*   1�������������Լ���ӵ��Ǻ����˽�λ
*   2���Ҳ��������Լ�����н�λ������� ʹ��λ��ʵ�ֽ�λ
*   3��ѭ�������������  ֱ�����ٽ�λ
*/