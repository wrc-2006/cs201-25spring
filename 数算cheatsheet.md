#### 前缀树/字典树 Trie

电话号码

```python
class TrieNode:
    def __init__(self):
        self.child={}    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, nums):
        curnode = self.root
        for x in nums:
            if x not in curnode.child:
                curnode.child[x] = TrieNode()
            curnode=curnode.child[x]
    def search(self, num):
        curnode = self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode = curnode.child[x]
        return 1
t = int(input())
p = []
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(str(input()))
    nums.sort(reverse=True)
    s = 0
    trie = Trie()
    for num in nums:
        s += trie.search(num)
        trie.insert(num)
    if s > 0:
        print('NO')
    else:
        print('YES')
                
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,number):
        node=self.root
        for i in number:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
            if node.is_end:
                return False
        node.is_end=True
        return len(node.children)==0
    def is_consistent(self,numbers):
        for number in numbers:
            if not self.insert(number):
                return False
        return True
t=int(input())
for _ in range(t):
    n=int(input())
    numbers=[]
    for __ in range(n):
        numbers.append(input())
    numbers.sort(key=lambda x:len(x))
    trie=Trie()
    if trie.is_consistent(numbers):
        print('YES')
    else:
        print('NO')
```

#### 欧拉筛

```python
def is_prime(n):
    lst=[True]*(n+1)
    primes=[]
    lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return lst

def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
```

#### 网络延迟时间 dijikstra

有 `n` 个网络节点，标记为 `1` 到 `n`。给你一个列表 `times`，表示信号经过 **有向** 边的传递时间。 `times[i] = (ui, vi, wi)`，其中 `ui` 是源节点，`vi` 是目标节点， `wi` 是一个信号从源节点传递到目标节点的时间。现在，从某个节点 `K` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1` 。

```Python
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph={i:[] for i in range(1,n+1)}
        for i in times:
            graph[i[0]].append((i[1],i[2]))
        distance={i:float('inf') for i in range(1,n+1)}
        distance[k]=0
        p=[(0,k)]
        while p:
            time,node=heapq.heappop(p)
            if time>distance[node]:
                continue
            for v,w in graph[node]:
                if distance[v]>distance[node]+w:
                    distance[v]=distance[node]+w
                    heapq.heappush(p,(distance[v],v))
        ans=max(distance.values())
        if ans !=float('inf'):
            return ans
        return -1                    
    
if __name__=='__main__':
    sol=Solution()
    print(sol.networkDelayTime([[1,2,1]],2,1))   
```

#### Bellman-Ford算法（不一定考）

```python
def bellman_ford(graph, V, source):    # 初始化距离
    dist = [float('inf')] * V
    dist[source] = 0
    # 松弛 V-1 次
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # 检测负权环
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("图中存在负权环")
            return None
    return dist
# 图是边列表，每条边是 (起点, 终点, 权重)
edges = [
    (0, 1, 5),
    (0, 2, 4),
    (1, 3, 3),
    (2, 1, 6),
    (3, 2, -2)
]
V = 4
source = 0
print(bellman_ford(edges, V, source))
```

有 `n` 个城市通过一些航班连接。给你一个数组 `flights` ，其中 `flights[i] = [fromi, toi, pricei]` ，表示该航班都从城市 `fromi` 开始，以价格 `pricei` 抵达 `toi`。现在给定所有的城市和航班，以及出发城市 `src` 和目的地 `dst`，你的任务是找到出一条最多经过 `k` 站中转的路线，使得从 `src` 到 `dst` 的 **价格最便宜** ，并返回该价格。 如果不存在这样的路线，则输出 `-1`。

```python 
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        distance=[float('inf')]*n
        distance[src]=0
        for _ in range(k+1):
            cur=distance[:]
            for st,ed,cost in flights:
                if distance[st]+cost<distance[ed]:
                    cur[ed]=min(cur[ed],distance[st]+cost)
            distance=cur
        if distance[dst]==float('inf'):
            return -1
        else:
            return distance[dst]
