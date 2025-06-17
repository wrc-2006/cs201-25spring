'''
n,m=[int(x) for x in input().split()]
edges=[]
for _ in range(m):
    edges.append([int(x) for x in input().split()])
d=[[0]*n for i in range(n)]
a=[[0]*n for i in range(n)]
for edge in edges:
    d[edge[0]][edge[0]]+=1
    d[edge[1]][edge[1]]+=1
    a[edge[0]][edge[1]]+=1
    a[edge[1]][edge[0]]+=1
ans=[[]for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[i].append(d[i][j]-a[i][j])
for i in ans:
    print(*i)
'''
##OOP写法
class vertex:
    def __init__(self,key):
        self.key=key
        self.neighbors={}
    def get_neighbor(self,other):
        return self.neighbors.get(other)
    def set_neighbor(self,other,weight=0):
        self.neighbors[other]=weight
    def get_neighbors(self):
        return self.neighbors.keys()
    def get_key(self):
        return self.key
class Graph:
    def __init__(self):
        self.vertlist={}
    def addvertex(self,key):
        newvert=vertex(key)
        self.vertlist[key]=newvert
        return newvert
    def getvert(self,n):
        return self.vertlist.get(n)
    def addedge(self,a,b,weight=0):
        if a not in self.vertlist:
            new=self.addvertex(a)
        if b not in self.vertlist:
            new=self.addvertex(b)
        self.vertlist[a].set_neighbor(self.vertlist[b],weight)
    def __iter__(self):
        return iter(self.vertlist.values())
        
n,m=[int(x) for x in input().split()]
edges=[]
for _ in range(m):
    edges.append([int(x) for x in input().split()])
graph=Graph()
for i in range(n):
    graph.addvertex(i)
for edge in edges:
    a,b=edge
    graph.addedge(a,b)
    graph.addedge(b,a)
ans=[]
for vert in graph:
    row=[0]*n
    row[vert.get_key()]=len(vert.get_neighbors())
    for neighbor in vert.get_neighbors():
        row[neighbor.get_key()]=-1
    ans.append(row)
for i in ans:
    print(*i)