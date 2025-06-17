'''
import heapq
from collections import defaultdict
def prim(d):
    visited={0}
    pq=d[0]
    heapq.heapify(pq)
    total_cost=0
    edge_used=1
    while pq and edge_used<len(d):
        distance,node=heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            total_cost+=distance
            edge_used+=1
            for nei_distance,neighbor in d[node]:
                if neighbor not in visited:
                    heapq.heappush(pq,[nei_distance,neighbor])
    return total_cost
            
while True:
    try:
        n=int(input())
        d=defaultdict(list)
        for _ in range(n):
            s=[int(x) for x in input().split()]
            for i in range(n):
                d[_].append([s[i],i])  #distance,end
        print(prim(d))
    except EOFError:
        break
'''
import heapq
while True:
    try:
        n=int(input())
        graph=[]
        for _ in range(n):
            s=[int(x) for x in input().split()]
            graph.append(s)
        d=[float('inf')]*n   #d[i]当前生成树到农场i的最小边权
        d[0]=0    #从农场0开始
        visited=set()
        q=[]
        cnt=0      #最小生成树的总权重
        heapq.heappush(q,(d[0],0))   #distance,node
        while q:
            x,y=heapq.heappop(q)
            if y in visited:
                continue
            visited.add(y)
            cnt+=d[y]
            for i in range(n):
                if d[i]>graph[y][i]:
                    d[i]=graph[y][i]
                    heapq.heappush(q,(d[i],i))
        print(cnt)
    except EOFError:
        break
