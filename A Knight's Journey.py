# pylint: skip-file
def dfs(x,y,step,st):
    global ans
    if step==rp*rq:
        ans.append(st)
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<rp and 0<=ny<rq and lst[nx][ny]==0:
            lst[x][y]=1
            dfs(nx,ny,step+1,st+str(re[ny])+str(nx+1))
            lst[x][y]=0
    ans.sort()
    return ans

    
n=int(input())
case=1
re=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
d=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
for _ in range(n):   
    rp,rq=[int(x) for x in input().split()]
    lst=[[0]*rq for i in range(rp)]
    ans=[]
    ans=dfs(0,0,1,'A1')
    print(f'Scenario #{case}:')
    if ans==[]:
        print('impossible')
    else:
        print(ans[0])
    case+=1
    print()