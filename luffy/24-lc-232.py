#lc-232:
#implement queue using stacks


class MyQueue:

    def __init__(self):
        self.input_stack=[]
        self.out_stack=[]
        

    def push(self, x: int) -> None:
        self.input_stack.append(x)
        
        

    def pop(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.input_stack:
                self.out_stack.append(self.input_stack.pop())

            return self.out_stack.pop()
        

    
    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        while self.input_stack:
            self.out_stack.append(self.input_stack.pop())
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        if self.input_stack or self.out_stack:
            return False
        else:
            return True

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()