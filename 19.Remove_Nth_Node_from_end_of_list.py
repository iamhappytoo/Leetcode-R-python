# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr:
            curr=curr.next
            cnt += 1
        N = cnt
        target = N-n
        if target == 0:
            head = head.next
            return head
        else:
            curr = head
            i = 0
            while i < N-n-1:
                curr = curr.next
                i += 1
            curr.next = curr.next.next
            return head

###Do that in one pass (with two pointers):
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        right = dummy
        left = dummy
        cnt = 0
        while right and cnt < n:
            right=right.next
            cnt += 1
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
