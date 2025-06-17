from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return 1+f(n-1)+f(n-2)
n=int(input())
print(f(n))