import heapq
from collections import defaultdict
def dijkstra(d):
    pq=[(0,0)]  #weigh,st
    visited=set()
    dist={i:float('inf') for i in range(n)}
    dist[0]=0
    while pq:
        weigh,st=heapq.heappop(pq)
        if st==n-1:
            return weigh
        if st in visited:
            continue
        visited.add(st)
        for i in d[st]:
            if i[0] not in visited and dist[i[0]]>weigh+i[1]:
                heapq.heappush(pq,(weigh+i[1],i[0]))
                dist[i[0]]=weigh+i[1]
    return dist[n-1]

n,m=[int(x) for x in input().split()]
d=defaultdict(list)
for _ in range(m):
    a,b,c=[int(x) for x in input().split()]
    d[a-1].append((b-1,c))
print(dijkstra(d)) 
    