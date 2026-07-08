# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        i = head
        j = head
        while j is not None and j.next is not None:
            i = i.next
            j = j.next.next

            if i == j:
                return True
        return False           