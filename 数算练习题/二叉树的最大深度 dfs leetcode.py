# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """ 
        if not root:
            return 0
        lefth=self.maxDepth(root.left)
        righth=self.maxDepth(root.right)
        return max(lefth,righth)+1