from collections import deque,defaultdict
def topo(graph):
    indegree=defaultdict(int)
    result=[]
    q=deque()
    for u in graph:
        for v in graph[u]:
            indegree[v]+=1
    for u in graph:
        if indegree[u]==0:
            q.append(u)
    while q:
        u=q.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.append(v)
    if len(result)==len(graph):
        return 'No'
    else:
        return 'Yes'
t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    graph=defaultdict(list)
    for __ in range(m):
        x,y=[int(x) for x in input().split()]
        graph[x].append(y)
    print(topo(graph))