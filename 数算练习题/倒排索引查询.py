n=int(input())
dic={i:[] for i in range(n)}
arr=set()
for _ in range(n):
    lst=set([int(x) for x in input().split()][1:])
    arr=arr|lst
    dic[_]=lst
m=int(input())
for _ in range(m):
    record=[int(x) for x in input().split()]
    ans=arr
    for i in range(n):
        if record[i]==1:
            ans=ans&dic[i]
        if record[i]==-1:
            ans=ans-dic[i]
    if not ans:
        print('NOT FOUND')
        continue
    print(*sorted(ans))