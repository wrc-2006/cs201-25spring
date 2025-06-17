from collections import deque,defaultdict
def Graph(words):
    graph={i:[] for i in words}
    map=defaultdict(list)
    for word in words:
        for i in range(4):
            record=word[:i]+'*'+word[i+1:]
            map[record].append(word)
    for word in words:
        for i in range(4):
            record=word[:i]+'*'+word[i+1:]
            for a in map[record]:
                if a!=word:
                    graph[word].append(a)
    return graph

def bfs(st,ed,path):
    q=deque()
    inq=set()
    q.append((st,path))
    inq.add(st)
    while q:
        word,path=q.popleft()
        if word==ed:
            return path
        lst=graph[word]
        for i in lst:
            if i not in inq:
                newpath=path+[i]
                q.append((i,newpath))
                inq.add(i)
    return None

n=int(input())
words=[]
for _ in range(n):
    words.append(input())
st,ed=[x for x in input().split()]
graph=Graph(words)
path=bfs(st,ed,[st])
if path:
    print(*path)
else:
    print('NO')
