# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        inq=set()
        if not root:
            return []
        ans=[[root.val]]
        inq.add(root.val)
        q=deque([(root,0)])
        while q:
            node,cnt=q.popleft()
            if node.left:
                q.append((node.left,cnt+1))
                if len(ans)>cnt+1:
                    ans[cnt+1].append(node.left.val)
                else:
                    ans.append([node.left.val])
            if node.right:
                q.append((node.right,cnt+1))
                if len(ans)>cnt+1:
                    ans[cnt+1].append(node.right.val)
                else:
                    ans.append([node.right.val])
        return ans
            
        
        