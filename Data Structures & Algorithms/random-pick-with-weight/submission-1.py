import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        currSum = 0

        for i in range(len(self.w)):
            currSum += self.w[i]
            if currSum > target:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()