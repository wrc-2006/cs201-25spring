'''
手搓有点困难……
import heapq
n=int(input())
stack=[]
for _ in range(n):
    s=[int(x) for x in input().split()]
    if len(s)==2:
        heapq.heappush(stack,s[1])
    else:
        print(heapq.heappop(stack))
'''
class heap:
    def __init__(self):
        self.pq=[]
        
    def getup(self,i):
        while (i-1)//2>=0:   #当前父节点   
            parent=(i-1)//2
            if self.pq[i]<self.pq[parent]:
                self.pq[i],self.pq[parent]=self.pq[parent],self.pq[i]
            i=parent
    
    def insert(self,i):
        self.pq.append(i)
        self.getup(len(self.pq)-1)
        
    def getdown(self,i):
        while 2*i+1<len(self.pq):
            child=self.getmin(i)
            if self.pq[i]>self.pq[child]:
                self.pq[i],self.pq[child]=self.pq[child],self.pq[i]
            else:
                break
            i=child
            
    def getmin(self,i):
        if 2*i+2>len(self.pq)-1:
            return 2*i+1
        if self.pq[2*i+1]<self.pq[2*i+2]:
            return 2*i+1
        return 2*i+2
    
    def delete(self):
        self.pq[0],self.pq[-1]=self.pq[-1],self.pq[0]
        ans=self.pq.pop()
        self.getdown(0)
        return ans

n=int(input())
pq=heap()
for _ in range(n):
    s=[int(x) for x in input().split()]
    if len(s)==2:
        pq.insert(s[1])
    else:
        print(pq.delete())
