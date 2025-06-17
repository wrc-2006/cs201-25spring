class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        if len(nums)==0:
            return [[]]
        for i in range(len(nums)):
            cur=nums[i]
            remain=nums[:i]+nums[i+1:]
            repermute=self.permute(remain)
            for a in repermute:
                ans.append([cur]+a)
        return ans 
            