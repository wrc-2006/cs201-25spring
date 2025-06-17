class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        dic={}
        for i in nums:
            if i in dic:
                dic.pop(i)
            else:
                dic[i]=1
        key=list(dic.keys())
        return key[0]
        '''
        ###位操作
        ans=nums[0]
        for i in nums[1:]:
            ans^=i
        return ans