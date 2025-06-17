n=int(input())
lst=[]
for _ in range(n):
    lst.append([x for x in input().split()])
m=int(input())
for _ in range(m):
    word=input()
    ans=[]
    for i in range(len(lst)):
        if word in lst[i]:
            ans.append(i+1)
    if not ans:
        print('NOT FOUND')
        continue
    print(*ans)