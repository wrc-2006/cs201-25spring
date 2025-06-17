n,k=[int(x) for x in input().split()]
lst=[]
for i in range(n):
    lst.append(int(input()))
lst.sort()
record=lst[-1]
cnt=0
for i in lst:
        cnt+=i//record

while cnt<k:
    cnt=0
    record-=1
    if record==0:
        break
    for i in lst:
        cnt+=i//record
  
print(record)