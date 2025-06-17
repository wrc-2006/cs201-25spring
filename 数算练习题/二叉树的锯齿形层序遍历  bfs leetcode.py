from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        out=[]
        out.append([root.val])
        q=deque([(root,0)])   
        while q:
            node,cnt=q.popleft()
            if node.left:
                q.append((node.left,cnt+1))
                if len(out)<=cnt+1:
                    out.append([node.left.val])
                else:
                    out[cnt+1].append(node.left.val)
            if node.right:
                q.append((node.right,cnt+1))
                if len(out)<=cnt+1:
                    out.append([node.right.val])
                else:
                    out[cnt+1].append(node.right.val)
        for i in range(1,len(out),2):
            out[i].reverse()
        return out
            
        