```



#### 并查集

谣言       Vova试图解决一个任务。 任务是来到一个名为Overcity的定居点并在其中传播谣言。Vova 知道 Overcity 有 n 个角色。 有些角色彼此是朋友，他们分享获得的信息。 Vova 还知道他可以贿赂每个角色，这样他或她就开始散布谣言； 第 i 个角色想要 ci 金币来换取散布谣言。 当一个角色听到谣言时，他会告诉他所有的朋友，然后他们开始向他们的朋友传播谣言（免费），依此类推。当所有 n 个角色都知道谣言时，任务就完成了。 Vova 完成任务至少需要花费多少金币？

输入：第一行包含两个整数n和m（1 ≤ n ≤ 10**5， 0 ≤ m ≤ 10**5）—Overcity中的角色数量和好友对的数量。第二行包含n个整数ci（0 ≤ ci ≤ 10**9）—第i个角色要求开始散布谣言的金币数量。接下来是 m 行，每行包含一对数字 (xi, yi)，表示字符 xi 和 yi 是朋友（1 ≤ xi, yi ≤ n, xi ≠ yi）。 保证每对最多列出一次。

```Python
from collections import defaultdict
def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]  #路径压缩
        u=parent[u] 
    return u
def union(u,v):
    u_root=find(u)
    v_root=find(v)
    if u_root==v_root:
        return 
    if rank[u_root]>rank[v_root]:
        parent[v_root]=u_root   #按秩合并，小树挂到大树下
    else:
        parent[u_root]=v_root
        if rank[u_root]==rank[v_root]:
            rank[v_root]+=1
n,m=[int(x) for x in input().split()]
cost=[int(x) for x in input().split()]
friends=defaultdict(list)
parent=[int(x) for x in range(n+1)]
rank=[0]*(n+1)
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    union(a,b)
min_cost=defaultdict(lambda:float('inf'))
for i in range(1,n+1):
    root=find(i)
    if cost[i-1]<min_cost[root]:
        min_cost[root]=cost[i-1]
print(sum(min_cost.values()))
#方法二，按cost排序
from collections import defaultdict
def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]  #路径压缩
        u=parent[u] 
    return u
def union(u,v):
    u_root=find(u)
    v_root=find(v)
    if u_root==v_root:
        return 
    if cost[u_root-1]>cost[v_root-1]:
        parent[u_root]=v_root   
    else:
        parent[v_root]=u_root
n,m=[int(x) for x in input().split()]
cost=[int(x) for x in input().split()]
friends=defaultdict(list)
parent=[int(x) for x in range(n+1)]
for _ in range(m):
    a,b=[int(x) for x in input().split()]
    union(a,b)
record=set()
ans=0
for i in range(1,n+1):
    if find(i) not in record:
        record.add(find(i))
        ans+=cost[find(i)-1]
print(ans)
```

#### Huffman编码

计算最优二叉编码树的带权外部路径长度。要构建一个最优的哈夫曼编码树，首先需要对给定的字符及其权值进行排序。然后，通过重复合并权值最小的两个节点（或子树），直到所有节点都合并为一棵树为止。

```Python
import heapq
class Node:
    def __init__(self, weight, char=None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None
    def __lt__(self, other):
        if self.weight == other.weight:
            return self.char < other.char
        return self.weight < other.weight
def huffman_encoding(char_freq):
    heap = [Node(freq, char) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight + right.weight, min(left.char, right.char))
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]
def external_path_length(node, depth=0):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return depth * node.weight
    return (external_path_length(node.left, depth + 1) +
            external_path_length(node.right, depth + 1))
def main():
    char_freq = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 8, 'f': 9, 'g': 11, 'h': 12}
    huffman_tree = huffman_encoding(char_freq)
    external_length = external_path_length(huffman_tree)
    print("The weighted external path length of the Huffman tree is:", external_length)
if __name__ == "__main__":
    main()
# Output:The weighted external path length of the Huffman tree is: 169
```

构造一个具有n个外部节点的扩充二叉树，每个外部节点Ki有一个Wi对应，作为该外部节点的权。使得这个扩充二叉树的叶节点带权外部路径长度总和最小： Min( W1 * L1 + W2 * L2 + W3 * L3 + … + Wn * Ln)

Wi:每个节点的权值。Li:根节点到第i个外部叶子节点的距离。编程计算最小外部路径长度总和。

输入：第一行输入一个整数n，外部节点的个数。第二行输入n个整数，代表各个外部节点的权值。2<=N<=100。输出：输出最小外部路径长度总和。

```Python
import heapq
n=int(input())
weight=[int(x) for x in input().split()]
heapq.heapify(weight)
ans=0
while len(weight)>1:
    a=heapq.heappop(weight)
    b=heapq.heappop(weight)
    combine=a+b
    ans+=combine
    heapq.heappush(weight,combine)
