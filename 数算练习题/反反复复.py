n=int(input())
s=input()
ns=''
num=1
while True:
    if num*n-1<len(s):
        if num%2==1:
            ns+=s[(num-1)*n:num*n]
        else:
            ns+=s[num*n-1:(num-1)*n-1:-1]
        num+=1
    else:
        break
ans=''
for i in range(n):
    cnt=0
    while cnt*n+i<len(ns):
        ans+=ns[cnt*n+i]
        cnt+=1
print(ans)