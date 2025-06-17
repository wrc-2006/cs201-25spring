n,m=[int(x) for x in input().split()]
ans=[[] for _ in range(n)]
for _ in range(m):
    u,v=[int(x) for x in input().split()]
    ans[u].append(v)
    ans[v].append(u)
for i in range(n):
    if ans[i]:
        print(f'{i}({len(ans[i])})',end=' ')
        print(*ans[i])
    else:
        print(f'{i}({len(ans[i])})')