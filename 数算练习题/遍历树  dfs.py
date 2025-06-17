import sys
sys.setrecursionlimit(1<<30)
class TreeNode:
    def __init__(self,val=0,children=None):
        self.val=val
        self.children=[]
        
def dfs(root):
    if not root.children:
        print(root.val)
        return
    lst=[root]+root.children
    lst.sort(key=lambda x:x.val)
    for i in lst:
        if i==root:
            print(root.val)
            continue
        dfs(i)

n=int(input())
record={}
lst=[]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append(s)
    for i in s[1:]:
        if i not in record:
            record[i]=TreeNode(i)
nodes=[]
for i in lst:
    arr=i
    if arr[0] in record:
        node=record[arr[0]]
    else:
        node=TreeNode(arr[0])
    for j in arr[1:]:
        node.children.append(record[j])
    nodes.append(node)
child=list(record.values())
root=list(filter(lambda x:x not in child,nodes))[0]
dfs(root)
    