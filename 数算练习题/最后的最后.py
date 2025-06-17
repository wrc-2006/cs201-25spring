n,k=[int(x) for x in input().split()]
cnt=k
lst=[int(i) for i in range(1,n+1)]
ans=[]
while len(lst)>1:
    if k==1:
        ans.append(lst.pop(0))
        k=cnt
    lst.append(lst.pop(0))
    k-=1
print(*ans)