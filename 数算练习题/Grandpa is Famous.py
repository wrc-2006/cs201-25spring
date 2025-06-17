while True:
    n,m=[int(x) for x in input().split()]
    if n==m==0:
        break
    dic={}
    for _ in range(n):
        s=[int(x) for x in input().split()]
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
    ans=[]
    value=list(dic.values())
    value.sort()
    se=value[-2]
    key=list(dic.keys())
    for i in key:
        if dic[i]==se:
            ans.append(i)
    ans.sort()
    print(*ans)