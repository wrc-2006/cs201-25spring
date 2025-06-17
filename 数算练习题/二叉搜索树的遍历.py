from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def build(preorder):
    rootval=preorder[0]
    root=TreeNode(rootval)
    if len(preorder)==1:
        return root
    in_index=0
    for i in range(1,len(preorder)-1):
        if preorder[i]<rootval and preorder[i+1]>rootval:
            in_index=i
            break
    if in_index:
        root.left=build(preorder[1:in_index+1])
        root.right=build(preorder[in_index+1:])
    else:
        if preorder[1]<rootval:
            root.left=build(preorder[1:])
        else:
            root.right=build(preorder[1:])
    return root
def post(root):
    ans=[]
    if root:
        ans+=post(root.left)
        ans+=post(root.right)
        ans.append(root.val)
    return ans
n=int(input())
preorder=[int(x) for x in input().split()]
root=build(preorder)
ans=post(root)
print(*ans)
