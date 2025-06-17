class TreeNode:
    def __init__(self,val=0,degree=0,children=[]):
        self.val=val
        self.degree=degree
        self.children=children
        
def build(s):
    tree=[None]*(len(s)//2)
    for i in range(len(tree)):
        tree[i]=TreeNode(s[2*i],s[2*i+1],[])
    record=tree[1:]
    for i in range(len(tree)):
        for j in range(int(tree[i].degree)):
            tree[i].children.append(record.pop(0))
    return tree[0]
    
def f(root):
    ans=[]
    if root.children:
        for i in root.children:
            ans+=f(i)
    ans+=root.val
    return ans   
      
n=int(input())
out=[]
for _ in range(n):
    s=[i for i in input().split()]
    root=build(s)
    out+=f(root)
print(*out)