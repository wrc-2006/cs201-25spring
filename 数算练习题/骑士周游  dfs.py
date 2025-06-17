import sys
sys.setrecursionlimit(1<<30)
'''
def dfs(x,y,step):
    if step==n*n:
        return 'success'
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny]=True
            if dfs(nx,ny,step+1)=='success':
                return 'success'
            visited[nx][ny]=False
    return 'fail'
'''
def warnsdorff(x,y,step):
    def getdegree(x,y):  #计算自由度（未访问的邻居数）
        cnt=0
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                cnt+=1
        return cnt
    def move(x,y):
        lst=[]
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                degree=getdegree(nx,ny)
                lst.append((degree,nx,ny))
        if not lst:
            return None
        lst.sort()
        return lst[0][1],lst[0][2]   #返回自由度最小的两个点
    while step<n*n:
        nextmove=move(x,y)
        if not nextmove:
            return 'fail'
        x,y=nextmove
        visited[x][y]=True
        step+=1
    return 'success'
    
n=int(input())
x,y=[int(x) for x in input().split()]
visited=[[False]*n for _ in range(n)]
visited[x][y]=True
d=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
print(warnsdorff(x,y,1))