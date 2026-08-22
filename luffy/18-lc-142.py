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
        # 1. Initialize Pointers / 初始化指针
        # Both slow and fast pointers start at the head of the linked list.
        # 慢指针和快指针都从链表头节点开始。
        slow = head
        fast = head
        
        # 2. Detect the Cycle / 检测环的存在
        # Move slow by 1 step and fast by 2 steps.
        # 每次让慢指针走1步，快指针走2步。
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle exists.
            # 如果快慢指针相遇，说明链表中存在环。
            if slow == fast:
                
                # 3. Find the Cycle Entrance / 寻找环的入口
                # The distance from the head to the cycle's entrance equals 
                # the distance from the meeting point to the entrance.
                # 从链表头部到环入口的距离，正好等于从相遇点到环入口的距离。
                point1 = head
                point2 = slow
                
                # Move both pointers 1 step at a time until they meet.
                # 两个新指针每次各走1步，直到它们再次相遇。
                while point1 != point2:
                    point1 = point1.next
                    point2 = point2.next
                    
                # 4. Return Result / 返回结果
                # The node where they meet is the start of the cycle.
                # 它们相遇的节点就是环的起始入口节点。
                return point1
                
        # If the loop finishes without returning, it means we reached the end of the list (no cycle).
        # 如果循环结束都没有相遇（遇到了 None），说明走到了链表尽头，不存在环。
        return None


            


        
        