class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None
        self.minVals = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minVal = val
        
        if val <= self.minVal:
            if self.stack:
                self.minVals.append(self.minVal)
            self.minVal = val
            
        self.stack.append(val)

    def pop(self) -> None:
        if self.top() == self.minVal:
            if self.minVals: 
                self.minVal = self.minVals.pop()
            else:
                self.minVal = None
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        
# stack = []
# minVal = null
# minVals = [] append minVal to minVals if val <= minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time complexity: O(1)
# Space complexity: O(n)
# Pattern: Stack
# Time used: 38min