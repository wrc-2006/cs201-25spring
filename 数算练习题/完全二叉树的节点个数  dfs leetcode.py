# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        def depth(node,record):
            depth=0
            while node:
                if record=='left':
                    depth+=1
                    node=node.left
                else:
                    depth+=1
                    node=node.right
            return depth
        lefth,righth=depth(root,'left'),depth(root,'right')
        if lefth==righth:
            return 2**lefth-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1