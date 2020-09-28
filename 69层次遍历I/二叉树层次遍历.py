'''
描述
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
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
        return value
#思路
#牺牲空间换时间  本来以为不咋的  结果超过了百分之90多的玩家？？？？？？？
#每层的节点全部记录，用完就删除（卸磨杀驴）
#每层的值都留着