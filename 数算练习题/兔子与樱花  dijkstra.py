import heapq
def dijkstra(st,ed):
    record={}
    for i in dic:
        record[i]=float('inf')
    record[st]=0
    ans=''
    ans+=st
    q=[]
    heapq.heappush(q,(0,st,ans))
    if st==ed:
        return ans
    while q:
        distance,st,path=heapq.heappop(q)
        if st==ed:
            return path
        lst=dic[st]
        for next,d in lst:
            if distance<=record[st]:
                record[st]=distance
                newpath=path+'->('+str(d)+')->'+next
                heapq.heappush(q,(distance+d,next,newpath))
    

p=int(input())
dic={}
for _ in range(p):
    dic[input()]=[]
q=int(input())
for _ in range(q):
    a,b,c=[x for x in input().split()]
    c=int(c)
    dic[a].append((b,c))
    dic[b].append((a,c))
r=int(input())
for _ in range(r):
    st,ed=input().split()
    print(dijkstra(st,ed))