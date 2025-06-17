def prime(n):
    lst=[True]*(n+1)
    primes=[]
    lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return lst
    
t=int(input())
rlst=prime(10001)
for _ in range(t):
    n=int(input())
    ans=[]
    st=n
    for cnt in range(2,n):
        if str(cnt)[-1]=='1':
            st=cnt
            break
    lst=[int(i) for i in range(st,n,10)]
    for i in lst:
        if rlst[i]:
            ans.append(i)
    print(f'Case{_+1}:')
    if ans:
        print(' '.join(map(str,ans)))
    else:
        print('NULL')