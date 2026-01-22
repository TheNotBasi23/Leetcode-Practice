from tkinter.constants import SEL


class MinStack:
    stack =[]
    minItems = []
    def __init__(self):
        self.stack = []
        self.minItems = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val)
            self.minItems.append(min(val,self.minItems[-1]))
        else:
            self.stack.append(val)
            self.minItems.append(val)


    def pop(self) -> None:
        if self.stack:
            self.minItems.pop()
            return self.stack.pop(-1)
        else:
            return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minItems:
            return self.minItems[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()