# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def dfs(nums):
            mid=len(nums)//2
            lst=[None]*len(nums)
            for i in range(len(nums)):
                lst[i]=TreeNode(nums[i])
            if len(nums)==1:
                return lst[0]
            if len(nums)==2:
                lst[0].right=lst[1]
                return lst[0]
            lst[mid].left=dfs(nums[:mid])
            lst[mid].right=dfs(nums[mid+1:])
            return lst[mid]
        return dfs(nums)
        
        
            
        
        
        