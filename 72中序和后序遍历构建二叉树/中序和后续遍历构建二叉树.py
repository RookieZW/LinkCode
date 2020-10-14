'''
根据中序遍历和后序遍历树构造二叉树

样例
样例 1:

输入：[],[]
输出：{}
解释：
二叉树为空
样例 2:

输入：[1,2,3],[1,3,2]
输出：{2,1,3}
解释：
二叉树如下
  2
 / \
1   3
注意事项
你可以假设树中不存在相同数值的节点
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        length = len(inorder)
        pos_start=in_start = 0
        pos_end = in_end = length - 1
        return self.build(inorder, in_start, in_end, postorder, pos_start, pos_end)
    
    def build(self, inorder, in_start, in_end, postorder, pos_start, pos_end):
        if in_start > in_end or pos_start > pos_end:
            return 
        
        tn = TreeNode(postorder[pos_end])
        index = inorder.index(postorder[pos_end])
        num = index - in_start
        
        tn.left = self.build(inorder, in_start, index - 1, postorder, pos_start, pos_start + num - 1)
        tn.right = self.build(inorder, index + 1, in_end, postorder, pos_start + num, pos_end - 1)
        return tn
'''
回溯算法问题
'''