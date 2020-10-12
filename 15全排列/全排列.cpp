'''
给定一个数字列表，返回其所有可能的排列。

样例
样例 1：

输入：[1]
输出：
[
  [1]
]
样例 2：

输入：[1,2,3]
输出：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
挑战
使用递归和非递归分别解决。

注意事项
你可以假设没有重复数字。
'''

class Solution {
public:
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int>> permute(vector<int> &nums) {
        // write your code here
        vector<vector<int>> res;
        vector<int> tem;
        
        this->getPermute(nums, res, tem);
        
        return res;
    }
    
    void getPermute(vector<int> &nums, vector<vector<int>> &res, vector<int> &tem){
        if (nums.size() == tem.size()){
            res.push_back(tem);
            return ;
        }
        
        for(int i = 0; i < nums.size(); i++){
            if (std::find(tem.begin(),tem.end(), nums[i]) != tem.end()){
                continue;
            }
            
            tem.push_back(nums[i]);
            getPermute(nums, res, tem);
            tem.pop_back();
        }
    }
};
'''
回溯问题：
    框架：

        结束条件

        for  
            取数据加到路径中
            递归
            移除数据
'''