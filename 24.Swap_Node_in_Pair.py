# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        nextstep = head.next
        savehead = head.next
        prev = ListNode()
        while curr and curr.next:
            temp = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp
            prev = curr
            curr = temp
            
        return savehead
###Using a easier to understand denotation
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next
            
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            prev_node = first_node
            head = first_node.next
            
        return dummy.next
###Using a recursive way
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next
         
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node
        
