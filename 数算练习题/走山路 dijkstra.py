import heapq
def dijkstra(x1,y1,x2,y2,lst):
    pq=[(0,(x1,y1))]
    distance=[[float('inf')]*n for _ in range(m)]
    distance[x1][y1]=0
    visited=set()
    while pq:
        dist,(x,y)=heapq.heappop(pq)
        if x==x2 and y==y2:
            return dist
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<m and 0<=ny<n:
                if (nx,ny) not in visited and lst[nx][ny]!='#':
                    newdist=dist+abs(int(lst[nx][ny])-int(lst[x][y]))
                    if newdist<distance[nx][ny]:
                        distance[nx][ny]=newdist
                        heapq.heappush(pq,(newdist,(nx,ny)))
    return 'NO'
    
m,n,p=[int(x) for x in input().split()]
lst=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(m):
    lst.append([x for x in input().split()])   #字符串
for _ in range(p):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    if lst[x1][y1]=='#' or lst[x2][y2]=='#':
        print('NO')
        continue
    print(dijkstra(x1,y1,x2,y2,lst))