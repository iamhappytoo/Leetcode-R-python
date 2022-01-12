##My Solution 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        start=ListNode()
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        pt1 = list1
        pt2 = list2
        pt = start
        start.next=head
        while pt1 is not None and pt2 is not None:
            if pt1.val < pt2.val:                
                pt.next=pt1
                pt1=pt1.next
                pt=pt.next
            elif pt1.val > pt2.val:
                pt.next=pt2
                pt2=pt2.next
                pt=pt.next
            else:
                pt.next=pt1
                pt1=pt1.next
                pt=pt.next
                pt.next=pt2
                pt2=pt2.next
                pt=pt.next
        if pt1 is None and pt2 is None:
            return start.next
        elif pt1 is None:
            pt.next=pt2
            return start.next
        else:
            pt.next = pt1
            return start.next 
##Optimize:
1. list1, list2 can directly be pt1, pt2, no need to redefine pt1, pt2.
2. no need to consider the pt1.val==pt2.val case, just select one when equal, so assign to the pointer when <=. 
3. No need to put pt=pt.next everywhere, just put it at the end. 
4. No need to write multiline elif etc at the end, can be one line. 

##Optimized code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev=ListNode()
        prevhead=prev
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 and list2:
            if list1.val <= list2.val:                
                prev.next=list1
                list1=list1.next
            else:
                prev.next=list2
                list2=list2.next
            prev=prev.next
        prev.next = list1 or list2
        return prevhead.next 
        
##Another recursive way:
class Solution:
  def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
          
