# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def ino(root):
            ans=[]
            if root:   ##中序遍历
                ans+=ino(root.left)
                ans.append(root.val)
                ans+=ino(root.right)
            return ans
        ans=ino(root)
        return ans[k-1]