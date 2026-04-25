class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.vals = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.vals[i]

    def set(self, i: int, n: int) -> None:
        self.vals[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        self.vals[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.getSize() > 0:
            self.size -= 1
        return self.vals[self.size]

    def resize(self) -> None:
        self.capacity *= 2

        new_vals = [0] * self.capacity
        for i in range(self.size):
            new_vals[i] = self.vals[i]

        self.vals = new_vals 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity