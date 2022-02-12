# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode
        curr = head
        inherit = 0
        while l1 is not None and l2 is not None:
            Sum = l1.val + l2.val + inherit
            if Sum >= 10:
                inherit = 1
                Sum -= 10  
            else:
                inherit = 0
            curr.next = ListNode(val=Sum)
            curr = curr.next                      
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 is not None else l2
        while l is not None:
            Sum = l.val + inherit
            if Sum >=10:
                inherit = 1
                Sum -= 10
            else:
                inherit = 0
            curr.next = ListNode(Sum)
            curr = curr.next
            l = l.next
        
        if inherit > 0:
            curr.next = ListNode(inherit)
        return head.next
      
      
##Simplified version
class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
   
class Solution:
  def addTwoNumbers(self, l1, l2):
    result = ListNode(0)
    result_tail = result
    carry = 0
    while l1 or l2 or carry:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      carry, out = divmod(val1 + val2 + carry, 10)
      result_tail.next = ListNode(val = out)
      result_tail = result_tail.next 
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
  return result.next
