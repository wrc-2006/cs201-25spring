import heapq
def dijkstra(n):
    q=[(0,0,1)]   #路径长度，cost，起始城市
    while q:
        path,cost,st=heapq.heappop(q)
        if st==n:
            return path
        lst=dic[st]
        for ed,need,lenth in lst:
            if need+cost<=k:
                heapq.heappush(q,(path+lenth,cost+need,ed))
    return -1
k=int(input())
n=int(input())
r=int(input())
dic={int(x):[] for x in range(1,n+1)}
for _ in range(r):
    s,d,l,t=[int(x) for x in input().split()]
    dic[s].append([d,t,l])   ##ed,cost,len
for i in range(1,n):
    dic[i].sort()
print(dijkstra(n))
        
