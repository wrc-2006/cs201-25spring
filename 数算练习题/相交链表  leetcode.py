# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pointerA,pointerB=headA,headB
        while pointerA!=pointerB:
            pointerA=headB if pointerA is None else pointerA.next
            pointerB=headA if pointerB is None else pointerB.next
        return pointerA