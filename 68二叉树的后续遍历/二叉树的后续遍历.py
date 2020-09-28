'''
描述
给出一棵二叉树，返回其节点值的后序遍历。
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        stack = []
        output = []

        while root != None or len(stack) != 0:
            if root != None:
                stack.append(root)
                output.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        output.reverse()
        return output
#思路：（双栈牛逼）
#记得反转