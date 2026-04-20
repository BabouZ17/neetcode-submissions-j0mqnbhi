import random

class Solution:

    def __init__(self, w: List[int]):
        total = 0
        for val in w:
            total += val
        self.weights = [val / total for val in w]
        self.indexes = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.indexes, weights=self.weights, k=1)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()