'''
from collections import defaultdict
import heapq
def f(dic):
    degree=defaultdict(int)
    ans=[]
    pq=[]
    for u in dic:
        for v in dic[u]:
            degree[v]+=1
    for u in range(1,lv+1):
        if degree[u]==0:
            heapq.heappush(pq,u)
    while pq:
        u=heapq.heappop(pq)
        ans.append(u)
        for v in dic[u]:
            degree[v]-=1
            if degree[v]==0:
                heapq.heappush(pq,v)
    return ans
    
lv,a=[int(x) for x in input().split()]
dic=defaultdict(list)
for _ in range(a):
    m,n=[int(x) for x in input().split()]
    dic[m].append(n)
ans=f(dic)
out=[]
for i in ans:
    out.append('v'+str(i))
print(*out)
'''
from collections import defaultdict
import heapq
lv,a=[int(x) for x in input().split()]
d=defaultdict(list)
q=[]
result=[]
indegree=defaultdict(int)
for _ in range(a):
    m,n=[int(x) for x in input().split()]
    d[m].append(n)
for u in d:
    for v in d[u]:
        indegree[v]+=1
for i in range(1,lv+1):
    if indegree[i]==0:
        heapq.heappush(q,i)
while q:
    u=heapq.heappop(q)
    result.append(u)
    for v in d[u]:
        indegree[v]-=1
        if indegree[v]==0:
            heapq.heappush(q,v)
ans=[]
for i in result:
    ans.append('v'+str(i))
print(*ans)