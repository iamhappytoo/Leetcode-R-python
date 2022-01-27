class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def get(self,index):
        if index>self.size-1 or index < 0:
            return -1
        else:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            return curr.val
##Here head is sentinel node, head.next is node at index 0 , head.next.next is node at index 1
    def addAtHead(self,val):
        self.addAtIndex(0,val)

    def addAtTail(self,val):
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
            
        self.size += 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        toinsert = ListNode(val)
        toinsert.next= prev.next
        prev.next = toinsert

    def deleteAtIndex(self, index):
        if index > self.size - 1 or index < 0:
            return
        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
