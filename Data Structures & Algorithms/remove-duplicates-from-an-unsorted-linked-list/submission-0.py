# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freqCount = {}
        copy = head

        while copy:
            freqCount[copy.val] = freqCount.get(copy.val, 0) + 1
            copy = copy.next
        prev = ListNode(next=head)
        start = prev
        copy = head
                        #c   
                # p  -> 1 --> 2 --> 3 --> 2

        while copy:
            checkDup = freqCount[copy.val] > 1
            if checkDup:
                prev.next = copy.next
            copy = copy.next
            
            if not checkDup:
                prev = prev.next

        return start.next
        