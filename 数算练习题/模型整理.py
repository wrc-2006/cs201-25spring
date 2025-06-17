n=int(input())
dic={}
for _ in range(n):
    m,n=[x for x in input().split('-')]
    if m not in dic:
        dic[m]=[n]
    else:
        dic[m].append(n)
key=sorted(list(dic.keys()))
for i in key:
    m,b=[],[]
    value=dic[i]
    for j in value:
        if j[-1]=='M':
            m.append(eval(j[:-1]))
        else:
            b.append(eval(j[:-1]))
    m.sort()
    b.sort()
    for num in range(len(m)):
        m[num]=str(m[num])+'M'
    for num in range(len(b)):
        b[num]=str(b[num])+'B'
    lst=m+b
    print(f'{i}: ',end='')
    print(', '.join(lst))
    
