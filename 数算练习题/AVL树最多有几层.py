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