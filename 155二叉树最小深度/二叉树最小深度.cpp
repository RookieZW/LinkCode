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
     * @param root: The root of binary tree
     * @return: An integer
     */
    public:
        int depth = INT_MAX;
    int minDepth(TreeNode * root) {
        // write your code here
        if (root == nullptr) return 0;
        int left = minDepth(root->left);
        int right = minDepth(root->right);
        depth = min(depth, left + right + 1);
        if (left && right) return min(left, right) +1;
        else return left > right ? left + 1 : right + 1;
    }
};

'''
注意只有右子树的情况
'''