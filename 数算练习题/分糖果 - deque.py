from collections import deque
n,m=[int(x) for x in input().split()]
s=[int(x) for x in input().split()]
lst=[]
for i in range(n):
    lst.append((s[i],i+1))
lst=deque(lst)
while lst:
    candy,kid=lst.popleft()
    if not lst:
        print(kid)
        break
    if candy<=m:
        continue
    else:
        candy-=m
        lst.append((candy,kid))
