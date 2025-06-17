class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        left,right=1,max(nums)
        while left<=right:
            mid=(left+right)//2
            record=0
            for i in nums:
                record+=(i-1)//mid
            if record>maxOperations:
                left=mid+1
            else:
                ans=mid
                right=mid-1
        return ans
            
            