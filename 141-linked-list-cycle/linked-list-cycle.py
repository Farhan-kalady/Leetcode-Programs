# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        pointer = head
        visited = set()
        visited.add(head)
        while True:
            pointer = pointer.next
            if not pointer:
                return False
            if pointer in visited:
                return True
            visited.add(pointer)        