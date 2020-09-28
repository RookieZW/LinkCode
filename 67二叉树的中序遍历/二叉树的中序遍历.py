'''
描述
给出一棵二叉树,返回其中序遍历
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack = []
        output = []
        while root!=None or len(stack) != 0:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                output.append(root.val)
                root = root.right
        return output
#思路：
# 中序不同之处在于   输出的列表接收stack弹出的值