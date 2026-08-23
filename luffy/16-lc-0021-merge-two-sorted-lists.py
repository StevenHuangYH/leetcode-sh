#lc-21
#merge two sorted lists
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy-虚拟头节点
        dummy=ListNode()
        current=dummy
        while list1!=None and list2!=None:
            if list1.val <=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1 == None:
            current.next=list2
        else:
            current.next=list1

        return dummy.next


