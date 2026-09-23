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
        node = ListNode(0, None)
        copy = node

        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                node.next = list1
                list1 = list1.next
                node = node.next
            elif (list2.val <= list1.val):
                node.next = list2
                list2 = list2.next
                node = node.next

        if (list1 == None and list2 != None):
            node.next = list2
        elif (list2 == None and list1 != None):
            node.next = list1

        return copy.next