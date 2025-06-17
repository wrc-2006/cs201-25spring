def trans(s):
    stack=[]
    record=[]
    num=''
    for i in s:
        if i in '0123456789' or i=='.':
            num+=i
        else:
            if num!='':
                stack.append(num)
                num=''
            if i=='(':
                record.append(i)
            elif i in '+-':
                while record!=[] and record[-1] in '/*+-':
                    stack.append(record.pop())
                record.append(i)
            elif i in '/*':
                while record!=[] and record[-1] in '/*':
                    stack.append(record.pop())
                record.append(i)
            elif i==')':
                while record!=[] and record[-1]!='(':
                    stack.append(record.pop())
                record.pop()
    if num:
        stack.append(num)
    while record:
        stack.append(record.pop())
    return stack
                
                
n=int(input())
for _ in range(n):
    s=input()
    ans=trans(s)
    print(*ans)
    