from collections import defaultdict
def dfs(x,y):   
    global cnt,flag
    cnt.add(x)
    for i in graph[x]:
        if i not in cnt:
            dfs(i,x)
        elif y!=i:   #i已被访问过且不是父节点y，说明存在环
            flag=True
n,m=[int(x) for x in input().split()]
graph=defaultdict(list)
for _ in range(m):
    u,v=[int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
cnt,flag=set(),False
for i in range(n):
    cnt.clear()
    dfs(i,-1)
    if len(cnt)==n and flag:    ##连通,lag==True:有环
        break
print("connected:"+("yes" if len(cnt) == n else "no"))
print("loop:"+("yes" if flag else 'no'))