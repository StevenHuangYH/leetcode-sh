#lc-142
#listed-list-cycle
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow =slow.next
            fast=fast.next.next

            if slow==fast:
                point1=head
                point2=slow
                while point1!=point2:
                    point1=point1.next
                    point2=point2.next

                return point1


        return None
    


            


        
        