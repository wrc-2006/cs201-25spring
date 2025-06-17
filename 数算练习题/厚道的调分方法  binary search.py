def f(grade):
    grade.sort()
    cnt=0
    for i in grade:
        if i>=85:
            cnt+=1
    if cnt>=0.6*len(grade):
        return True
    return False

grade=[eval(x) for x in input().split()]
grade.sort()
left,right=0,1000000000
while left<=right:
    mid=(left+right)//2
    newgrade=[(mid/1000000000)*x+1.1**((mid/1000000000)*x) for x in grade]
    if f(newgrade):
        ans=mid
        right=mid-1
    else:
        left=mid+1
        
print(ans)    
