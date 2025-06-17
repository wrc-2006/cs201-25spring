from collections import deque
def bfs(lst,st,r,c):
    inq=set()
    q=deque()
    inq.add(st)
    q.append((st,0))
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        (x,y),time=q.popleft()
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<r and 0<=ny<c:
                if lst[nx][ny]=='E':
                    return time+1
                elif lst[nx][ny]=='.' and (nx,ny) not in inq:
                    inq.add((nx,ny))
                    q.append(((nx,ny),time+1))
    return 'oop!'

t=int(input())
for _ in range(t):
    r,c=[int(x) for x in input().split()]
    lst=[]
    for __ in range(r):
        s=input()
        lst.append(s)
        if 'S' in s:
            st=(__,s.index('S'))
    print(bfs(lst,st,r,c))