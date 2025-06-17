'''
from collections import defaultdict
def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]  #路径压缩
        u=parent[u] 
    return u
def union(u,v):
    u_root=find(u)
    v_root=find(v)
    if u_root==v_root:
        return 
    if rank[u_root]>rank[v_root]:
        parent[v_root]=u_root   #按秩合并，小树挂到大树下
    else:
        parent[u_root]=v_root
        if rank[u_root]==rank[v_root]:
            rank[v_root]+=1

n,m=[int(x) for x in input().split()]
cost=[int(x) for x in input().split()]
friends=defaultdict(list)
parent=[int(x) for x in range(n+1)]
rank=[0]*(n+1)
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    union(a,b)
min_cost=defaultdict(lambda:float('inf'))
for i in range(1,n+1):
    root=find(i)
    if cost[i-1]<min_cost[root]:
        min_cost[root]=cost[i-1]
print(sum(min_cost.values()))
'''
from collections import defaultdict
def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]  #路径压缩
        u=parent[u] 
    return u
def union(u,v):
    u_root=find(u)
    v_root=find(v)
    if u_root==v_root:
        return 
    if cost[u_root-1]>cost[v_root-1]:
        parent[u_root]=v_root   
    else:
        parent[v_root]=u_root
n,m=[int(x) for x in input().split()]
cost=[int(x) for x in input().split()]
friends=defaultdict(list)
parent=[int(x) for x in range(n+1)]
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    union(a,b)
record=set()
ans=0
for i in range(1,n+1):
    if find(i) not in record:
        record.add(find(i))
        ans+=cost[find(i)-1]
print(ans)