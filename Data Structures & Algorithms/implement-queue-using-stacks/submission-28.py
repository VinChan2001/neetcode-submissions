#pop() should pop from left (front of the queue)
#push() should push to the back of the queue 
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        
    def peek(self) -> int:
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        if (not self.s1) and (not self.s2):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()