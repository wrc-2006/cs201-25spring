from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def build(inorder,postorder):
    if not inorder or not postorder:
        return None
    rootval=postorder[-1]
    root=TreeNode(rootval)
    in_index=inorder.index(rootval)
    root.left=build(inorder[:in_index],postorder[:in_index])
    root.right=build(inorder[in_index+1:],postorder[in_index:-1])
    return root
def bfs(root):
    q=deque()
    ans=''
    q.append(root)
    while q:
        node=q.popleft()
        if node:
            ans+=node.val
            q.append(node.left)
            q.append(node.right)
    return ans
n=int(input())
for _ in range(n):
    inorder=input()
    postorder=input()
    root=build(inorder,postorder)
    print(bfs(root))