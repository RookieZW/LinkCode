#include <iostream>
#include <assert.h>
/*给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)。

样例
样例 1:

输入:  str="abcdefg", offset = 3
输出:  str = "efgabcd"    
样例解释:  注意是原地旋转，即str旋转后为"efgabcd"
*/
class Solution {
public:
    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    void rotateString(string &str, int offset) {
        // write your code here
        assert(offset>=0);
        assert(str.length()>=0);
        if (str.length()==0)
            return ;
        if (offset >= str.length()){
            offset = offset % str.length();
        }
        int i = 0, j =0;
        for(i = offset; i > 0; i--){
            char c = str[str.length()-1];
            for (j = str.length()-1; j > 0; j--){
                str[j] = str[j-1];
            }
            str[0] = c;
        }
    }
};

/*
*解题思路
*   1、记住移动了offset次
*   2、每次记录位于最末尾的数
*   3、其余数字依次后移， 并将记录的数放到最开始位置
*/