def f(maxcost):
    month=1
    current=0
    for i in cost:
        if current+i>maxcost:
            month+=1
            if month>m:
                return False
            current=i
        else:
            current+=i
    return True
n,m=[int(x) for x in input().split()]
cost=[]
for _ in range(n):
    cost.append(int(input()))
left,right=max(cost),sum(cost)+1
ans=0
while left<right:
    mid=(left+right)//2
    if f(mid):
        ans=mid
        right=mid
    else:
        left=mid+1
print(ans)