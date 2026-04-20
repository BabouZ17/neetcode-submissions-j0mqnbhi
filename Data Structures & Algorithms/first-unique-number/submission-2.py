from collections import deque

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.unique = dict()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and not self.unique[self.queue[0]]:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.unique:
            self.unique[value] = False
        else:
            self.queue.append(value)
            self.unique[value] = True
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
