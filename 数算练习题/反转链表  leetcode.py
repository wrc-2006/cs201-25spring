# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        ans=None
        while cur:
            newnode=cur.next
            cur.next=ans
            ans=cur
            cur=newnode
        return ans
            