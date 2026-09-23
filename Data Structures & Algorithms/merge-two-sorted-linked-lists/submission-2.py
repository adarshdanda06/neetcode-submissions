# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 4 5 6
# 1 2 3


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        curr1 = list1
        curr2 = list2
        node = ListNode(0, None)
        copy = node

        while (curr1 != None and curr2 != None):
            if (curr1.val <= curr2.val):
                node.next = curr1
                curr1 = curr1.next
                node = node.next
            elif (curr1 != None and curr2.val <= curr1.val):
                node.next = curr2
                curr2 = curr2.next
                node = node.next

        if (curr1 == None and curr2 != None):
            node.next = curr2
        elif (curr2 == None and curr1 != None):
            node.next = curr1

        return copy.next