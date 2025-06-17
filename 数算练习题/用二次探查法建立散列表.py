'''
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
'''
n,m=[int(x) for x in input().split()]
num_list=[int(x) for x in input().split()]
lst=[None]*m
ans=[]
visited=set()
for i in num_list:
    if i in visited:
        ans.append(ans[num_list.index(i)])
        continue
    visited.add(i)
    record=i%m
    if lst[record]==None:
        lst[record]=i
        ans.append(record)
    else:
        t=1
        cnt=0
        while True:
            if cnt%2==0:
                if lst[(record+t**2)%m]==None:
                    lst[(record+t**2)%m]=i
                    ans.append((record+t**2)%m)
                    break
            else:
                if lst[(record-t**2)%m]==None:
                    lst[(record-t**2)%m]=i
                    ans.append((record-t**2)%m)
                    break
            if cnt%2!=0:
                t+=1
            cnt+=1        
print(*ans)