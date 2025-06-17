n,k=[int(x) for x in input().split()]
first,second=[],[]
lst=[]
for _ in range(n):
    a,b=[int(x) for x in input().split()]
    first.append(a)
    second.append(b)
    lst.append([a,b,_+1])
lst.sort(reverse=True)
lst=lst[:k]
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][2])