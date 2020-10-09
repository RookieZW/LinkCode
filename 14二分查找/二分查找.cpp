'''
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1
'''

class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    int binarySearch(vector<int> &nums, int target) {
        // write your code here
        int length = nums.size() - 1;
        if (nums[0] > target || nums[length] < target){
            return -1;
        }
        int middle = length / 2;
        int begin = 0;
        int end = length;
        while(middle <= end && middle >= begin){
            if(nums[middle] < target){
                begin = middle + 1;
                middle = (begin + end) / 2;
            }else if(nums[middle] > target){
                end = middle - 1;
                middle = (begin + end) / 2;
            }else{
                while(nums[middle] == target){
                    middle--;
                }
                return ++middle;
            }
        }
        return -1;
    }
}
//二分查找
