/*
给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）

样例
样例 1:
	输入:  给定一棵树（只有一个节点）:
	2
	输出：2
	
样例 2:
	输入:  给定一棵树：

      1
     / \
    2   3
		
	输出: 6
*/
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    public:
        int ret = INT_MIN;
        int maxPathSum(TreeNode * root) {
        // write your code here
        getReslult(root,ret);
        return ret;
    }
    int getReslult(TreeNode *root,int &ret){
        if(root==NULL) return 0;
        int left=getReslult(root->left,ret);
        int right=getReslult(root->right,ret);
        
        ret=max(ret,max(0,left)+max(0,right)+root->val);
        return max(0,max(left,right)+root->val);
    }
    
};
/*
 与最长路径的差别  
  增加了记录ret
*/