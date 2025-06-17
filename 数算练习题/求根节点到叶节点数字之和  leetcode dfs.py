# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.ans=0
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root,s):
            s+=str(root.val)
            if not root.left and not root.right:
                self.ans+=int(s)
                return
            if root.left:
                dfs(root.left,s) 
            if root.right:
                dfs(root.right,s)
        dfs(root,'')
        return self.ans
    
if __name__=='__main__':
    sol=Solution()
    