import heapq
n=int(input())
weight=[int(x) for x in input().split()]
heapq.heapify(weight)
ans=0
while len(weight)>1:
    a=heapq.heappop(weight)
    b=heapq.heappop(weight)
    combine=a+b
    ans+=combine
    heapq.heappush(weight,combine)
print(ans)