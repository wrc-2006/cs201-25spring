#pylint:skip-file
def f(inc,outc):
    global cnt
    if inc==n and outc==n:
        cnt+=1
    if outc<n:
        f(inc,outc+1)
    if inc<outc:
        f(inc+1,outc)
    
n=int(input())
lst=[int(x) for x in range(1,n+1)] 
cnt=0
f(0,0)
print(cnt)