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