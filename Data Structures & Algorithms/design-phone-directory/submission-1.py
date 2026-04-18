from collections import deque

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.queue = deque(range(maxNumbers))
        self.used = set()

    def get(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.popleft()
        self.used.add(val)
        return val

    def check(self, number: int) -> bool:
        return number not in self.used

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.queue.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
