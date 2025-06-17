from collections import defaultdict,deque
n=int(input())
edges=defaultdict(list)
for _ in range(n-1):
    a,b=[int(x) for x in input().split()]
    edges[a].append(b)
    edges[b].append(a)
restricted=[int(x) for x in input().split()]
visited=set()
visited.add(0)
q=deque([0])  #curnode
cnt=1
while q:
    cur=q.popleft()
    lst=edges[cur]
    for i in lst:
        if i not in restricted and i not in visited:
            visited.add(i)
            q.append(i)
            cnt+=1
print(cnt)