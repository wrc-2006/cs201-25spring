'''
import sys
sys.setrecursionlimit(1<<30)
from collections import defaultdict
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        ans=[]
        def dfs(st,ed):
            if st==ed:
                return True
            lst=graph[st]
            for i in lst:
                if i not in visited:
                    if dfs(i,ed):
                        return True
            return False
        graph=defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])<=maxDiff:
                    graph[i].append(j)
                    graph[j].append(i)
        for st,ed in queries:
            visited=set()
            visited.add(st)
            ans.append(dfs(st,ed))
        return ans  
'''
'''
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        lst=[]
        ans=[]
        for i in range(n):
            record=[i]
            for j in range(i+1,n):
                if nums[j]-nums[j-1]<=maxDiff:
                    record.append(j)
                else:
                    break
            if len(record)>1:
                lst.append(record)
        print(lst)
        for st,ed in queries:
            if st==ed:
                ans.append(True)
                continue
            for i in lst:
                if st in i and ed in i:
                    ans.append(True)
                    break
            else:
                ans.append(False)
        return ans
'''   
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        a=[0]*n
        pos=0
        for i in range(n-1):
            if nums[i+1]-nums[i]<=maxDiff:
                a[i]=a[i+1]=pos
            else:
                a[i]=pos
                pos+=1
                a[i+1]=pos
        m=len(queries)
        ans=[False]*m
        for i in range(m):
            u,v=queries[i][0],queries[i][1]
            if a[u]==a[v]:
                ans[i]=True
            else:
                ans[i]=False
        return ans

if __name__ =='__main__':
    sol=Solution()
    print(sol.pathExistenceQueries(4,[2,5,6,8],2,[[0,1],[0,2],[1,3],[2,3]]))