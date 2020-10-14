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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root == None:
            return []
        level = 0
        value = [[root.val]]
        level_value = []
        level_root = [root]
        next_level_root = []
        count = 0
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
                count += 1
                level_root = next_level_root
                next_level_root = []
                if count % 2 == 0:
                    value.append(level_value)
                else:
                    
                    level_value.reverse()
                    value.append(level_value)
                    
                level_value = []
        return value
"""
层次遍历  判断奇偶层  加入时根据条件是否进行反转
"""