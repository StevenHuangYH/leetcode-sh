#lc-155-min-stack


class MinStack:

    def __init__(self):
        self.data_stack=[]
        self.min_stack=[]

    def push(self, value: int) -> None:
        self.data_stack.append(value)
        if self.min_stack:
            top=self.min_stack[-1]
            min_value=min(value,top)
            self.min_stack.append(min_value)
        else:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.data_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()