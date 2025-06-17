case=1
while True:
    n,m=[int(x) for x in input().split()]
    dic={i:[] for i in range(1,n+1)}
    if n==m==0:
        break
    for _ in range(m):
        i,j=[int(x) for x in input().split()]
        dic[i].append(j)
        dic[j].append(i)
    record=[]
    ans=0
    key=[int(i) for i in range(1,n+1)]
    for i in key:
        if i not in record:
            record.append(i)
            record+=dic[i]
            ans+=1
        else:
            record+=dic[i]
    print(f'Case {case}: {ans}')
    case+=1