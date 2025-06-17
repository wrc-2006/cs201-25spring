from collections import deque,defaultdict
n,m=[int(x) for x in input().split()]
graph=defaultdict(list)
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    graph[b].append(a)
indegree=defaultdict(int)
q=deque()
result=[]
for u in graph:
    for v in graph[u]:
        indegree[v]+=1
for u in graph:
    if indegree[u]==0:
        q.append((u,0))
while q:
    u,cost=q.popleft()
    result.append((u,cost))
    for v in graph[u]:
        indegree[v]-=1
        if indegree[v]==0:
            q.append((v,cost+1))
ans=100*n
for i in result:
    ans+=i[1]
print(ans)