# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        leftprev = dummy
        # Move leftprev to the node before where reversal starts
        for i in range(left - 1):
            leftprev = leftprev.next

        # Start reversal
        prev = None
        curr = leftprev.next
        for i in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpNext

        # Connect reversed section back to list
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
