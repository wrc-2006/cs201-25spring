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
cnt=1
while True:
    
    n,m=[int(x) for x in input().split()]
    parent=[int(x) for x in range(n+1)]
    rank=[0]*(n+1)
    if n==m==0:
        break
    for _ in range(m):
        i,j=[int(x) for x in input().split()]
        union(i,j)
    num=set()
    for i in range(1,n+1):
        num.add(find(i))
    ans=len(num)
    print(f'Case {cnt}: {ans}')
    cnt+=1