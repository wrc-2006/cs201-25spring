# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        rootval=preorder[0]
        root=TreeNode(rootval)
        in_index=inorder.index(rootval)
        root.left=self.buildTree(preorder[1:in_index+1],inorder[:in_index])
        root.right=self.buildTree(preorder[in_index+1:],inorder[in_index+1:])
        return root