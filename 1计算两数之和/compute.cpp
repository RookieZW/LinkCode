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
* 问题描述
*   不适用+操作  使用位操作实现加法
* 
* 
* 解决思路：
*   1、异或操作：可以计算加但是忽略了进位
*   2、且操作：可以计算具有进位的情况， 使用位移实现进位
*   3、循环上述两种情况  直至不再进位
*/