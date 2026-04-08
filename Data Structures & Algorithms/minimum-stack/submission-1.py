class StackEmptyError(Exception):
    pass


class MinStack:

    def __init__(self):
        self.values = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.values.append((val, self.min))

    def is_empty(self) -> bool:
        return len(self.values) == 0

    def pop(self) -> None:
        if not self.is_empty():
            value, prev_min = self.values[-1]
            self.values = self.values[:len(self.values) - 1]

            if not self.is_empty():
                self.min = self.values[-1][1]
            else:
                self.min = float('inf')

            return value
        else:
            raise StackEmptyError("Stack is empty")

    def top(self) -> int:
        if not self.is_empty():
            return self.values[-1][0]
        else:
            raise StackEmptyError("Stack is empty")        

    def getMin(self) -> int:
        return self.min
        
