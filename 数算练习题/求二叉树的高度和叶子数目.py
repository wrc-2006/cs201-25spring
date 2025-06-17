#pylint:skip-file
import sys
sys.setrecursionlimit(1<<30)

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def height(root):
    if not root:
        return -1
    return max(height(root.left),height(root.right))+1

def leave(root):
    if not root:
        return 0
    if (not root.left) and (not root.right):
        return 1
    return leave(root.left)+leave(root.right)

n=int(input())
nodes=[None]*n
for i in range(n):
    nodes[i]=TreeNode(i)
has_parent=[False]*n
for i in range(n):
    l,r=[int(x) for x in input().split()]
    if l!=-1:
        nodes[i].left=nodes[l]
        has_parent[l]=True
    if r!=-1:
        nodes[i].right=nodes[r]
        has_parent[r]=True
for i in range(n):
    if has_parent[i]==False:
        root=nodes[i]
        break
print(height(root),leave(root))
