# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        prev = None
        while(head.next != None):
            hnext = head.next
            head.next = prev
            prev = head
            head = hnext
        head.next = prev
        return head
        # 1 -> 2 -> 3 -> 4
        #
