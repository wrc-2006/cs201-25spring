t=int(input())
s=[int(x) for x in input().split()]
s.sort()
ans=[(float('inf'),0)]
l,r=0,len(s)-1
while l<r:
    record=s[l]+s[r]
    if abs(t-record)<ans[0][0]:
        ans.pop(0)
        ans.append([abs(t-record),record])
    elif abs(t-record)==ans[0][0]:
        ans.append([abs(t-record),record])
    if record<=t:
        l+=1
    else:
        r-=1
ans.sort()
print(ans[0][1])