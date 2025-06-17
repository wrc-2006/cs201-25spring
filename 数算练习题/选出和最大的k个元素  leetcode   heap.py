'''
class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        lst=[(nums1[i],i) for i in range(len(nums1))]
        lst.sort()
        record=[[]for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if lst[j][0]<nums1[i]:    
                    record[i].append(lst[j][1])
                else:
                    break
        newre=[[]for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in record[i]:
                newre[i].append(nums2[j])
            if len(newre[i])>k:
                newre[i].sort(reverse=True)
                newre[i]=newre[i][:k]
        ans=[[] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            ans[i]=sum(newre[i])
        return ans 
'''        

import heapq
class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        lst=[(nums1[i],i,nums2[i]) for i in range(len(nums1))]
        lst.sort()
        ans=[0]*(len(nums1))
        pq=[]
        sumpq=0
        re=[]
        for i in range(1,len(nums1)):
            cnt=lst[i][1]
            if lst[i-1][0]<lst[i][0]:
                heapq.heappush(pq,lst[i-1][2])
                for a in re:
                    heapq.heappush(pq,a)
                    sumpq+=a
                    re=[]
                sumpq+=lst[i-1][2]
            else:
                re.append(lst[i-1][2])
            while len(pq)>k:
                sumpq-=heapq.heappop(pq)
            ans[cnt]=sumpq
            
        return ans
if __name__=='__main__':
    sol=Solution()
    print(sol.findMaxSum([18,11,24,9,10,11,7,29,16], [28,26,27,4,2,19,23,1,2], 1))