'''
超时超时   使用heapq
def f(nums):
    st=nums[0]
    for i in nums[1:]:
        if i<st:
            return False
        st=i
    return True
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        while not f(nums):
            ans+=1
            record=(nums[0]+nums[1],0,1)   #相邻和，两数索引
            for i in range(1,len(nums)-1):
                if nums[i]+nums[i+1]<record[0]:
                    record=(nums[i]+nums[i+1],i,i+1)
            nums.pop(record[1]) 
            nums.pop(record[2]-1)
            nums.insert(record[1],record[0])
        return ans   
'''
import heapq
       
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return 0
        l=[i-1 for i in range(n)]
        r=[i+1 for i in range(n)]
        alive=[True]*n
        bad=0
        v=nums[:]
        for i in range(n-1):
            if v[i]>v[i+1]:
                bad+=1
        pq=[]
        for i in range(n-1):
            heapq.heappush(pq,(v[i]+v[i+1],i))
        cnt=0
        while bad>0:
            s,i=heapq.heappop(pq)
            j=r[i]
            if j>=n or not alive[i] or not alive[j] or v[i]+v[j]!=s:
                continue
            pi,nj=l[i],r[j]
            if pi>=0 and alive[pi] and v[pi]>v[i]:
                bad-=1
            if v[i]>v[j]:
                bad-=1
            if nj<n and alive[nj] and v[j]>v[nj]:
                bad-=1
            v[i]=s
            alive[j]=False
            r[i]=nj
            if nj<n:
                l[nj]=i
            if pi>=0 and alive[pi] and v[pi]>v[i]:
                bad+=1
            if nj<n and alive[nj] and v[i]>v[nj]:
                bad+=1
            if pi>=0 and alive[pi]:
                heapq.heappush(pq,(v[pi]+v[i],pi))
            if nj<n and alive[nj]:
                heapq.heappush(pq,(v[i]+v[nj],i))
            cnt+=1
        return cnt

if __name__=='__main__':
    sol=Solution()
    print(sol.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))