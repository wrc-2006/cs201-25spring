from math import sqrt
case=1
while True:
    ans=0
    n,d=[int(x) for x in input().split()]
    if n==d==0:
        break
    position=[]
    for _ in range(n):
        x,y=[int(x) for x in input().split()]
        if y>d:
            ans=-1
        else:
            dx=sqrt(d**2-y**2)
            position.append([x-dx,x+dx])
    input()
    if ans==-1:
        print(f'Case {case}: -1')
    else:
        ans=1
        position.sort()
        st,ed=position[0][0],position[0][1]
        for i in position[1:]:
            if i[0]<=ed:
                st=i[0]
                ed=min(ed,i[1])
            else:
                ans+=1
                st,ed=i[0],i[1]
        print(f'Case {case}: {ans}')
    case+=1
        