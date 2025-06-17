'''
n=int(input())
lst=[int(input()) for _ in range(n)]
ans=0
for i in range(1,n):
    for j in range(i):
        if lst[i]>lst[j]:
            ans+=1
print(ans)
'''
def merge(arr,temp,left,right):
    if left>=right:
        return 0
    mid=(left+right)//2
    cnt=merge(arr,temp,left,mid)+merge(arr,temp,mid+1,right)
    i,j,k=left,mid+1,left
    while i<=mid and j<=right:
        if arr[i]>=arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            cnt+=(mid-i+1)
            j+=1
        k+=1
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        arr[i]=temp[i]
    return cnt

n=int(input())
arr=[int(input()) for _ in range(n)]
temp=[0]*n
print(merge(arr,temp,0,n-1))