print(ans)
```

#### AVL树

n层AVL树最少结点数：f(n)=1+f(n-1)+f(n-2)  ,  f(1)=1  ,  f(2)=2

n个结点的AVL数最多层数

```Python
from functools import lru_cache
@lru_cache(maxsize=None)
def min_node(n):  #n层AVL树最小节点数
    if n==1:
        return 1
    if n==2:
        return 2
    return 1+min_node(n-1)+min_node(n-2)
def f(n):
    h=1
    while min_node(h)<=n:
        h+=1
    return h-1
n=int(input())
print(f(n))
```

#### 拓扑排序 Kahn算法

拓扑排序（Topological Sorting）是对有向无环图（DAG）进行排序的一种算法。它将图中的顶点按照一种线性顺序进行排列，使得对于任意的有向边 (u, v)，顶点 u 在排序中出现在顶点 v 的前面。【0

```Python
from collections import deque, defaultdict
def topological_sort(graph):
    indegree = defaultdict(int)
    result = []
    queue = deque()
    for u in graph:   # 计算每个顶点的入度
        for v in graph[u]:
            indegree[v] += 1
    for u in graph:    # 将入度为 0 的顶点加入队列
        if indegree[u] == 0:
            queue.append(u)
    while queue:   # 执行拓扑排序
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    # 检查是否存在环
    if len(result) == len(graph):
        return result
    else:
        return None   ##有向图中存在环
# 示例调用代码
graph = {'A': ['B', 'C'],'B': ['C', 'D'],'C': ['E'],'D': ['F'],'E': ['F'],'F': []}
sorted_vertices = topological_sort(graph)
if sorted_vertices:
    print("Topological sort order:", sorted_vertices)
else:
    print("The graph contains a cycle.")
# Output:
# Topological sort order: ['A', 'B', 'C', 'D', 'E', 'F']
```

#### 判断无向图是否连通、有无环

dfs能直接判断是否连通，过程中记录父亲节点，只要当前节点能够去到一个已经遍历过的节点，并且这个节点不是父亲节点，那么必然成环，以及连通和成环是可以同时判断的

```python
from collections import defaultdict
def dfs(x,y):   #x当前顶点，y父节点
    global cnt,flag
    cnt.add(x)
    for i in graph[x]:
        if i not in cnt:
            dfs(i,x)
        elif y!=i:   #i已被访问过且不是父节点y，说明存在环
            flag=True
n,m=[int(x) for x in input().split()]
graph=defaultdict(list)
for _ in range(m):
    u,v=[int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
cnt,flag=set(),False
for i in range(n):
    cnt.clear()
    dfs(i,-1)   #-1表示初始顶点没有父节点
    if len(cnt)==n :    ##连通
        break
    if flag:   ##flag==True:有环
        break
print("connected:"+("yes" if len(cnt) == n else "no"))
print("loop:"+("yes" if flag else 'no'))
```



#### 最小生成树  MST

用于在带权无向连通图中找到一个权值和最小的生成树。生成树（Spanning Tree）是指一个连通图的子图，它是一棵树（无环且连通），并且包含图中的所有顶点。

给定每对农场之间铺设光纤所需的距离（成本），计算连接所有农场所需的最少光纤总长度。

输入包含多个测试用例。对于每个测试用例：第一行是一个整数 **N**（3 ≤ N ≤ 100），表示农场的数量。接下来的 N 行是一个 N × N 的邻接矩阵，表示每对农场之间的距离。矩阵的第 i 行第 j 列的值表示农场 i 到农场 j 的光纤距离。矩阵的对角线（即 i = j 的位置）均为 0，因为农场到自身的距离无意义。**prim算法**

```python
import heapq
while True:
    try:
        n=int(input())
        graph=[]
        for _ in range(n):
            s=[int(x) for x in input().split()]
            graph.append(s)
        d=[float('inf')]*n   #d[i]当前生成树到农场i的最小边权
        d[0]=0    #从农场0开始
        visited=set()
        q=[]
        cnt=0      #最小生成树的总权重
        heapq.heappush(q,(d[0],0))   #distance,node
        while q:
            x,y=heapq.heappop(q)
            if y in visited:
                continue
            visited.add(y)
            cnt+=d[y]    (ds说这里应该是x不是d[y]?)
            for i in range(n):
                if d[i]>graph[y][i]:
                    d[i]=graph[y][i]
                    heapq.heappush(q,(d[i],i))
        print(cnt)
    except EOFError:
        break
```



**Kruskal算法**

```Python
class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
 def kruskal(graph):
    num_vertices = len(graph)
    edges = []
    # 构建边集
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    # 按照权重排序
    edges.sort(key=lambda x: x[2])
    # 初始化并查集
    disjoint_set = DisjointSet(num_vertices)
    # 构建最小生成树的边集
    minimum_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, weight))
    return minimum_spanning_tree
