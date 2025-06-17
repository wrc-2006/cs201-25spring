class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
n=int(input())
lst=[int(x) for x in input().split()]
nodes=[None]*n
for i in range(n):
    nodes[i]=TreeNode(lst[i])
for i in range(n):
    if 2*i+1<n:
        nodes[i].left=nodes[2*i+1]
    if 2*i+2<n:
        nodes[i].right=nodes[2*i+2]
ans=[]
def dfs(node,record):
    if not node.left and not node.right:
        ans.append(record+[node.val])
        return 
    if node.right:
        dfs(node.right,record+[node.val])
    if node.left:
        dfs(node.left,record+[node.val])
    
dfs(nodes[0],[])
maxh=0
minh=0
for i in ans:
    print(*i)
    re_max,re_min,same=0,0,0
    lenth=len(i)
    for j in range(1,len(i)):
        if i[j]>i[j-1]:
            re_min+=1
        elif i[j]<i[j-1]:
            re_max+=1
        else:
            same+=1
    if re_max==0:
        minh+=1
    if re_min==0:
        maxh+=1
if maxh==len(ans):
    print('Max Heap')
elif minh==len(ans):
    print('Min Heap')
else:
    print('Not Heap')