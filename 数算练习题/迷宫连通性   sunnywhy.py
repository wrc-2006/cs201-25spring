from collections import defaultdict
def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]
        u=parent[u]
    return u
def union(u,v):
    u_root=find(u)
    v_root=find(v)
    if u_root==v_root:
        return
    if rank[u_root]>rank[v_root]:
        parent[v_root]=u_root
    else:
        parent[u_root]=v_root
        if rank[u_root]==rank[v_root]:
            rank[v_root]+=1

n,m=[int(x) for x in input().split()]
parent=[int(x) for x in range(n+1)]
rank=[int(x) for x in range(n+1)]
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    union(a,b)
root=find(1)
for i in range(1,n+1):
    if root!=find(i):
        print('No')
        break
else:
    print('Yes')