```

#### 滑动窗口

给定一个字符串 `s`，找出可以由其 **子字符串** 组成的 **3个最大的不同质数** 的和。返回这些质数的 **总和** ，如果少于 3 个不同的质数，则返回 **所有** 不同质数的和。**子字符串** 是字符串中的一个连续字符序列。 **注意：**每个质数即使出现在 **多个** 子字符串中，也只能计算 **一次** 。此外，将子字符串转换为整数时，忽略任何前导零。

```Python
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        primes=set()
        for left in range(len(s)):
            num=int(s[left])
            if is_prime(num):
                primes.add(num)
            for right in range(left+1,len(s)):
                num=int(s[left:right+1])
                if is_prime(num):
                    primes.add(num)
        primes=list(primes)
        primes.sort(reverse=True)
        return sum(primes[:3])
```



#### Kadane's(连续子数组最大和，最大子数组)

```python 
def max_subarray_sum(arr):
    if not arr:
        return 0
    max_current=max_global=arr[0]
    for num in arr[1:]:
        max_current =max(num,max_current+num)
        if max_current>max_global:
			max_global= max_current
    return max_global
```

推广：最大子矩阵

```Python
'''
为了找到最大的非空子矩阵，可以使用动态规划中的Kadane算法进行扩展来处理二维矩阵。
基本思路是将二维问题转化为一维问题：可以计算出从第i行到第j行的列的累计和，
这样就得到了一个一维数组。然后对这个一维数组应用Kadane算法，找到最大的子数组和。
通过遍历所有可能的行组合，我们可以找到最大的子矩阵。
'''
def max_submatrix(matrix):
    def kadane(arr):
      	# max_ending_here 用于追踪到当前元素为止包含当前元素的最大子数组和。
        # max_so_far 用于存储迄今为止遇到的最大子数组和。
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
          	# 对于每个新元素，我们决定是开始一个新的子数组（仅包含当前元素 x），
            # 还是将当前元素添加到现有的子数组中。这一步是 Kadane 算法的核心。
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum
n = int(input())
nums = []
while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]
max_sum = max_submatrix(matrix)
print(max_sum)
```

#### KMP

```python 
def kmp(s1,s2):
    n,m=len(s1),len(s2)
    x,y=0,0
    nt=nextarray(s2,m)
    while x<n and y<m:
        if s1[x]==s2[y]:
            x+=1
            y+=1
        elif y==0:
            x+=1
        else:
            y=nt[y]
    return x-y if y==m else -1
def nextarray(s,m):
    if m==1:
        return [-1]
    nt=[0]*m
    nt[0],nt[1]=-1,0
    i,cn=2,0
    while i<m:
        if s[i-1]==s[cn]:
            cn+=1
            nt[i]=cn
            i+=1
        elif cn>0:
            cn=nt[cn]
        else:
            nt[i]=0
            i+=1
    return nt
```



#### 双指针bisect

```Python
import bisect
 a = [1, 2, 4, 4, 8]
 print(bisect.bisect_left(a, 4))  # 输出: 2
 print(bisect.bisect_right(a, 4))  # 输出: 4
 print(bisect.bisect(a, 4))  # 输出: 4  同bisect_right
```

#### 冒泡排序

```Python
for i in range(n):
	ok=True
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
            ok=False
	if ok:
        break
