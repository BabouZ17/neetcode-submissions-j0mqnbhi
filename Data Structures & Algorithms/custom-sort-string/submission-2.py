import string
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        customerOrder = {}
        for i in range(len(order)):
            customerOrder[order[i]] = i

        i = 0
        for letter in string.ascii_lowercase:
            if letter not in customerOrder:
                customerOrder[letter] = i + 100
                i += 1
        return "".join(sorted(s, key=lambda x: customerOrder.get(x, 100)))
    