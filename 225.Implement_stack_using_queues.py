##Solution push O(1), pop O(n)
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        n = len(self.q1)
        for i in range(n-1):
            self.q2.append(self.q1.pop(0))
        n = len(self.q2)
        for i in range(n):
            self.q1.append(self.q2.pop(0))
        return self.q1.pop(0)
    def top(self) -> int:
        n = len(self.q1)
        for i in range(n-1):
            self.q2.append(self.q1.pop(0))
        out = self.q1[0]
        self.q2.append(self.q1.pop(0))
        n = len(self.q2)
        for i in range(n):
            self.q1.append(self.q2.pop(0))
        return out
    def empty(self) -> bool:
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False
            
            
##Solution push O(n) pop O(1)
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        n = len(self.q1)
        for i in range(n):
            self.q2.append(self.q1.pop(0))
        self.q2, self.q1 = self.q1, self.q2

    def pop(self) -> int:
        return self.q1.pop(0)
    def top(self) -> int:
        out = self.q1[0]
        return out
    def empty(self) -> bool:
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

###Solution with one queue
class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)
        for i in range(n-1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        return self.q.pop(0)
    def top(self) -> int:
        out = self.q[0]
        return out
    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
