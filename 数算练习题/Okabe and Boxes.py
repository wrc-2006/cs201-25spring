n=int(input())
stack=[]
num=1
cnt=0
for _ in range(2*n):
    s=[x for x in input().split()]
    if s[0]=='add':
        stack.append(int(s[1]))
    else:
        if stack[-1]==num:
            stack.pop()
        else:
            stack.sort(reverse=True)
            stack.pop()
            cnt+=1
        num+=1
print(cnt)