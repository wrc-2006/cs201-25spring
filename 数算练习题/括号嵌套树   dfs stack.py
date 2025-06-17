import sys
sys.setrecursionlimit(1<<30)
class TreeNode:
    def __init__(self,val=0,children=None):
        self.val=val
        self.children=[]

def pre(root):
    out=''
    if root:
        out+=root.val
        for i in root.children:
            out+=pre(i)
    return out

def post(root):
    out=''
    if root:      
        for i in root.children:
            out+=post(i)
        out+=root.val
    return out
        
s=input()
root=TreeNode(s[0])
stack=[]
nodes=[]
cur=root
for i in s[1:]:
    if i=='(':
        stack.append(i)
        nodes.append(cur)
    elif i==',':
        continue
    elif i==')':
        stack.pop()
        nodes.pop()
    else:
        node=TreeNode(i)
        nodes[-1].children.append(node)
        cur=node
print(pre(root))
print(post(root))
