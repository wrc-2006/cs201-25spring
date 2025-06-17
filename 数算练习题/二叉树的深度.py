class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def depth(root):
    if not root:
        return 0
    lefth=depth(root.left)
    righth=depth(root.right)
    return max(lefth,righth)+1

def build(node):
    if not node:
        return None
    tree=[None]*len(node)
    for i in range(len(node)):
        tree[i]=TreeNode(i+1)
    for i,(left,right) in enumerate(node):
        if left!=-1:
            tree[i].left=tree[left-1]
        if right!=-1:
            tree[i].right=tree[right-1]
    return tree[0]
    
n=int(input())    
node=[]
for _ in range(n):
    l,r=[int(x) for x in input().split()]
    node.append([l,r])
root=build(node)
print(depth(root))
