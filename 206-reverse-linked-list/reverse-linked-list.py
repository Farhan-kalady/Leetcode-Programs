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
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return head        