from collections import defaultdict
n=int(input())
parent={}
rank=defaultdict(int)
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
        if rank[u_root]==v_root:
            rank[v_root]+=1
record=[]
for _ in range(n):
    a,b,c,d=[x for x in input()]
    if a not in parent:
        parent[a]=a
    if d not in parent:
        parent[d]=d
    if b=='=':
        union(a,d)
    else:
        record.append((a,d))
for a,d in record:
    if find(a)==find(d):
        print('False')
        break
else:
    print('True')
            