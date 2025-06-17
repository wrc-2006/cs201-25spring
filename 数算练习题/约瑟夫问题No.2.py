while True:    
    n,p,m=[int(x) for x in input().split()]
    if n==0:
        break
    ans=[]
    lst=[int(x) for x in range(p,n+1)]+[int(x) for x in range(1,p)]
    while lst:
        cnt=m
        while cnt!=1:
            cnt-=1
            lst.append(lst.pop(0))
        ans.append(lst.pop(0))
    print(','.join(map(str,ans)))
