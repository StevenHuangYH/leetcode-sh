# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur=None 
#         while head!=None:
#             cur =ListNode(head.val,cur)
#             head=head.next

#         return cur



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        
        while head!=None:
            next_node=head.next
            head.next=pre
            pre=head
            head=next_node
        return pre
        



         


