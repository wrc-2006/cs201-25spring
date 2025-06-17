class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        def backtrack(st,record):
            ans.append(record)
            for i in range(st,len(nums)):
                backtrack(i+1,record+[nums[i]])
        backtrack(0,[])
        return ans