old =[]
new = []
for i in range(int(input())):
    val = list(map(int,input().split()))
    if val[0] == 1:
        new.append(val[1])
    elif val[0] == 2:
        if not old:
            while new: old.append(new.pop())
        old.pop()
    else:            
        print(old[-1] if old else new[0])

        
##Another way using the class object:
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[0]
    def empty(self) -> bool:
        if not self.s1 and not self.s2: 
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