```

#### 快速随机排序

```Python
def quicksort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i
```



#### 归并排序  Merge Sort

归并排序求逆序数

```Python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]  # 左半部分
        R = arr[mid:]  # 右半部分        
        # 递归排序并获取左右子数组的逆序数
        L, inv_left = mergeSort(L)
        R, inv_right = mergeSort(R)      
        i = j = k = 0
        inv_merge = 0  # 记录当前合并阶段的逆序数       
        # 合并两个有序子数组
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inv_merge += len(L) - i  # 关键：左半剩余元素均构成逆序
            k += 1        
        # 处理剩余元素
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1        
        # 返回排序后的数组和总逆序数
        return arr, inv_left + inv_right + inv_merge
    else:
        return arr, 0  # 单元素数组无逆序
```

##### 根据前序中序构造二叉树

```python
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        rootval=preorder[0]
        root=TreeNode(rootval)
        in_index=inorder.index(rootval)
        root.left=self.buildTree(preorder[1:in_index+1],inorder[:in_index])
        root.right=self.buildTree(preorder[in_index+1:],inorder[in_index+1:])
        return root
```

##### 由二叉树中后序输出前序

```Python
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def preorder(root):
    ans=''
    if root:
        ans+=root.val
        ans+=preorder(root.left)
        ans+=preorder(root.right)
    return ans
def build(inorder,postorder):
    if not inorder or not postorder:
        return None
    rootval=postorder[-1]
    root=TreeNode(rootval)
    in_index=inorder.index(rootval)
    root.left=build(inorder[:in_index],postorder[:in_index])
    root.right=build(inorder[in_index+1:],postorder[in_index:-1])
    return root
inorder=input()
postorder=input()
root=build(inorder,postorder)
print(preorder(root))
```

##### 层序遍历

```Python
from collections import deque
def bfs(root):
    q=deque()
    ans=''
    q.append(root)
    while q:
        node=q.popleft()
        if node:
            ans+=node.val
            q.append(node.left)
            q.append(node.right)
    return ans
```

##### 前缀表达式（波兰表达式）

使用 栈（Stack） 从**右到左**扫描：

遇到数字 → 入栈；遇到运算符 → 弹出栈顶两个数计算，结果入栈；最后栈中剩余的数即为结果。

如：+ 3 * 4 - 2 1          # 前缀表达式，等价于 3 + 4 * (2 - 1）

##### 后缀表达式（逆波兰表达式）

使用 栈（Stack） 从**左到右**扫描：

遇到数字 → 入栈；遇到运算符 → 弹出栈顶两个数计算，结果入栈；最后栈中剩余的数即为结果。

如：3 4 2 1 - * +          # 后缀表达式，等价于 3 + 4 * (2 - 1)

##### **tips：**

```Python
from functools import lru_cache
@lru_cache(maxsize=None)    #超时超内存时尝试

#pylint:skip-file

import sys
sys.setrecursionlimit(1<<30)
```

##### 0-1背包（小偷背包）

```Python
n,b=[int(x) for x in input().split()]  #n物品数 b最大承重
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
dp=[0]*(b+1)   #用于存储不同重量下的最大价值
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])
print(dp[-1])
```

##### 完全背包

```Python
n,a,b,c=[int(x) for x in input().split()]
s=[a,b,c]
dp=[0]+[-float('inf')]*n
for i in range(1,n+1):
    for j in s:
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)
print(dp[n])
```



##### 集合交并集操作

并集：A|B          交集：A&B        差集：A-B

eg：A = {1, 2, 3}，B = {3, 4, 5}              print(A - B)    # 输出: {1, 2}

##### 杂七杂八

hex(x) oct(x) bin(x) 将一个整数x转换为一个十六进制、八进制、二进制的字符串并且有‘0x’ ‘0o’ ‘0b’前缀

ord() 返回单个字符的ASCII码       chr()

##### OOP：

 | `__eq__(self, other)` | `==` | 判断相等 |
 | `__ne__(self, other)` | `!=` | 判断不相等 |
 | `__lt__(self, other)` | `<` | 判断是否小于 |
 | `__le__(self, other)` | `<=` | 判断是否小于等于 |
 | `__gt__(self, other)` | `>` | 判断是否大于 |
 | `__ge__(self, other)` | `>=` | 判断是否大于等于 |

##### 出栈序列统计

栈是常用的一种数据结构，有n个元素在栈顶端一侧等待进栈，栈顶端另一侧是出栈序列。你已经知道栈的操作有两种：push和pop，前者是将一个元素进栈，后者是将栈顶元素弹出。现在要使用这两种操作，由一个操作序列可以得到一系列的输出序列。请你编程求出对于给定的n，计算并输出由操作数序列1，2，…，n，经过一系列操作可能得到的输出序列总数。输入n(1≤n≤15)。输出可能输出序列的总数目。

```Python
#pylint:skip-file
def dfs(innum,outnum):
    global cnt
    if innum==n and outnum==n:
        cnt+=1
    if innum<outnum:
        dfs(innum+1,outnum)
    if outnum<n:
        dfs(innum,outnum+1)
