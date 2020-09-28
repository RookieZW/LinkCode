'''
描述
给出一棵二叉树，返回其节点值的前序遍历。
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        stack = []
        output = []
        
        while root != None or len(stack) != 0:
            if root != None:
                stack.append(root)
                output.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return output
#思路
#双栈法（太好用了）
#直接借用递归思想