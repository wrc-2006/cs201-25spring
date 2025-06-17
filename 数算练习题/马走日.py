#pylint:skip-file
def dfs(n,m,x,y,node):
    global cnt
    if node==n*m:
        cnt+=1
        return
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=True
            dfs(n,m,nx,ny,node+1)
            visited[nx][ny]=False
t=int(input())
for _ in range(t):
    n,m,x,y=[int(x) for x in input().split()]
    cnt=0
    d=[(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
    visited=[[False]*m for _ in range(n)]
    visited[x][y]=True
    dfs(n,m,x,y,1)
    print(cnt)