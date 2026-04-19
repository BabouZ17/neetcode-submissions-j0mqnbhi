import random

from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.index_mapping = dict()
        self.vals = list()

    def insert(self, val: int) -> bool:
        if val not in self.index_mapping:
            self.index_mapping[val] = len(self.vals)
            self.vals.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index_mapping:
            last_element = self.vals[-1]
            val_idx = self.index_mapping[val]
            
            self.vals[val_idx] = last_element
            self.index_mapping[last_element] = val_idx

            self.vals.pop()
            del self.index_mapping[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.vals)
