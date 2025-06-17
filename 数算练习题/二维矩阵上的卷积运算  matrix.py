m,n,p,q=[int(x) for x in input().split()]
a,b=[],[]
for _ in range(m):
    a.append([int(x) for x in input().split()])
for _ in range(p):
    b.append([int(x) for x in input().split()])
ans=[[0]*(n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for c in range(p):
            for d in range(q):
                ans[i][j]+=b[c][d]*a[c+i][d+j]
for i in ans:
    print(*i)