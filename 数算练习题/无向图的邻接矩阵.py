from collections import defaultdict
n,m=[int(x) for x in input().split()]
ans=[[0]*n for _ in range(n)]
for _ in range(m):
    u,v=[int(x) for x in input().split()]
    ans[u][v]=1
    ans[v][u]=1
for i in ans:
    print(*i)