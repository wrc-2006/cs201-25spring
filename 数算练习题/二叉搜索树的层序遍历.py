from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def build(root,insertval):    
    insert=TreeNode(insertval)    
    if insertval>root.val:
        if root.right:
            build(root.right,insertval)
        else:
            root.right=insert   
    if insertval<root.val:
        if root.left:
            build(root.left,insertval)
        else:
            root.left=insert
    return root

def bfs(root):
    ans=[]
    q=deque([root])
    while q:
        node=q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans

s=[int(x) for x in input().split()]
root=TreeNode(s[0])
record=set()
record.add(s[0])
for i in s[1:]: 
    if i in record:
        continue
    root=build(root,i)
    record.add(i)
ans=bfs(root)
print(*ans)
    