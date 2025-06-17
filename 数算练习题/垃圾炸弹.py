d=int(input())
n=int(input())
lst=[[0]*1025 for i in range(1025)]
for _ in range(n):
    x,y,i=[int(x) for x in input().split()]
    for a in range(max(0,x-d),min(1025,x+d+1)):
        for b in range(max(0,y-d),min(1025,y+d+1)):
            lst[a][b]+=i
ans,cnt=0,1
for i in range(1025):
    for j in range(1025):
        if lst[i][j]>ans:
            ans=lst[i][j]
            cnt=1
        elif lst[i][j]==ans:
            cnt+=1
print(cnt,ans)