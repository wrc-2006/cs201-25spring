s=input()
num=[str(i) for i in range(10)]
stack=[]
for i in range(len(s)):
    stack.append(s[i])
    if stack[-1]==']':
        stack.pop()
        newstack=[]
        while stack[-1]!='[':
            newstack.append(stack.pop())
        stack.pop()
        newstack.reverse()
        cnt=''
        for i in range(len(newstack)):
            if newstack[i] in num:
                cnt+=newstack[i]
            else:
                newstack=newstack[i:]
                break
        if cnt=='':
            cnt='1'
        stack+=int(cnt)*str(''.join(newstack))
print(''.join(stack))