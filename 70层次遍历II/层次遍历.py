'''
从下往上遍历
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if root == None:
            return []
        level = 0
        value = [[root.val]]
        level_value = []
        level_root = [root]
        next_level_root = []
        while len(next_level_root) > 0 or root != None:
            if len(level_root) > 0:
                root = level_root.pop()
                if root.right:
                    next_level_root.insert(0, root.right)
                    level_value.insert(0, root.right.val)
                if root.left:
                    next_level_root.insert(0, root.left)
                    level_value.insert(0, root.left.val)
            elif len(next_level_root) == 0:
                root = None
            
            else:
                level_root = next_level_root
                next_level_root = []
                value.append(level_value)
                level_value = []
        value.reverse()
        return value
#思路
#上一集的思想 
#反转即可