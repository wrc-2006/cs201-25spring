import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int 
        :rtype: int
        """
        return bisect.bisect_left(nums,target)
        