from collections import defaultdict
import heapq
n=int(input())
stars=defaultdict(list)
d=defaultdict(lambda:float('inf'))
for _ in range(n-1):
    s=[x for x in input().split()]
    root=s[0]
    for i in range(2,len(s)-1,2):
        stars[root].append((s[i],int(s[i+1])))  #star,distance
        stars[s[i]].append((root,int(s[i+1])))  #注意反向边
d['A']=0
visited=set()
q=[]
cnt=0
heapq.heappush(q,(d['A'],'A'))  #distance,node     
while q:
    x,y=heapq.heappop(q)
    if y in visited:
        continue
    visited.add(y)
    cnt+=d[y]
    for i in stars[y]:
        if d[i[0]]>i[1]:
            d[i[0]]=i[1]
            heapq.heappush(q,(d[i[0]],i[0]))
print(cnt)