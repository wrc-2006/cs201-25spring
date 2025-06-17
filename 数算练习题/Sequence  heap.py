'''
t=int(input())
for _ in range(t):
    m,n=[int(x) for x in input().split()]
    lst=[]
    d=[]
    for __ in range(m):
        s=sorted([int(x) for x in input().split()])
        lst.append(s)
        d.append([s[i]-s[i-1] for i in range(1,n)])
    ans=[]
    re=0
    for i in  lst:
        re+=i[0]
    ans.append(re)
    for i in range(n-1):
        minnum=float('inf')
        record=0
        for j in range(n-1):
            if d[j]!=[]:
                if d[j][0]<minnum:
                    minnum=d[j][0]
                    record=j
        d[record].pop(0)
        
        re+=minnum
        ans.append(re)
    print(*ans)
'''

import heapq
def find_two(a,b):
    out,d=[],[]
    st=a[0]+b[0]
    d.append(tuple([a[i]-a[i-1] for i in range(1,n)]))
    d.append(tuple([b[i]-b[i-1] for i in range(1,n)]))
    pq=[]   
    arr=[0]*2
    heapq.heappush(pq,(st,arr))
    visited=set()
    visited.add(tuple(arr))
    while len(out)<n:
        current_st,current_arr=heapq.heappop(pq)
        out.append(current_st)
        for i in range(2):
            if current_arr[i]+1<n:
                new_arr=current_arr[:]
                new_arr[i]+=1
                if tuple(new_arr) not in visited:
                    visited.add(tuple(new_arr))
                    new_re=current_st+d[i][current_arr[i]]
                    heapq.heappush(pq,(new_re,new_arr))
    return out

t=int(input())
        
def find(m,n):
    ans,lst=[],[] 
    for __ in range(m):
        s=sorted([int(x) for x in input().split()])
        lst.append(s)
    if len(lst)==1:
        return lst[0]
    else:
        out=find_two(lst[0],lst[1])
        for i in lst[2:]:
            out=find_two(out,i)
        return sorted(out)

for _ in range(t):
    m,n=[int(x) for x in input().split()]
    ans=find(m,n)
    print(*ans)