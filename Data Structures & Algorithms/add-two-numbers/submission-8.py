# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Test Change 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumOf, store = 0, 0

        head = ListNode()
        res = head

        arr = []
        while (l1 or l2):
            if (l1 and l2):
                sumOf = l1.val + l2.val + store
            elif (l1):
                sumOf = l1.val + store
            else:
                sumOf = l2.val + store

            arr.append(sumOf % 10)
            res.next = ListNode(sumOf % 10)

            print(sumOf % 10)
            res = res.next
            store = sumOf // 10
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next
        
        if (store != 0):
            arr.append(store)
            res.next = ListNode(store, None)
        
        print(arr)
        return head.next
# T3

# Test change 2

        