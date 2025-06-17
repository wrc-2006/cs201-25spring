
'''
def f(graph):
    def search(key):
        visited=set()
        visited.add(key)
        q=deque()
        q.append(key)
        while q:
            nkey=q.popleft()
            lst=graph[nkey]
            for newkey in lst:
                if newkey==key:
                    return True
                visited.add(newkey)
                q.append(newkey)
    keys=list(graph.keys())
    for key in keys:
        if search(key):
            return 'Yes'
    return 'No'     
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1<<30)
def f(graph):
    def dfs(key,st,step):
        if key==st and step:
            return True
        lst=graph[key]
        for i in lst:
            if i not in visited:
                visited.add(i)
                if dfs(i,st,True):
                    return True
        return False
    keys=list(graph.keys())
    for key in keys:
        visited=set()
        if dfs(key,key,False):
            return 'Yes'
    return 'No'  

n,m=[int(x) for x in input().split()]
graph=defaultdict(list)
for _ in range(m):
    u,v=[int(x) for x in input().split()]
    graph[u].append(v)
print(f(graph))