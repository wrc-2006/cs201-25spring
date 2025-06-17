from collections import deque
def bfs(a,b,c):
    inq=set((0,0))
    q=deque([(0,0,0)])
    lst={}
    while q:
        m,n,step=q.popleft()
        if m==c or n==c:
            return step,lst,(m,n)
        if (a,n) not in inq:
            inq.add((a,n))
            q.append((a,n,step+1))
            lst[(a,n)]=((m,n),'FILL(1)')
        if (m,b) not in inq:
            inq.add((m,b))
            q.append((m,b,step+1))
            lst[(m,b)]=((m,n),'FILL(2)')
        if (0,n) not in inq:
            inq.add((0,n))
            q.append((0,n,step+1))
            lst[(0,n)]=((m,n),'DROP(1)')
        if (m,0) not in inq:
            inq.add((m,0))
            q.append((m,0,step+1))
            lst[(m,0)]=((m,n),'DROP(2)')
        if (max(m-b+n,0),min(b,n+m)) not in inq:
            inq.add((max(m-b+n,0),min(b,n+m)))
            q.append((max(m-b+n,0),min(b,n+m),step+1))
            lst[(max(m-b+n,0),min(b,n+m))]=((m,n),'POUR(1,2)')
        if (min(a,m+n),max(m+n-a,0)) not in inq:
            inq.add((min(a,m+n),max(m+n-a,0)))
            q.append((min(a,m+n),max(m+n-a,0),step+1))
            lst[(min(a,m+n),max(m+n-a,0))]=((m,n),'POUR(2,1)')
    return 0,[],(0,0)

a,b,c=[int(x) for x in input().split()]
step,lst,(m,n)=bfs(a,b,c)
if step==0:
    print('impossible')
else:
    print(step)
    ans=[]
    while step>0:
        step-=1
        ans.append(lst[(m,n)][1])
        (m,n)=lst[(m,n)][0]
    for i in ans[::-1]:
        print(i)