from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        d1 = ListNode(-1)
        d2 = ListNode(-1)

        p1 = d1
        p2 = d2


        p = head

        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next

            else:
                p1.next = p
                p1 = p1.next

            temp = p.next
            p.next = None

            p = temp

        p1.next = d2.next

        return d1.next

    

