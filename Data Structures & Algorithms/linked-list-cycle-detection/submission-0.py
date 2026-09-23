# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        curr = head.next
        while (curr.next and curr.next.next):
            if curr == head:
                return True
            head = head.next
            curr = curr.next.next
        return False