n=int(input())
cnt=0
dfs(0,0)
print(cnt)
```

##### 括号匹配问题 stack

在某个字符串（长度不超过100）中有左括号、右括号和大小写字母；规定（与常见的算数式子一样）任何一个左括号都从内到外与在它右边且距离最近的右括号匹配。写一个程序，找到无法匹配的左括号和右括号，输出原来字符串，并在下一行标出不能匹配的括号。不能匹配的左括号用"$"标注,不能匹配的右括号用"?"标注.输入包括多组数据，每组数据一行，包含一个字符串，只包含左右括号和大小写字母。输出：对每组输出数据，输出两行，第一行包含原始输入字符，第二行由"$","?"和空格组成，"$"和"?"表示与之对应的左括号和右括号不能匹配。

```
((ABCD(x)
$$
)(rttyy())sss)(
?            ?$
```

```Python
while True:
    try:
        s=input()
        n=len(s)
        ans=[' ']*n
        stack=[]
        for i in range(n):
            if s[i]=='(':
                stack.append(('(',i))
            if s[i]==')':
                if not stack:
                    ans[i]='?'
                else:
                    a,b=stack.pop()
        for a,b in stack:
            ans[b]='$'
        print(s)
        print(''.join(ans))
    except EOFError:
        break
```

##### 根据后序表达式建立队列表达式

后序算术表达式可以通过栈来计算其值，做法就是从左到右扫描表达式，碰到操作数就入栈，碰到运算符，就取出栈顶的2个操作数做运算(先出栈的是第二个操作数，后出栈的是第一个)，并将运算结果压入栈中。最后栈里只剩下一个元素，就是表达式的值。有一种算术表达式不妨叫做“队列表达式”，它的求值过程和后序表达式很像，只是将栈换成了队列：从左到右扫描表达式，碰到操作数就入队列，碰到运算符，就取出队头2个操作数做运算（先出队的是第2个操作数，后出队的是第1个），并将运算结果加入队列。最后队列里只剩下一个元素，就是表达式的值。给定一个后序表达式，请转换成等价的队列表达式。例如，"3 4 + 6 5 * -"的等价队列表达式就是"5 6 4 3 * + -" 。

输入：第一行是正整数n(n<100)。接下来是n行，每行一个由字母构成的字符串，长度不超过100,表示一个后序表达式，其中小写字母是操作数，大写字母是运算符。运算符都是需要2个操作数的。

输出：对每个后序表达式，输出其等价的队列表达式。

```Python
from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def build_tree(postfix):
    stack = []
    for char in postfix:
        node = TreeNode(char)
        if char.isupper():
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack[0]
def level_order_traversal(root):
    dq = [root]
    traversal = []
    while dq:
        node = dq.pop(0)
        traversal.append(node.value)
        if node.left:
            dq.append(node.left)
        if node.right:
            dq.append(node.right)
    return traversal
n = int(input().strip())
for _ in range(n):
    postfix = input().strip()
    root = build_tree(postfix)
    queue_expression = level_order_traversal(root)[::-1]
    print(''.join(queue_expression))
```

##### 差分数组

给定原数组 `arr`，其差分数组 `diff` 定义为：

- `diff[0] = arr[0]`
- `diff[i] = arr[i] - arr[i-1]` （`i ≥ 1`）

- **区间增减操作**：
  若要对 `arr` 的区间 `[L, R]` 统一加 `k`，只需修改差分数组的 **两个位置**：
  - `diff[L] += k`
  - `diff[R+1] -= k` （如果 `R+1` 越界则忽略）
- **恢复原数组**：
  对 `diff` 求前缀和即可得到修改后的 `arr`

零钱数组变换1

```Python
class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * n
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        # 前缀和得到每个位置的操作次数
        ops = [0] * n
        ops[0] = diff[0]
        for i in range(1, n):
            ops[i] = ops[i - 1] + diff[i]
        for i in range(n):
            if ops[i] < nums[i]:
                return False
        return True
```

