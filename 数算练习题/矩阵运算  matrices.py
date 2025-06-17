lst=[]
for _ in range(3):
    row,col=[int(x) for x in input().split()]
    m=[]
    for __ in range(row):
        m.append([int(x) for x in input().split()])
    lst.append(m)
a,b,c=lst[0],lst[1],lst[2]
if len(a[0])==len(b) and len(a)==len(c) and len(b[0])==len(c[0]):
    ans=[[0]*len(b[0]) for _ in range(len(a))]  ##浅拷贝问题
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            for p in range(len(b)):
                ans[i][j]+=a[i][p]*b[p][j]
            ans[i][j]+=c[i][j]
    for i in ans:
        print(*i)
else:
    print('Error!')