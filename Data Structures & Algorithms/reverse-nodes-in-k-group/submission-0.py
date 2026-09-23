# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k = 3


        #p_
        # <- 1 <- 2 <- 3     4 -> 5 -> 6
        #              se    n
        # 3 -> 2 -> 1 ->  <- 4 <- 5 <- 6
        #           p.       p          se n
        #         p   st   snp
        # <- 1 <- 2 <- 3 
        # <- 1 <- 2 <- 3



        #                p   st
        # k_prev pointer, points to end of last seq
        # start pointer, copy pointer (which becomes prev for the next group of k)
        # end pointer hops k - 1 elems ahead of start
            # if we get a null val when getting there, leave group as is 
        # get e->next and keep that as nextGroup pointer
        # reverse linked list from s to e


        orig = head
        copy, start, end = head, head, head
        count = 0
        k_prev = None
        k_group = 0
    
        #  re       kp   k_g_n
        #  3 -> 2-> 1 ->   4  -> 5 -> 6
        #           c        
        while end:
            end = end.next
            count += 1

            if end and count == k - 1:
                k_group_n = end.next
                rev_prev = None
                
                for i in range(k):
                    s_n_p = start.next
                    start.next = rev_prev
                    rev_prev = start
                    start = s_n_p
                
                if k_group == 0:
                    orig = end
                k_group += 1

                copy.next = k_group_n
                if k_prev:
                    k_prev.next = end
                k_prev = copy
                count = 0
                copy, start, end = k_group_n, k_group_n, k_group_n


        return orig


                # start of reverse list, end
                # k_prev
            #           r    e    n
            # <- 1  <-  2 <- 3   4 -> 5 -> 6 -> 7 -> 8
    #k_prev     c                 s_.        

            # 3 -> 2 -> 1 ->      6 -> 5 -> 4 -> 7 -> 8

        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        # k = 2

