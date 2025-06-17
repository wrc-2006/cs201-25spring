# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pre=None
        while slow:
            newnode=slow.next
            slow.next=pre
            pre=slow
            slow=newnode
        while pre:
            if head.val!=pre.val:
                return False
            head=head.next
            pre=pre.next
        return True

def link(arr):
    if not arr:
        return None
    head=ListNode(arr[0])
    cur=head
    for val in arr[1:]:
        cur.next=ListNode(val)
        cur=cur.next
    return head