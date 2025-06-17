import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)
def dfs(x,y):
    step=1
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<r and 0<=ny<c and lst[nx][ny]<lst[x][y]:
            step=max(step,dfs(nx,ny)+1)
    return step
    
r,c=[int(x) for x in input().split()]
d=[(0,1),(1,0),(-1,0),(0,-1)]
lst=[]
for _ in range(r):
    lst.append([int(x) for x in input().split()])
ans=0
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))
print(ans)