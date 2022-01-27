# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        stat = ListNode(0)
        stat.next = head
        prev, curr = stat, head
        while curr:
            if curr.val != val:
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return stat.next
